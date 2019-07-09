#how would you calculate a good tip for a 55 dollar meal?
meal_price = 55
tip = meal_price*0.15
total_price = meal_price + tip
print("For a meal price of ${}, a 15% tip would be ${},\nFor a total of ${}.".format(meal_price, tip, total_price))

# Try adding a string and an int with the + operator, what happens.
# find a way to convert the int to a sftring first and use print to print the result
print('\n\n')

num1 = 12
string1 = "14"

#print(num1 + string1)
#This returns:
#Traceback (most recent call last):
# File "exercise2.py", line 14, in <module>
 #   print(num1 + string1)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#So we cant use the + operator on an int and a str they both need to be the same type

print(int(string1)+num1)
#OR
print(str(num1)+string1)
print('\n\n')


#Try Try outputting the result of 45628 multiplied by 7839 in a sentence by using string interpolation.
print("the result of 45628 multiplied by 7839 is: {}".format(45628*7839))

print('\n\n')

#What's the value of the expression (10 < 20 and 30 < 20) or not(10 == 11)? Try figuring it out on your own before typing it in
#(True AND False) or !(False) => (False) or (True) => True

result = (10 < 20 and 30 < 20) or not(10 == 11)
print(result)

print('\n\n')

name = "Sandra"
greeting = "Hello {}! It's good to see you again.".format(name)
mission = "Your mission, should you choose to accept it..."

print("{} {}".format(greeting, mission))
