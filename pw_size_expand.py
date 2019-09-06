import random
'''
weak = "C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\password_files\\weak\\10-million-password-list-top-1000000.txt"

weak_list = []

with open(weak, 'r') as file:
    for line in file:
        if len(weak_list) <= 340000:
            weak_list.append(line.rstrip())
        else:
            break
    file.close()
    
new_weak = weak_list[40000:] # 300000 new words

random.shuffle(new_weak)

final_weak = []

for word in new_weak:
    final_weak.append(word + ",1")

with open("C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\weak_master_list.txt", 'a+') as file:
    for word in final_weak:
        file.write(word + "\n")
    file.close()
 '''   
    
    
strong = "C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\strong_master_list.txt"

strong_list = []

with open(strong, 'r') as file:
    for word in file:
        strong_list.append(word.rstrip())
    file.close()
    
new_strong = []

for word in strong_list:
    new_strong.append(word.strip(",0"))
    
# now the list should contain around 36000 strong passwords from the strong master list
# now you need to iterate through, duplicating them, shuffling the duplicate, adding to master list

final_strong = []

for word in new_strong:
    for x in range(4):
        str_var = list(word)
        random.shuffle(str_var)
        pw = ''.join(str_var)
        final_strong.append(pw + ",0")

with open(strong, 'a+') as file:
    for word in final_strong:
        strong_list.append(word)
        if len(strong_list) <= 338000:
            file.write(word + "\n")