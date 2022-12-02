import speech_recognition as sr

def record(m=sr.Microphone(), r=sr.Recognizer()):
	print("Listening...")
	with m as source: audio=r.listen(source, 7, 5)

	print("Houndify recognized:")
	return r.recognize_houndify(audio, "vObDPB9syIEOKJn4ZT8XNw==", "kRgINvNQvmpnNYun5tG0NitvlN4SahAXAXaq2IhcLq1OX2HW_jLmvUfJxC-lt9wM5dX3kC0rtGPGrrAL0yEajw==")

	#return audio

def transcribe():
	while True:
		recording = record()
		print(recording)
		if "command stop" in recording: break

	return "Transcription Ended"

if __name__ == "__main__":
	print(transcribe())