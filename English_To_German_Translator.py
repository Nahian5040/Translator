from translate import Translator
print("You can type Q anytime to exit the programme")
while True:
    sentence = input("Write down the sentence you wanted to translate in german:")
    if sentence == "Q":
        break
    else:
        s = Translator(from_lang = "English" , to_lang = "German")
        translation = s.translate(sentence)
        print(translation)