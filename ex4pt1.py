#Ask the user to enter a number. Use an if statement to print "that's a big number!" 
# if the number is 100 or more, or "why not dream a little bigger?" otherwise.

print("Hello user, please enter a number")
user_num = int(input())

if user_num >= 100:
    print("Wow! That's a Big Number!")
else:
    print("Why not dream bigger?")