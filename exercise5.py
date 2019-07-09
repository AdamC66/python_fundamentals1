#Ask the user for input on what action to take - walk or run. 
# If they walk, the total distance should go up by one, and you should update the user on their total distance traveled as follows:
#"Distance from home is 6 km."
#If they run, their total distance should go up by 5. Your program should keep asking for input - 
# you don't know where you're going until you get there! Each time, you should print the total distance traveled.

#6.1
#Allow the user to go home when they are done exercising.
#The program should stop asking for input if the user enters 'go home'.

#See if you can also make the program tell the user when they have entered a command that does not exist.

#Exercise 6.2
#You started the day with energy, but you are going to get tired as you travel! Keep track of your energy.

#If you walk, your energy should increase. If you run, it should decrease. Moreover, you should not be able to run if your energy is zero.

#...then, go crazy with it! Allow the user to rest and eat. Do whatever you think might be interesting.

class Person:
    def __init__(self, name, energy, dist_from_home):
        self.name = name
        self.energy = energy
        self.dist_from_home = dist_from_home

def walk():
    #in order to be truly DRY, I think I should have written a function to check energy, that accepts the action.... but w/e this works
    if user.energy != 0:
        user.energy-=1
        user.dist_from_home += 1
        print("\n{}, you are {}km from home, you have {} energy remaining\n".format(user.name, user.dist_from_home, user.energy))
    else:
        print("\nYou dont have the energy to do that right now, you should try eating\n")
    
def run():
    #in order to be truly DRY, I think I should have written a function to check energy, that accepts the action.... but w/e this works
    if user.energy >= 2:
        user.energy-=2
        user.dist_from_home += 5
        print("\n{}, you are {}km from home, you have {} energy remaining\n".format(user.name, user.dist_from_home, user.energy))
    else:
        print("\nYou dont have the energy to do that right now, you should try eating\ngo")

def eat():
    user.energy+=2
    print("\n{}, you are {}km from home, you have {} energy remaining\n".format(user.name, user.dist_from_home, user.energy))

def go_home():
    
    print("\nYou have decided to return home, in total you travelled {}km\n".format(user.dist_from_home))

user = Person("name", 5, 0)
print("Hello User, please enter your name:")
exercise = True
user.name = input()

print("Hello {}, Lets do some exercise, please enter \"walk\", \"run\", or \"eat\"".format(user.name))
print("When you are done, you can enter \"go home\" to automatically return home")

while exercise == True:
    print("What would you like to do?")
    action = input().lower()
    
    if action == "walk":
        walk()
    elif action == "run":
        run()
    elif action == "eat":
        eat()
    elif action == "go home":
        go_home()
        exercise = False
    else:
        print("You have entered an invalid command, please try again")
    


