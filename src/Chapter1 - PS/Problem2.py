# Write a Python program to convert text to speech, here is a sample text:
# pyttsx3 is a text-to-speech conversion library in Python. It works offline and is compatible with both Python 2 and 3.

import pyttsx3  # # Importing the pyttsx3 module
engine = pyttsx3.init()  # object creation

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!""")
engine.runAndWait()
