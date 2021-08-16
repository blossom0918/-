import speech_recognition
import tempfile
from gtts import gTTS
import mp3play
import time
from googletrans import Translator

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')


def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts = gTTS(text=sentence, lang=lang)
		tts.save("{}.mp3".format(fp.name))
		clip = mp3play.load('{}.mp3'.format(fp.name))
		clip.play()
		time.sleep(3)
		clip.stop()
		
translator = Translator()
lang = 'en'
speak(translator.translate(listenTo(), lang).text, lang)