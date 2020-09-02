from my_git.playPub.axon.shared_memory import SharedMemoryGenerator, get_shared_memory_object
import cv2
from my_git.playPub.axon.mb_shared_pb2 import FrameMetadata
import zmq

zmq_port = "5581"

zmq_address = "tcp://0.0.0.0:{PORT}".format(PORT=zmq_port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(zmq_address)


cap = cv2.VideoCapture("test.mp4")
generator = SharedMemoryGenerator("sm_name")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        frame_buf = frame.tobytes()

        memory_name = generator.get_next_shared_memory(size=len(frame_buf))
        memory = get_shared_memory_object(memory_name)
        memory.acquire_semaphore()
        memory.write_to_memory(frame_buf)
        memory.release_semaphore()


        # proto

        frame_metadata = FrameMetadata()
        frame_metadata.id = 12  # "uint32"
        frame_metadata.timeUtc = 123  # "uint64"

        height, width, channels = frame.shape

        frame_metadata.rasterInfo.size.width = width  # "int32" #shape[0]
        frame_metadata.rasterInfo.size.height = height  # "int32" #shape[1]

        frame_metadata.rasterInfo.channels = channels  # "uint32" #shape[2]
        frame_metadata.rasterInfo.offsetInContainer = 0  # "uint32"

        frame_metadata.rasterInfo.containerDescriptor.uri = memory_name  # Shared memory name

        # inserted only the fields that is being used by demo we got (might add the other fields later)

        # send in zmq
        socket.send_string("frameData", zmq.SNDMORE)
        socket.send(frame_metadata.SerializeToString(), zmq.NOBLOCK)

    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
