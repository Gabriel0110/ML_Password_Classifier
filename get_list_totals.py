weak = "weak_master_list.txt"
strong = "strong_master_list.txt"

total = 0

with open(weak, 'r') as file:
    for line in file:
        total += 1
    file.close()

print("Total weak: ", total)

total = 0

with open(strong, 'r') as file:
    for line in file:
        total += 1
    file.close()

print("Total strong: ", total)
