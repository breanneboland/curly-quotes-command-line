import argparse
import sys

fixed_string_list = []
problem_pointer_list = []

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"",
    "‘": "\'",
    "’": "\'"
}

# Get arguments, if any, from the command line
# command_line_string = sys.argv[1]

# Adding command line help/utility
parser = argparse.ArgumentParser(description='Finds curly quotes and replaces them with straight quotes.')
parser.add_argument('string', metavar='S', type=str, nargs='+', help='the string to be examined and fixed')

args = parser.parse_args()
print(args.accumulate(args.string))

def judge_your_string(string_list):
    string_judgment = None
    for char in string_to_list:
        if char in magical_character_conversion_dict.keys():
            return True
        else:
            pass
    return False

def fix_your_string(string_list):
    for char in string_list:
        if char in magical_character_conversion_dict.keys():
            swap_char = magical_character_conversion_dict[char]
            fixed_string_list.append(swap_char)
            problem_pointer_list.append("^")
        else:
            fixed_string_list.append(char)
            problem_pointer_list.append(" ")

if __name__ == "__main__":
    # if command_line_string:
    #     print(command_line_string)
    string_input = input("Paste your questionable string here: ")
    string_to_list = list(string_input)

    if not string_input:
        print("No ideas? Run this again and try this: “Riddled with smartquotes, this.”")
    elif judge_your_string(string_input) == True:
        fix_your_string(string_to_list)
        print("ftfy:", "".join(fixed_string_list))
        print("     ", "".join(problem_pointer_list))
    else:
        print("Looks great. Smooth sailing.")
