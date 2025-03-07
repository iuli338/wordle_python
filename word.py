import json
import random

class Word:
    TARGET_WORD = ""
    WORDS = None

    def SelectTargetWord():
        with open("cuvinte.json", "r", encoding="utf-8") as f:
            Word.WORDS = json.load(f)
        Word.TARGET_WORD = random.choice(Word.WORDS).upper()
        # Debug
        # print(Word.WORDS)
        print(Word.TARGET_WORD)