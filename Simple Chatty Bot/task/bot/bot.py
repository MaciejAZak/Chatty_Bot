# write your code here
bot_name = "Zhab00n"
birth_year = 2020
print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
print("Please, remind me your name")

user_name = input()
print("What a great name you have, {0}.".format(user_name))
print("Let me guess your age")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is {0}: that's a good time to start programming!".format(user_age))
print("Your age is {0}: that's a good time to start programming!".format(user_age))
print("Now I will prove to you that I can count to any number you want.")

number = int(input())
i=0
while i <= number:
    print(str(i) + " !")
    i += 1

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

answer = int(input())

while True:
    if answer != 2:
        print("Please, try again.")
        answer = int(input())
    else:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
