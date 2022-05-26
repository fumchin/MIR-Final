import pyaudio
import time
import numpy as np

WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    # print(len(in_data))
    # in_data = np.sign(in_data) * (1 - np.exp(-1 * np.abs(in_data)))
    # print(type(in_data))
    # in_data_list = np.array(list(in_data),  dtype='uint8')
    in_data_list = list(in_data)
    # print(type(in_data_list[1]))
    # print(in_data_list)
    # distortion_data_list = np.multiply(np.sign(in_data_list) , (1 - np.exp(-1 * np.abs(in_data_list))))
    # distortion_data_list = np.arctan(8 * np.float64(in_data_list) / 255)
    distortion_data_list = np.arctan(8 * float(in_data_list))
    # print(distortion_data_list)
    distortion_data = bytes(int(distortion_data_list*255))
    # print(in_data_list)
    # return (distortion_data, pyaudio.paContinue)
    out = bytes(distortion_data)
    return (out, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=4,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(1)

stream.stop_stream()
stream.close()

p.terminate()
# import pyaudio
# import wave
# import numpy as np
# # from scipy.io import wavefile

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 8
# RATE = 96000
# RECORD_SECONDS = 10
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 input_device_index=4,
#                 frames_per_buffer=CHUNK
#                 )

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()


# #Not really sure what b'' means in BYTE STRING but numpy needs it 
# #just like wave did...
# framesAll = b''.join(frames)

# #Use numpy to format data and reshape.  
# #PyAudio output from stream.read() is interlaced.
# result = np.fromstring(framesAll, dtype=np.int16)
# chunk_length = len(result) / CHANNELS
# result = np.reshape(result, (chunk_length, CHANNELS))

# #Write multi-channel .wav file with SciPy
# # wavfile.write(WAVE_OUTPUT_FILENAME,RATE,result)
