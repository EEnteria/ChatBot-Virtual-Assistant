import speech_recognition as sr
import pyaudio


r = sr.Recognizer()


with sr.Microphone() as source2:
    print("setting up...")
    r.adjust_for_ambient_noise(source2,duration = 1)
    print("Go ahead and speak!")

    audio2 = r.listen(source2, 10)


    Text = r.recognize_houndify(audio2,"9kAZxer4_FLIh9EoDZEtFA==","tNBJvex-K_VXNhRUGdTtrY66FEV--kocbjQsCCJW46GUJprXHrxR3yNuLU1F7vyjGM_4NDiYElC6J765bUuwgg==")
    Text = Text.lower()

    print("Did you say " + Text)
    
    
    

