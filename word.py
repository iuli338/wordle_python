import json
import random

class Word:
    TARGET_WORD = ""
    WORDS = None
    HINT_INDEX = 0

    def SelectTargetWord():
        with open("cuvinte.json", "r", encoding="utf-8") as f:
            Word.WORDS = json.load(f)
        Word.TARGET_WORD = random.choice(Word.WORDS).upper()
        Word.HINT_INDEX = random.choice([0,1,2,3,4])
        # Debug
        # print(Word.WORDS)

    def ChangeTargetWord():
        Word.TARGET_WORD = random.choice(Word.WORDS).upper()
        Word.HINT_INDEX = random.choice([0,1,2,3,4])