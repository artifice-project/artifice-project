from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.WHITE + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# go thru each line of the string body
# if line ends with NEW_LINE, insert a '*' character at the end of the line
#




from colorama import init
from termcolor import colored

init()

print(colored('Hello, World!', 'green', 'on_red'))
