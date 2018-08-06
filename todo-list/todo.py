import sys
import todo_helper

# the todo_helper.get() function gets you a list of strings that represent all
# of the todo items
todos = todo_helper.get()

# the todo_helper.save(todos_list) function saves the given list of strings as
# the todo list. It will overwrite the existing list with the one you give it
todo_helper.save(todos)

# the todo_helper.get_ch() function will wait for the user to press a single
# key and will return with the key the user pressed. This is handy for asking
# the user to provide a 'q' to quit, etc.
def menu():
    menu_list = """
    l: todos_list
    a: add item
    d: delete
    q: quit"""
    user_input = input("What would you like to do?")
    return user_input

user_choice = menu()
while (user_choice != "q"):
    print menu_list
    user_choice = todo_helper.get_ch()

    if user_choice =="l":
        for index, item in enumerate(my_list):
            print index, item
        user_choice = menu()

    elif (user_choice == "a"):
        print("What would you like to add?")
        todos.append(my_list())
        todo_helper.save(todos)
        user_choice = menu()

    elif(user_choice == "d"):
        print("What would you like to remove?")
        todos.pop(my_list())
        todo.helper.save(todos)

        break
# Question:
# Do I need to make my_list?

#print("press any key to quit...")
#response = todo_helper.get_ch()
