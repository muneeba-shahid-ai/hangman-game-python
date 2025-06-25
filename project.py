import random
import os

#fumtion start

def r_key(d):
    random_word = random.choice(list(d.keys()))
    # print(random_word)
    # for i in random_word :
    #     print(" _ ",end=" ")
    print("_ " * len(random_word))
    chance = 7
    list_of_ltters = []
    while chance > 0:
        letter = input("enter a letter :") 
        if letter.isalpha() == False or len(letter) > 1:
            print("enter only one letter")
            continue
        elif letter in list_of_ltters:
            print("letter already entered")
            continue
        else :
            find_letter = random_word.find(letter)
            # print(find_letter)
            if find_letter >= 0 :
                list_of_ltters.append(letter)
                word_completed = True
                for char in random_word:
                    if char in list_of_ltters :
                        print(char,end=" ")
                    else :
                        word_completed = False
                        print("_ ",end="")
                print()         
                if word_completed :
                    print(f'{name}-won-word : {random_word}')
                    return random_word 
                print()    
                print()                 
            else :
                chance -= 1
                print(f'letter {letter} does not exists')
                print()
                print()
                print("chances left ",chance)
                if chance == 0:
                    print(f'{name}-loss-word : {random_word}')
    os.makedirs("D:\\Muniba Work\\Week 2\\Final Project", exist_ok=True)
    with open("D:\Muniba Work\Week 2\Final Project\games_result.txt","a") as result:
        if word_completed :
            result.write(f'{name}-won-word : {random_word}\n')
        else:
            result.write(f'{name}-loss-word : {random_word}\n')
            

#function end

os.makedirs("D:\\Muniba Work\\Week 2\\Final Project", exist_ok=True)
words_dict = {}
with open("D:\\Muniba Work\\Week 2\\Final Project\\dictionary.txt","r") as d:
    for line in d: 
        print("Dictionary in txt is ")
        # print(line)
        words = line.split(",")
        for word in words :
            w = word.split(" : ")
            key = w[0].strip('"')
            value = int(w[1]) 
            words_dict[key]=value
name = input("Enter your name : ")
# for choice in name :    
choice = ""
while choice != 'play' and choice != 'exit':   
    choice = input("choose Play | Exit ")
    
    if choice.lower() == 'play':
        # r_key(words_dict)
        random_word_was = r_key(words_dict)
        words_dict[random_word_was] += 1
        # print("Now dictionary is : ")
        # print(words_dict)
        text_dict = ''
        items = list(words_dict.items())
        # print(items)
        for idx,(k,v) in enumerate(items):
            text_dict += f'"{k}" : '+ str(v) 
            if idx != len(items) - 1:
                text_dict += ", "
                for word in text_dict:
                    k = k.strip('"')
        # print(text_dict)
        choice = "play_again"
        continue
    elif choice.lower() == 'exit':
        os.remove("dictionary.txt")
        os.makedirs("D:\\Muniba Work\\Week 2\\Final Project", exist_ok=True)
        with open("D:\\Muniba Work\\Week 2\\Final Project\\dictionary.txt","w") as d:
            d.write(text_dict)
        break
    else :
        print("No such typo accepted. Please choose again.")
        continue 
