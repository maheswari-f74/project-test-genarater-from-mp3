# -*- coding: utf-8 -*-
"""project text generation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FYsGw4G0f9KeBtYfM2BbWtV_GyGDMqiN
"""

!pip install gtts

from gtts import gTTS

!pip install SpeechRecognition

import speech_recognition as sr

model = sr.Recognizer()

!pip install pydub

mp3_file=r'/content/class.mp3'
from pydub import AudioSegment
from pydub.playback import play
audio=AudioSegment.from_file(mp3_file)
audio.export("temp2.wav",format="wav")

audio_file=r'/content/temp2.wav'
with sr.AudioFile(audio_file) as source:
  #reco.adjust_for_ambient_noise(source)
  audio_data = model.record(source)
  text=model.recognize_google(audio_data)
text

pip install transformers

from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

text_input = input('enter some text:')

result = analyzer(text_input)

result

summarize = pipeline('summarization')

text = input('')

result = summarize(text)

result

q_a = pipeline('question-answering')

while True:
    question = input("Ask a question about video: ")
    result = q_a({
        'question': question,
        'context': """
        Recursion is just another way to create a loop but infinite Loops aren't very useful in practice in practice . Recursive functions are not the right choice in every situation but they are very good for tree and graph traversals . In the next video I'll explain how to improve this with memoization .
        """
    })
    print(result)