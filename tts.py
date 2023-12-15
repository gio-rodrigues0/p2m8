import soundfile as sf
import simpleaudio as sa

from txtai.pipeline import TextToSpeech

# Build pipeline
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

def text_to_speech(text):
    print('Reproduzindo...')
    # Generate speech
    speech = tts(text)

    # Write to file
    sf.write("out.wav", speech, 22050)

    # Read the file
    wave_obj = sa.WaveObject.from_wave_file("out.wav")

    # Play audio
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until audio finishes playing

while True:
    command = input("Digite o que quer dizer:")
    if command == "sair":
        break
    text_to_speech(command)
    