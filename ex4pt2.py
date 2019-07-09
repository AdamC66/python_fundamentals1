#Ask the user to enter their age, and then display a message telling them how many years apart in age you are from them. 
#If they enter a number larger than 105, print "I'm not sure I believe you".

my_age = 25
print("Hello user, please enter your age")
user_age = int(input())

age_diff = abs(my_age-user_age)

if user_age > 105:
    print("I'm not sure I believe you")
else:
    print("The absolute difference between our ages is {}".format(age_diff))