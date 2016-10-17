#! /usr/bin/env python3

class QuoteFixer:
    """In which we fix strings that might contain curly quotes"""
    CHARACTER_CONVERSION_DICT = {
        "“": "\"",
        "”": "\"",
        "‘": "\'",
        "’": "\'"
    }

    def __init__(self, string):
        self.input = list(string)

    def test_for_string_input(self):
        if not self.input:
            print("No ideas? Run this again and try this: “Riddled with smartquotes, this.”")

    def judge_your_string_list(self, string_list):
        for char in string_list:
            if self.CHARACTER_CONVERSION_DICT.get(char) != None:
                return True
            else:
                pass
            return False

    def replace_curly_quotes(self, string_list):
        fixed_string_list = []
        problem_pointer_list = []
        for char in string_list:
            if self.CHARACTER_CONVERSION_DICT.get(char) != None:
                swap_char = self.CHARACTER_CONVERSION_DICT[char]
                fixed_string_list.append(swap_char)
                problem_pointer_list.append("^")
            else:
                fixed_string_list.append(char)
                problem_pointer_list.append(" ")
        fixed_string = "".join(fixed_string_list)
        problem_pointers = "".join(problem_pointer_list)

        return (fixed_string, problem_pointers)
