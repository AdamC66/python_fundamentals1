#Save your name as a string into a variable, then ask the user to enter their name. 
#If the two names match, print "We have the same name!".

my_name = "adam" #stored as lowercase intentionally
print("Hello user, please enter your name!")
user_name = input().lower() #stores user_name as lowercase string

if my_name == user_name:
    print("Wow! We have the same name")
else:
    print("ok, we do not have the same name")
