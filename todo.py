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
print("press any key to quit...")
response = todo_helper.get_ch()
