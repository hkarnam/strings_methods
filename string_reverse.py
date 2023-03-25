
# A python program to reverse every word of a string
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'

input_str = 'peter piper picked a peck of pickled peppers.'
word_split = input_str.split()

new_list = [word[::-1] for word in word_split] # using list comprehension
result = " ".join(new_list)
print(result)