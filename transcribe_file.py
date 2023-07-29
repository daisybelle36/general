#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
import whisper
 
# --- VARIABLES --- #
#HEAD_INDEX = 0
#PRON_INDEX = 1
 
# --- OBJECTS ----- #
#class Entry():
#def __init__(self, head, pron, rank):
#self.head = head
#self.pron = pron
#self.rank = rank
 
# --- HELPER FUNCTIONS --- #
# none yet
 
# --- MAIN --------------- #
def main():
	# create parser
	parser = ArgumentParser(description = 'transcribe an audio file using Whisper')
	# add arguments to parser
	parser.add_argument('audio_file', help='.mp3 file, etc')
	#parser.add_argument('-w', '--word', help='col of headword, default = 1', default = 1)
	# collate/parse arguments
	args = parser.parse_args()
 	
	# read in audio
	prefix = audio[:-4]
	print(prefix)
	audio = args.audio
	currentAudio = []
 		
	# transcribe audio
	model = whisper.load_model("base")
	result = model.transcribe("audio")

	#with open(audio, 'r') as inFile:
		#for line in inFile:
			#currentAudio.append(line.strip())
			#inFile.close()
 	
	#print(currentAudio)
 
if __name__ == "__main__":
	main()


