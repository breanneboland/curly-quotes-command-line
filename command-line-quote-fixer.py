fixed_string_list = []
problem_pointer_list = []

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

if __name__ == "__main__":
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
