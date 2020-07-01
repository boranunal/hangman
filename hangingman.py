import random

file = "word.txt"
words = open(file).read().splitlines()

print("*****type '!hint' get hint*****")
while 1:
    t = random.randint(0,len(words)-1)
    word = words[t]
    list_word = []
    for n in word:
        list_word.append(n)
    tries=10
    guesses=''
    hint_left = 1

    while tries > 0:
        dashes=0
        for char in word:
            if char in guesses:
                for n in list_word:
                    if char == n:
                        list_word.remove(char)
                print(char,end='')
            else:
                print('-',end='')
                dashes +=1
        print()
        if dashes==0:
            print('Congratulations!!')
            break
        guess = input('Enter your guess:')
        while guess == "!hint" or guess == "!h":
            if hint_left > 0:
                guess = random.choice(list_word)
                hint_left-=1
            else:
                print("you don't have any hint left")
                guess = input("Enter your guess:")
        while guess in guesses:
            print("You already guessed",guess)
            guess = input("Enter your guess:")
        guesses += guess
        tries -= 1
        if tries == 0:
            print("Sorry you lose! The word was",word)
            break
    cond = input("*****type '!exit' to exit game*****\n*****press enter to continoue*****")
    if cond == "!exit" or cond =="!quit" or cond =="!q":
        break
