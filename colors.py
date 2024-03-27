
from colorama import  Back, Style

# Define color escape sequences
def black(text):
    return f"\033[1;30m{text}\033[0m"

def red(text):
    return f"\033[1;31m{text}\033[0m"

def green(text):
    return f"\033[1;32m{text}\033[0m"

def yellow(text):
    return f"\033[1;33m{text}\033[0m"

def blue(text):
    return f"\033[1;34m{text}\033[0m"

def magenta(text):
    return f"\033[1;35m{text}\033[0m"

def cyan(text):
    return f"\033[1;36m{text}\033[0m"

def white(text):
    return f"\033[1;37m{text}\033[0m"

# Test the color functions
# colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
# text = "Hello, colored text!"
#
# for color_name in colors:
#     color_function = globals()[color_name]
#     print(color_function(text))

# # print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
# print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
# print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
# print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
# print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
# print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
# print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
#
#
# print("----------------------")
# print("\033[0m 1;30;40m what \033[0m 0;37;41m")

