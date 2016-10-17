#! /usr/bin/env python3
import quote_fixer

def fix_string_and_make_terminal_output(str):
    if quoteFixer.judge_your_string_list(str) == True:
        fixed_string, problem_pointers = quoteFixer.replace_curly_quotes(listed_string_to_fix)
        print("ftfy:", fixed_string)
        print("     ", problem_pointers)
    else:
        if str:
            print("Looks great. Smooth sailing.")


if __name__ == "__main__":
    string_input = input("Paste your questionable string here: ")
    quoteFixer = quote_fixer.QuoteFixer(string_input)
    quoteFixer.test_for_string_input()
    listed_string_to_fix = quoteFixer.input
    fix_string_and_make_terminal_output(listed_string_to_fix)
