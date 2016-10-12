#! /usr/bin/env python3

class QuoteFixing:
    """In which we fix strings that might contain curly quotes"""

    def __init__(self, string):
        self.input = string
        self.CHARACTER_CONVERSION_DICT = {
            "“": "\"",
            "”": "\"",
            "‘": "\'",
            "’": "\'"
        }

    def judge_your_string_list(self, string_list, character_dict):
        for char in string_list:
            if character_dict.get(char) != None:
                return True
            else:
                pass
            return False

    def replace_problematic_characters(self, string_list, character_dict):
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
