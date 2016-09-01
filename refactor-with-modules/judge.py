#! /usr/bin/env python3

def judge_your_string_list(string_list, character_dict):
    for char in string_list:
        if character_dict.get(char) != None:
            return True
        else:
            pass
        return False
