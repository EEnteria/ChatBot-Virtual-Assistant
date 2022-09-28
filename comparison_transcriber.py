import speech_recognition as sr
import pyaudio





#Initializes listening for mic input, includes transription for now, might separate later
def mic_input():
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

        return Text #Used for other functions as a comparison

    

def compare_transcription(): #Will be hard coded to access the transcript and the test file.
    '''Purpose of this is to test the accuracy of the transcript as compared to the test file. When inputting things into the original transcript file, make sure it is all lower case
        and without punctuation.

    '''

    with open("test_transcript.txt","r") as f:
        true_transcript =  f.read()

    with open("transcript.txt","r") as t:
        transcript = t.read()

    test_trans_array = [] #Variables used for comparison and rating
    correct_words = 0
    total_words = 0
    index = 0
    
    for word in true_transcript.split(): #For loop that splits and stores the original transcript
        test_trans_array.append(word)
    total_words = len(test_trans_array)
    
    for word in transcript.split():
        if word == test_trans_array[index]:
            correct_words += 1

        index += 1

    print("The total score is " + str(correct_words) + "/" + str(total_words))
    print("Or " + str((correct_words / total_words) * 100) + "%")
            
        
        
        
        
