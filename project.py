import random
import os

#fumtion start

def r_key(d, name):
    random_word = random.choice(list(d.keys()))
    # print(random_word)
    # for i in random_word :
    #     print(" _ ",end=" ")
    print("_ " * len(random_word))
    chance = 7
    list_of_ltters = []
    word_completed = False
    while chance > 0:
        letter = input("enter a letter :") 
        if letter.isalpha() == False or len(letter) > 1:
            print("enter only one letter")
            continue
        elif letter in list_of_ltters:
            print("letter already entered")
            continue
        else :
            if letter in random_word:
                list_of_ltters.append(letter)
                word_completed = True
                for char in random_word:
                    if char in list_of_ltters :
                        print(char,end="")
                    else :
                        word_completed = False
                        print("_ ",end="")
                print()         
                if word_completed :
                    print(f'{name} - won - word : {random_word}')
                    # return random_word 
                    break
                print()    
                print()                 
            else :
                chance -= 1
                print(f'letter {letter} does not exists')
                print()
                print()
                print("chances left ",chance)
                if chance == 0:
                    print(f'{name} - loss - word : {random_word}')
                    # return random_word       
    os.makedirs("D:\\Muniba Work\\Week 2\\Final Project", exist_ok=True)
    with open("D:\Muniba Work\Week 2\Final Project\games_result.txt", "a") as result:
        if word_completed :
            result.write(f'{name}-won-word : {random_word}\n')
        else:
            result.write(f'{name}-loss-word : {random_word}\n')
    return random_word

#function end
# Load dictionary from file
dictionary_path = "D:\\Muniba Work\\Week 2\\Final Project\\dictionary.txt"
os.makedirs("D:\\Muniba Work\\Week 2\\Final Project", exist_ok=True)
words_dict = {}
with open(dictionary_path, "r") as d:
    for line in d: 
        # print("Dictionary in txt is ")
        # print(line)
        words = line.strip().split(",")
        for word in words:
            if ":" not in word:
                continue  # 🔁 Skip malformed or empty parts
            w = word.split(":")
            if len(w) != 2:
                continue  # 🔁 Skip malformed entries
            key = w[0].replace('"', '').strip()
            value = int(w[1])
            words_dict[key] = value
name = input("Enter your name : ").strip()
game_played = False
# for choice in name :
while True:    
    choice = input("Choose Play | Exit: ").lower()
    if choice == 'play':
        random_word = r_key(words_dict, name)
        words_dict[random_word] += 1
        game_played = True
    elif choice == 'exit':
        if game_played:
            # Save updated dictionary
            with open(dictionary_path, "w") as d:
                items = [f'"{k}": {v}' for k, v in words_dict.items()]
                d.write(", ".join(items))
            print("Dictionary updated and saved.")
        else:
            print("No game played. Exiting without changes.")
        break
    else:
        print("Invalid option. Please type Play or Exit.")
