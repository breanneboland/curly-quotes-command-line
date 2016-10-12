#! /usr/bin/env python3
import quotes_class

string_input = input("Paste your questionable string here: ")
string_to_list = list(string_input)

quote_fixer = quotes_class.QuoteFixer(string_to_list)

def fix_string_and_make_terminal_output():
    listed_string_to_fix = quote_fixer.input
    char_conversion_dict = quote_fixer.CHARACTER_CONVERSION_DICT

    if not listed_string_to_fix:
        print("No ideas? Run this again and try this: “Riddled with smartquotes, this.”")
    elif quote_fixer.judge_your_string_list(listed_string_to_fix, char_conversion_dict) == True:
      fixed_string, problem_pointers = quote_fixer.replace_problematic_characters(listed_string_to_fix, char_conversion_dict)
      print("ftfy:", fixed_string)
      print("     ", problem_pointers)
    else:
        print("Looks great. Smooth sailing.")

if __name__ == "__main__":
    fix_string_and_make_terminal_output()
