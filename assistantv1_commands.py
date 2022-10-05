import transcribe as t
import database as d

def listen(microphone=None, recognizer=None):

	audio_sample = t.record()
	#print(audio_sample)

	command_line = ['']
	for i in range(len(audio_sample)):
		#print(command_line)
		if audio_sample[i]==' ': command_line.append('')
		else: command_line[-1]+=audio_sample[i]

	return command_line

def simplify(word_list, accepted_commands):

	simplified_list = []
	for i in range(len(word_list)):
		if word_list[i] in accepted_commands: simplified_list.append(word_list[i])

	return simplified_list

if __name__=="__main__":
	
	print("Testing Listen function:")

	print(listen())

	print("Testing Simplify function:")

	print(simplify(listen(), ['where', 'file']))
	
	