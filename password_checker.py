import re

"""
 a program to check the validity of password input by users.
Following are the criteria for checking the password: 
1. At least 1 letter between [a-z] 
2. At least 1 number between [0-9] 
3. At least 1 letter between [A-Z] 
4. At least 1 character from [$#@_&%] 
5. Minimum length of transaction password: 6 
6. Maximum length of transaction password: 12

"""

def reg_check(pattern, s):
    matched = re.search(pattern, s)
    is_match = bool(matched)
    return is_match


def password_checker(input):
    has_lowercase = False
    has_uppercase = False
    has_number = False
    has_specialchar = False
    has_correctlen = False

    #Minimum length of transaction password: 6  and #Maximum length of transaction password: 12
    if len(input) >= 6 and len(input) <= 12:
        has_correctlen = True
    #At least 1 letter between [a-z]     
    if reg_check("[a-z]",input):
        has_lowercase = True
    #At least 1 number between [0-9]     
    if reg_check("[0-9]", input):
        has_number = True    
    if reg_check("[A-Z]", input):
        has_uppercase = True
    if reg_check("[$#@_&%]",input):
        has_specialchar = True


    return has_correctlen and has_lowercase and has_number and has_specialchar and has_uppercase
    
    
    #At least 1 number between [0-9] 
    #At least 1 letter between [A-Z] 
    #At least 1 character from [$#@_&%] 


text = "p@ssworD1"

print(password_checker(text))