"""
adapter pattern provides interface between two incompatible interfaces or objects
Real life example is card reader which provides an adapter between the momory card
and the laptop. It helps two classes work together. Usually preferred during systems
integration. Example, english and french speaker cannot talk to each other without a translator
"""

class EnglishSpeaker(object):
    def __init__(self, message):
        self.message = message

    def speak(self):
        return self.message


class FrenchSpeaker(object):
    def __init__(self, message):
        self.message = message

    def speak(self):
        return self.message

class Adapter(object):
    def __init__(self, message):
        self.mapping = {"hello": "bonjour"}
        self.message = message

    def eng_to_french(self):
        if self.message in self.mapping:
            return self.mapping[self.message]

obj = EnglishSpeaker("hello")
english_message = obj.speak()

obj = Adapter(english_message)
translated_message = obj.eng_to_french()

obj = EnglishSpeaker("bonjour")
french_message = obj.speak()

assert french_message == translated_message