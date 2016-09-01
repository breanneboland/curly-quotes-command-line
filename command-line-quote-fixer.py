#! /usr/bin/env python3

fixed_string_list = []
problem_pointer_list = []

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"",
    "‘": "\'",
    "’": "\'"
}

def judge_your_string_list(string_list, character_dict):
    for char in string_list:
        if character_dict.get(char) != None:
            return True
        else:
            pass
        return False

def replace_problematic_characters(string_list, character_dict):
    for char in string_list:
        if character_dict.get(char) != None:
            swap_char = character_dict[char]
            fixed_string_list.append(swap_char)
            problem_pointer_list.append("^")
        else:
            fixed_string_list.append(char)
            problem_pointer_list.append(" ")

if __name__ == "__main__":
    string_input = input("Paste your questionable string here: ")
    string_to_list = list(string_input)

    if not string_input:
        print("No ideas? Run this again and try this: “Riddled with smartquotes, this.”")
    elif judge_your_string_list(string_input, magical_character_conversion_dict) == True:
        replace_problematic_characters(string_to_list, magical_character_conversion_dict)
        print("ftfy:", "".join(fixed_string_list))
        print("     ", "".join(problem_pointer_list))
    else:
        print("Looks great. Smooth sailing.")
