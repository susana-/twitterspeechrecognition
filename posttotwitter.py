import speech_recognition as sr
import twitter
api = twitter.Api(consumer_key='0JpfKxuQX8oKtt47wvBDqHSsC',
                  consumer_secret='2KlKdh8Hg9RFpwbbqPQ86jqzWlnztu6IQK1xzfmP68WZ5YpOX7',
                  access_token_key='927920639754817537-ExJMKZYKVmP2zZEwnX7WJ2tfHObUCYi',
                  access_token_secret='0mu2LoZgeWEiWuwrgBcWWcqo0W6y2zKgqllKD8vaKO9Oj')

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

status = api.PostUpdate(r.recognize_sphinx(audio))
print("Status updated.")
