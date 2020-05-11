
#Any vowel in the input phrase gets converted to letter g using the following function:

def translator_vowel_to_g(phrase):
    translated_phrase = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.islower():
                translated_phrase = translated_phrase + 'g'
            else:
                translated_phrase = translated_phrase + 'G'
        else:
            translated_phrase = translated_phrase + letter
    return translated_phrase

print(translator_vowel_to_g(input("Enter The Phrase: ")))
cnt = input("Do you want to continue?(Yes/No): ")

while cnt=="Yes" :
    print(translator_vowel_to_g(input("Enter The Phrase: ")))
    cnt = input("Do you want to continue?(Yes/No): ")

print("Thank you for using the translator!")
