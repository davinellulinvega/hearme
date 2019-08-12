#!/usr/bin/env python3
from time import sleep
import pyaudio as pa
from queue import Queue

STREAM = None

def wire(in_data, frame_count, time_info, status_flags):

    return in_data, pa.paContinue

if __name__ == "__main__":
    # Instantiate pyaudio manager
    pm = pa.PyAudio()

    # Instantiate the input and output stream
    STREAM = pm.open(format=pa.paInt16,
                     channels=2,
                     rate=48000,
                     input=True,
                     output=True,
                     frames_per_buffer=1024,
                     start=False,
                     stream_callback=wire)


    # Start the stream
    STREAM.start_stream()

    try:
        # Wait for ever
        while True:
            sleep(5)

    except IOError:
        print('An error occurred while trying to read/write data to the streams.\n Closing the program ...')
    except KeyboardInterrupt:
        print('Closing the program ...')
    finally:
        # Stop the stream
        STREAM.stop_stream()

        # Close the stream
        STREAM.close()

        # Close the PyAudio manager
        pm.terminate()


