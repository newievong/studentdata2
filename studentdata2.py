allinfo = [
  {"name": "Joseph", "hometown": "Sterling Heights", "fav_food": "fried chicken"},
  {"name": "Newie", "hometown": "Grand Prairie", "fav_food": "noodles"},
  {"name": "Anna", "hometown": "Shelby Township", "fav_food": "shrimp fried rice"},
  {"name": "Mason", "hometown": "Arlington", "fav_food": "papaya salad"},
]
def list_names(students):
    for peoplenum in range(len(students)):
        name = students[peoplenum]['name']
        print(f"{peoplenum + 1}. {name}")
option = input("Please select which action you'd like to do: add, view, or quit: ")

while option != 'add' and option != 'view' and option != 'quit':
    option = input("This is an invalid input. Please try again by typing in: add, view, or quit:  ")

if option == 'view':
    list_names(allinfo)
    choice = int(input(f"Which student would you like to learn more about? Enter a number between 1-{len(allinfo)}: "))


    while choice > len(allinfo) or choice < 1:
        choice = int(input("This is an invalid number. Please try again by entering a number between 1-4: "))
    else:
        selectstud = allinfo[choice - 1]
        print(f"Student {choice} is {selectstud['name']}. What would you like to know?")
        choice2 = input("Enter 'hometown' or 'favorite food': ")

        while choice2 != 'hometown' and choice2 != 'favorite food':
            choice2 = input("This is an invalid input. Please enter 'hometown' or 'favorite food: ")

        if choice2 == 'hometown':
            print(f"{selectstud['name']}'s hometown is {selectstud['hometown']}.")


        elif choice2 == 'favorite food':
            print(f"{selectstud['name']}'s favorite food is {selectstud['fav_food']}.")


if option == 'add':
    def get_new_student():
        newinfo = {}
        newinfo['name'] = input("Please input a name for the new student: ")
        newinfo['hometown'] = input("Next please input their hometown: ")
        newinfo['fav_food'] = input("Last, please input their favorite food: ")
        return newinfo

    allinfo.append(get_new_student())


elif option == 'quit':
  print("Goodbye!")