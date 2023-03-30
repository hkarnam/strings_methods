# converting the first letter of every word in a string to upper case if first letter is capital
# otherwise just convert the first letter to capital and print it

str1 = str(input("enter a string: "))
if str1[0].islower():  # checking if the lower case is already lower
    str2 = str1.capitalize()   # if not capitalizing it
    print(str2)

elif str1[0].isupper():
    str2 = str1.title()  # istititle converts all the first letters of words in string to capital

    print(str2)