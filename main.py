import base64

from colorama import Fore

print(Fore.LIGHTBLUE_EX, ''' 
___________        .___              __________        
\__    ___/___   __| _/____          \______   \___.__.
  |    | /  _ \ / __ |/  _ \   ______ |     ___<   |  |
  |    |(  <_> ) /_/ (  <_> ) /_____/ |    |    \___  |
  |____| \____/\____ |\____/          |____|    / ____|
                    \/                          \/     
''')

def Todo_Add(todo):
    # Encode message for .todo file
    todo_bytes = todo.encode('ascii')
    todo_base64 = base64.b64encode(todo_bytes)
    todo_message = todo_base64.decode('ascii')
    print(todo_message)