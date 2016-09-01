#! /usr/bin/env python3

def replace_problematic_characters(string_list, character_dict):
    fixed_string_list = []
    problem_pointer_list = []
    for char in string_list:
        if character_dict.get(char) != None:
            swap_char = character_dict[char]
            fixed_string_list.append(swap_char)
            problem_pointer_list.append("^")
        else:
            fixed_string_list.append(char)
            problem_pointer_list.append(" ")
    return (fixed_string_list, problem_pointer_list)
