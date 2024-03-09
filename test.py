from pydub import AudioSegment
from pydub.playback import play
 
song = AudioSegment.from_wav('timer.wav')
while(1)
play(song)