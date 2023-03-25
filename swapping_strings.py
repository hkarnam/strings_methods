# swapping two words of a string
input_str = 'peter piper picked a peck of pickled peppers.'
word_split = input_str.split()  # splitting a string returns output in string class
output = [] # initializing empty string to get new list with swapped elements
#print(word_split)
str1 = 'peter'
str2 = 'peppers.'
for x in word_split:  # iteration over the list
    if x == str1:
        x = str2
        output.append(x)
    elif x == str2:
        x = str1
        output.append(x)
    else:
        output.append(x)
#print(output)
new_str = " ".join(output)  # using join method to get a string with spaces
print(new_str)