#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshhold = 0
print('hi')
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("At least we know it's getting here..")

print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))

