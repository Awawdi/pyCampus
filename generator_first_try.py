def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_sentence = ""
    original_sentence = list(sentence.split())

    gen = ((words[key] for key in words))

    for i in original_sentence:
        translated_sentence += words[i] + " "

    return translated_sentence


print(translate("el gato esta en la casa"))
