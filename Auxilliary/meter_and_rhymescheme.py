import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import cmudict

# Load CMU Pronouncing Dictionary
d = cmudict.dict()

def syllable_count(word):
    """Count the number of syllables in a word."""
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

def get_meter_and_rhyme_scheme(lyrics):
    """Get the meter and rhyme scheme from a set of lyrics."""
    translator = str.maketrans('', '', string.punctuation)
    lyrics = lyrics.translate(translator)
    words = word_tokenize(lyrics)
    meter = []
    last_word_syllables = None
    rhyme_scheme = []

    for word in words:
        if word.lower() in d:
            syllables = syllable_count(word)
            if last_word_syllables is not None:
                if syllables == last_word_syllables:
                    meter.append("S")
                else:
                    meter.append("W")
            last_word_syllables = syllables

    # Determine Rhyme Scheme
    last_word = None
    last_word_rhyme = None
    for word in words[::-1]:
        if word.lower() in d:
            pronunciation = d[word.lower()][0]
            if pronunciation not in rhyme_scheme:
                if last_word_rhyme is not None:
                    rhyme_scheme.append(last_word_rhyme)
                last_word_rhyme = pronunciation[-2:]
        last_word = word

    # Account for possible leftover rhyme
    if last_word_rhyme is not None and last_word_rhyme not in rhyme_scheme:
        rhyme_scheme.append(last_word_rhyme)

    return "".join(meter), rhyme_scheme

# Example lyrics
lyrics = """
In fields of gold, we dance and play
Underneath the sun's warm embrace
With hearts entwined, we'll find our way
Together now, in this endless chase

Love's adventure, a journey bright
Hand in hand, through day and night
With every step, our spirits ignite
In love's embrace, our souls take flight
"""

meter, rhyme_scheme = get_meter_and_rhyme_scheme(lyrics)
print("Meter:", meter)
print("Rhyme Scheme:", rhyme_scheme)
