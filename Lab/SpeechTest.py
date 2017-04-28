# import pyTTS
# tts = pyTTS.Create()
# tts.SetVoiceByName('MSSam')
# tts.Speak("Hello, fellow Python programmer")

# import pyttsx
# engine = pyttsx.init()
#
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

from os import system
string = "My name is Jean"
system("say " + string)

# from gtts import gTTS
# blabla = ("Spoken text")
# tts = gTTS(text=blabla, lang='en')
# tts.save("test.mp3")

# import sounddevice as sd
# sd.play("test.mp3", 44100)