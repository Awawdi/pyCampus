def translate(sentence):
    result = ""
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen = (w for w in sentence.split())
    for i in gen:
        result += words[i] + " "
    return result


print(translate("el gato esta en la casa"))
