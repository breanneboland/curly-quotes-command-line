#! /usr/bin/env python3
import argparse

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"",
    "‘": "\'",
    "’": "\'"
}

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

def fix_string_and_make_terminal_output():
    if not string_input:
        print("No ideas? Run this again and try this: \
            “Riddled with smartquotes, this.”")
    elif judge_your_string(string_input) == True:
        fix_your_string(string_to_list)
        print("ftfy:", "".join(fixed_string_list))
        print("     ", "".join(problem_pointer_list))
    else:
        print("Looks great. Smooth sailing.")

if __name__ == "__main__":
    # Adding command line help/utility
    parser = argparse.ArgumentParser(description=
        'Finds curly quotes and replaces them with straight quotes.')
    parser.add_argument('words', metavar='string', type=str, nargs='+',
        help='the string to be examined and fixed')

    # Just turning the Namespace object into the string it once was
    args = parser.parse_args()
    input_list = args.words
    string_input = " ".join(input_list)

    # Changes string_input into lovely mutable list
    string_to_list = list(string_input)

    # Empty lists to concatenate into terminal output strings later
    fixed_string_list = []
    problem_pointer_list = []
    fix_string_and_make_terminal_output()
