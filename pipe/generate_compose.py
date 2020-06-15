import yaml

flask_port_counter = 5000


def prometheus_handler(pods, docker_compose):
    # add the monitoring system and the port for each one of them to listen 
    # and add the services in the docker compose and generate the prometheus yaml
    
    docker_compose["services"]["prometheus"] = {
        "container_name": "prometheus",
        "image": "prom/prometheus:latest",
        "logging": {
            "driver": "none"
        },
        "networks": {
            "default": {
                "aliases": [
                    "prometheus"
                ]
            }
        },
        "restart": "always",
        "volumes": [
            "./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml"
        ],
        "ports": [
            "9090:9090"
        ]
    }

    docker_compose["services"]["grafana"] = {
        "container_name": "grafana",
        "image": "grafana/grafana:latest",
        "logging": {
            "driver": "none"
        },
        "networks": {
            "default": {
                "aliases": [
                    "grafana"
                ]
            }
        },
        "restart": "always",
        "volumes": [
            "./monitoring/provisioning/dashboards:/etc/grafana/provisioning/dashboards",
            "./monitoring/provisioning/datasources:/etc/grafana/provisioning/datasources",
            "./monitoring/dashboards:/var/lib/grafana/dashboards",
            "grafana_data:/var/lib/grafana"
        ],
        "environment": {
            "GF_INSTALL_PLUGINS": "grafana-piechart-panel"
        },
        "ports": [
            "3000:3000"
        ]
    }

def add_ports_if_needed(pod_dict, components):
    global flask_port_counter
    for component in components.values():
        if ("component_type_name" in component) and (component["component_type_name"] == "FlaskVideoDisplay"):
            pod_dict["ports"] = [f"{flask_port_counter}:{flask_port_counter}"]
            flask_port_counter+= 1
        

GENERATED_CONFIG_FILES_FOLDER = "config_files/"

docker_compose_dictionary = {
    "version": "3.7",
    "services": {
        "redis": {
            "container_name": "redis",
            "image": "redis:5.0.7-buster",
            "logging": {
                "driver": "none"
            },
            "networks": {
                "default": {
                    "aliases": [
                        "redis"
                    ]
                }
            },
            "restart": "always",
            "ports": [
                "6379:6379"
            ]
        },
        "base-pipert": {
            "container_name": "base-pipert",
            "logging": {
                "driver": "none"
            },
            "build": {
                "context": "pipe-base/."
            },
            "networks": {
                "default": {
                    "aliases": [
                        "base-pipert"
                    ]
                }
            }
        }
    }
}

pipeline_first_pod = {
  "container_name": "",
  "image": "pipert_pipert",
  "build": {
    "context": ".",
    "args": {
      "SPLUNK": "no",
      "DETECTRON": "no"
    }
  },
  "networks": {
    "default": {
      "aliases": [
        "pipert"
      ]
    }
  },
  "depends_on": [
    "redis",
    "base-pipert"
  ],
  "environment": {
    "REDIS_URL": "redis://redis:6379/0",
    "UI": "${UI:-false}",
    "UI_PORT": "${UI_PORT:-5005}",
    "CLI_ENDPOINT": "${CLI_ENDPOINT:-4001}",
    "CONFIG_PATH": ""
  }
}


with open("config_file_example.yaml") as conf:
    config_file = yaml.load(conf, Loader=yaml.FullLoader)
    print("Loaded config file")

# monitoring_system = config_file["monitoring_system"]

first_pod_name, first_pod_config = config_file["pods"].popitem()
first_pod_config_path = GENERATED_CONFIG_FILES_FOLDER + first_pod_name + ".yaml"
with open(first_pod_config_path, 'w') as pod_config_file:
    yaml.dump(first_pod_config ,pod_config_file)
    print("Created config file for pod " + first_pod_name)
pipeline_first_pod["container_name"] = first_pod_name
pipeline_first_pod["environment"]["CONFIG_PATH"] = first_pod_config_path

add_ports_if_needed(pipeline_first_pod, first_pod_config["components"])
docker_compose_dictionary["services"][first_pod_name] = pipeline_first_pod

# del config_file["pods"][first_pod_name]

PIPELINE_OTHER_POD_TEMPLATE = {
  "container_name": "",
  "image": "pipert_pipert",
  "networks": {
    "default": {
      "aliases": [
        "pipert"
      ]
    }
  },
  "depends_on": [first_pod_name],
  "environment": {
    "REDIS_URL": "redis://redis:6379/0",
    "UI": "${UI:-false}",
    "UI_PORT": "${UI_PORT:-5005}",
    "CLI_ENDPOINT": "${CLI_ENDPOINT:-4001}",
    "CONFIG_PATH": ""
  }
}

for pod_name, pod_config in config_file["pods"].items():
    pod_config_path = GENERATED_CONFIG_FILES_FOLDER + pod_name + ".yaml"
    with open(pod_config_path, 'w') as pod_config_file:
        yaml.dump(pod_config ,pod_config_file)
        print("Created config file for pod " + pod_name)
    
    current_pipeline_pod = PIPELINE_OTHER_POD_TEMPLATE.copy()

    current_pipeline_pod["container_name"] = pod_name
    current_pipeline_pod["environment"]["CONFIG_PATH"] = pod_config_path

    add_ports_if_needed(current_pipeline_pod, pod_config["components"])
    docker_compose_dictionary["services"][pod_name] = current_pipeline_pod


with open("docker-compose-new.yaml", 'w') as generated_compose:
    yaml.dump(docker_compose_dictionary, generated_compose)
    print("Generated the docker compose")