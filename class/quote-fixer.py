#! /usr/bin/env python3
import quotes_class

string_input = input("Paste your questionable string here: ")
string_to_list = list(string_input) # Move this over too
# Stuff above could go into main function for better flow

quote_fixer = quotes_class.QuoteFixer(string_to_list)
# ^ Don't want the name to refer to what it is. quote-fixer.py, something like that. Also, the class should have the ability to deal with no submitted value (rather than having it so far below).

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
  fix_string_and_make_terminal_output() # This could also take the string I want to fix. And the class object creation could go within name/main as well.

# Look at the regular expression class. Make object, then apply
# to many strings. Try that pattern so that a billion objects don't
# need to be made.
# Also revisit names in general.
