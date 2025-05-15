def Vowel():
    letter = input("Enter a letter: ").lower()
    vowels = "aeiou"
    if letter in vowels:
        print("Vowel")
    else:
        print("Consonant")
Vowel()