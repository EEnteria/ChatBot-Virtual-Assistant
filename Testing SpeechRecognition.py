import speech_recognition as sr
import pyaudio



r = sr.Recognizer()


with sr.Microphone() as source2: #Sets up a microphone as the source
    print("setting up...")
    r.adjust_for_ambient_noise(source2,duration = 1) #Indicators and adjustments
    print("Go ahead and speak!")

    audio2 = r.listen(source2, 10)


    Text = r.recognize_houndify(audio2,"9kAZxer4_FLIh9EoDZEtFA==","tNBJvex-K_VXNhRUGdTtrY66FEV--kocbjQsCCJW46GUJprXHrxR3yNuLU1F7vyjGM_4NDiYElC6J765bUuwgg==") #Houndifier is the API that it is set to. Experiment w/ other client types?
    Text = Text.lower()

    print("Did you say " + Text)
    
    transcript_cache = open("transcript.txt","w")#File that we save transcripts to temporarily, will it be overwritten?
    transcript_cache.write(Text)
    transcript_cache.close()

