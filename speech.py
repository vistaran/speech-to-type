#
# Open source, MIT License
# AUTHOR: Jay Shah
# Company: Vistaran Techtronix Pvt Ltd.
# Date created: 01-11-2019
#

import speech_recognition as sr
import time
from pynput.keyboard import Key, Controller

#use the microphone as source for input. Here, we also specif 
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"

#enter the name of usb microphone that you found
#using lsusb
#the following name is only used as an example
mic_name = "Plantronics .Audio 628 USB: Audio (hw:2,0)"
#Sample rate is how often values are recorded
sample_rate = 44100
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here.
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 512
#Initialize the recognizer

#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    # print(microphone_name)
    if microphone_name == mic_name:
        device_id = i

print('DEVICE >> ')
print(device_id)

def recog(source):
    #wait for a second to let the recognizer adjust the
    #energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print("Say Something...")
    #listens for the user's input
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        keyboard = Controller()
        keyboard.type(text)
        # print("you said: " + text)
    #error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
        while True:
            recog(source)