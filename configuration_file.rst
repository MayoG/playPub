Configuration file
=======

Configuration file or config file is a file designed to upload to the pipeline 
a pre-made pipeline with all of its components already set with their routines.

There are two ways to generate a config file:
The first is to generate it from a pipeline that you made with the cli using 
the command export_config_file.

The second is to write one on your own. 
Here is an example of how a config file looks like and an explanation on its structure:
```
1.   - name: Stream
2.     queues:
3.     - video
4.     routines:
5.      - fps: 23.976023976023978
6.       name: capture_frame
7.       out_queue: video
8.       routine_type_name: ListenToStream
9.       stream_address: /home/internet/Desktop/video.mp4
10.    - max_stream_length: 10
11.      message_queue: video
12.      name: upload_redis
13.      redis_send_key: camera:0
14.      routine_type_name: MessageToRedis
15.  - name: Display
16.    queues:
17.    - messages
18.    routines:
19.    - message_queue: messages
20.      name: get_frames
21.      redis_read_key: camera:0
22.      routine_type_name: MessageFromRedis
23.    - frame_queue: messages
24.      name: draw_frames
25.      routine_type_name: DisplayCv2
```

```yaml
- name: Stream
  queues:
  - video
  routines:
  - fps: 23.976023976023978
    name: capture_frame
    out_queue: video
    routine_type_name: ListenToStream
    stream_address: /home/internet/Desktop/video.mp4
  - max_stream_length: 10
    message_queue: video
    name: upload_redis
    redis_send_key: camera:0
    routine_type_name: MessageToRedis
- name: Display
  queues:
  - messages
  routines:
  - message_queue: messages
    name: get_frames
    redis_read_key: camera:0
    routine_type_name: MessageFromRedis
  - frame_queue: messages
    name: draw_frames
    routine_type_name: DisplayCv2
```
```yaml
en:
  errors:
    format: "%{attribute} %{message}"
    messages:
      confirmation: "doesn't match %{attribute}"
      accepted: "must be accepted"
      wrong_length:
        one: "is the wrong length (should be 1 character)"
        other: "is the wrong length (should be %{count} characters)"
      equal_to: "must be equal to %{count}"
```

.. code-block:: yaml
  errors:
    format: "%{attribute} %{message}"
    messages:
      confirmation: "doesn't match %{attribute}"
      accepted: "must be accepted"
      wrong_length:
        one: "is the wrong length (should be 1 character)"
        other: "is the wrong length (should be %{count} characters)"
      equal_to: "must be equal to %{count}"
