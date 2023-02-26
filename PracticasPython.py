# you can find all python function here: https://docs.python.org/3/library/functions.html
#if you want to look for print funtion you can modify the url: 
# https://docs.python.org/3/library/functions.html#print

print ('Hello World!')
str = input("what is your name? ")
print("hello",str) #you can use the (,) coma mark to add variables
print("this is a nice day " + str + " doesnt it?" ) #you can use the. (+) sign to put variables

"""
print structure
print(*objects, sep=' ', end='\n', file=None, flush=False)
"""
#end ='/n' means that automatic after finish the print goes to tne nesxt line
#sep =' ' meand and space will separate the words, you can change too
#. if we se ttne end with "" , will remain in the same line
lastNmae = input("what is your last name ? ")
print("so, your first name is " + str , end ="")
print(" and your last name is:", lastNmae)
#if you put an "F" in print you can you {} with variable too

print(f"your full name is: {str} {lastNmae}")
#to remove space from striing
str= str.strip()
print(str.capitalize()) #to capitalized the first letter of first word
print(str.title()) #to capitalized the letter of evry wrord
print(str.strip().title()) # remove spaces and Capitalized first letters
#se puede hacer todo eso desde la variable 
all = input("what is your First and last Nme ? ").strip().title()
print(all)
first, last = all.split(" ")
print(f"your first name is: {first}")
#note: terminal works as an interactive mode example if you type 2+4 will answer 6print("hello world")
Name = input("What is your name? ")
Print("Hola "+ Name)
