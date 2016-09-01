#! /usr/bin/env python3
from judge import judge_your_string_list
from replace_chars import replace_problematic_characters

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"",
    "‘": "\'",
    "’": "\'"
}

if __name__ == "__main__":
    string_input = input("Paste your questionable string here: ")
    string_to_list = list(string_input)

    if not string_input:
        print("No ideas? Run this again and try this: “Riddled with smartquotes, this.”")
    elif judge_your_string_list(string_input, magical_character_conversion_dict) == True:
        fixed_string_list, problem_pointer_list = replace_problematic_characters(string_to_list, magical_character_conversion_dict)
        print("ftfy:", "".join(fixed_string_list))
        print("     ", "".join(problem_pointer_list))
    else:
        print("Looks great. Smooth sailing.")
