from jsonschema import validate, ValidationError

schem = {
    "type": "array",
    "items" : {
        "type": "object",
        "properties" : {
            "name" : {"type" : "string"},
            "queues" : {"type" : "array", "items" : {"type": "string"}},
            "routines" : {
                "type" : "array",
                "items" : {
                    "type": "object",
                    "properties" : {
                        "routine_type_name" : {"type" : "string"}
                    },
                    "required": ["routine_type_name"]

                }
            }
        },
        "required": ["name", "queues", "routines"]
    }
}

data = [
    {
        "name": "Stream",
        "queues": ["video"],
        "routines":
        [
            {
                "routine_type_name": "ListenToStream",
                "stream_address":
                    "0",
                "out_queue": "video",
                "fps": 30,
                "name": "capture_frame"
            },
            {
                "routine_type_name": "MessageToRedis",
                "redis_send_key": "cam",
                "message_queue": "video",
                "max_stream_length": 10,
                "name": "upload_redis"
            }
        ]
    },
    {
        "name": "Display",
        "queues": ["messages"],
        "routines":
        [
            {
                "routine_type_name": "MessageFromRedis",
                "redis_read_key": "cam",
                "message_queue": "messages",
                "name": "get_frames"
            },
            {
                "routine_type_name": "DisplayCv2",
                "frame_queue": "messages",
                "name": "draw_frames"
            }
        ]
    },
]

try:
    print(validate(instance=data, schema=schem))
except ValidationError as error:
    print(error.message)

# print(validate(instance=data, schema=schem))
