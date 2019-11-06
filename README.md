![Speech to type](https://i.imgur.com/ZmpqVy5.png?1)

# Speech To Type
Basic python script that continuously listens to your voice and transforms it to keyboard typing events. It types on an active window basically.

## Required Packages

#### [pyaudio](http://people.csail.mit.edu/hubert/pyaudio/)

`sudo apt-get install python-pyaudio python3-pyaudio`

`sudo pip3 install SpeechRecognition`

#### [pynput](https://pynput.readthedocs.io/en/latest/)

`sudo pip3 install pynput`

## Configuring Microphones

Make sure to change your mic name, sample rate and chunk size to appropriate plugged in device. In my case device name is following.

`mic_name = "Plantronics .Audio 628 USB: Audio (hw:2,0)"`

You can get list of available mics from `sr.Microphone.list_microphone_names()` function.

## Run

`python3 speech.py`
