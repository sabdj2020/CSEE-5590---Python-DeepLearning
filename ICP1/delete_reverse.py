# enter string as input from the user
inputString = input("please, enter the string in which you want to delete char and reverse: ")
# enter the number of characters to delete from the input string
charToDel = input("Enter the number of characters to be deleted : ")
# the number is in string, we need to cast this number into int
numOfChar = int(charToDel)
# display the string before operations
print("the input string before delete and reverse : " + inputString)
# delete first characters
inputString = inputString[numOfChar:]
print("the input string before reverse: " + inputString)
# reverse operation
inputString = inputString[::-1]
print("string after reverse : " + inputString)