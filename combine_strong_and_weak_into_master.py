import random

weak = "C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\weak_master_list.txt"
strong = "C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\strong_master_list.txt"
master = "C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\master_pw_list.txt"

strong_list = []
weak_list = []

with open(strong, 'r') as file:
    for word in file:
        strong_list.append(word.rstrip())
    file.close()
    
with open(weak, 'r') as file:
    for word in file:
        weak_list.append(word.rstrip())
    file.close()
    
master_list = []
for word in strong_list:
    master_list.append(word)

for word in weak_list:
    master_list.append(word)
    
random.shuffle(master_list)
random.shuffle(master_list)
    
with open(master, 'w') as file:
    for word in master_list:
        file.write(word + "\n")
    file.close()
    
print("done")