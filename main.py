import numpy as np
path_to_file="books/frankenstein.txt"
with open(path_to_file) as f:
    file_contents = f.read()
words = file_contents.split()
char_dictionary={
    "a":0
}
for word in words:
    for char in word:
        if(char.isalpha()):
            char=char.lower()
            if(char in char_dictionary):
                char_dictionary[char]+=1
            else:
                char_dictionary[char] = 1
#dictionary to array
result = char_dictionary.items()
data = list(result)
char_Array = np.array(data)
###################

char_Array =(sorted(char_Array, key=lambda x: int(x[1]),reverse=True))

for char in char_Array:
    print(f"{char[0]}The '{char[0]}' character was found {char[1]} times")
print("--- End report ---")

