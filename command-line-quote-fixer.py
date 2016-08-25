import sys

print(sys.argv)
string_input = sys.argv[1]
print("You entered", string_input)

def unfuck_your_string (str):
    global string_judgment
    string_judgment = None
    if "“" in str:
        string_judgment = True
    elif "”" in str:
        string_judgment = True
    elif "‘" in str:
        string_judgment = True
    elif "’" in str:
        string_judgment = True
    else:
        string_judgment = False



unfuck_your_string(string_input)
print(string_judgment)
