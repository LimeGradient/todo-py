import base64

from colorama import Fore

# Cool looking logo
print(Fore.LIGHTBLUE_EX, ''' 
___________        .___              __________        
\__    ___/___   __| _/____          \______   \___.__.
  |    | /  _ \ / __ |/  _ \   ______ |     ___<   |  |
  |    |(  <_> ) /_/ (  <_> ) /_____/ |    |    \___  |
  |____| \____/\____ |\____/          |____|    / ____|
                    \/                          \/     
''')

commands = [
  ".exit",
  ".read"
]

def Todo_Add(todo):
    # Encode message for .todo file
    todo_bytes = todo.encode('ascii')
    todo_base64 = base64.b64encode(todo_bytes)
    todo_message = todo_base64.decode('ascii')
    
print(Fore.WHITE)
print("How would you like your Todo list to be saved?")
print("[1] Local Storage")
print("[2] Online Storage")
mode = input("Saving Mode: ")

if mode == "1":
  while True:
    todo = input("Todo: ")
    if todo in commands:
      print(todo)
    else:
      Todo_Add(todo)