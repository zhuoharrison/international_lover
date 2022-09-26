import googletrans
import speech_recognition as sr
import pyaudio
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang = 'zh-tw'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        # print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('romantic.mp3')
playsound.playsound('romantic.mp3')

#print(googletrans.LANGUAGES)
