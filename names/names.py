import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# original code runs in 10.983 secs
'''duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''

# First Pass at optimization
# use a list comprehension runs in 3.902
'''duplicates = [
    name_2 for name_1 in names_1 for name_2 in names_2 if name_1 == name_2]'''

# Even more optimized
# use 2 separate for loops runs in 0.013 secs in O(n) time
duplicates = []  # list that stores duplicates
names_dic = {}  # dictionary that holds names in names_1 as values to name keys

# for every name in names_1
# take each name and assign it as a value to the name key in names_dic
for name in names_1:
    names_dic[name] = 'name in name_1'

# for every name in names_2
for name in names_2:
    # if name can be found as a value in names_dic
    if name in names_dic:
        # append the name to the duplicates list
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
