import random

words = [ "viens", "divi", "tris", "cits" ]

while True:
    word = random.choice(words)
    guessedWord = list("_" for _ in word)
    lives = 5
    print(word)

    while lives > 0 and "".join(guessedWord) != word:
        inp = input("Burts: ")
        if inp == "":
            continue
        inp = inp[0]

        guessed = False
        for i in range(0, len(word)):
            if inp == word[i]:
                guessedWord[i] = inp
                guessed = True

        if not guessed:
            lives -= 1

        print(f"Dzīvības: {lives}")
        print(guessedWord)

    if lives > 0:
        print("Uzvarējām")
    else:
        print("Zaudējām")

    if input("Vai sākt jaunu spēli? y/n").lower() != "y":
        break