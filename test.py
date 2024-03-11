import sounddevice as sd
import soundfile as sf

# Replace "audio_file.mp3" or "audio_file.wav" with your actual file path
audio_file_path = "timer.mp3"
data, samplerate = sf.read(audio_file_path)
while(1):
    sd.play(data, samplerate=samplerate)
    sd.wait()