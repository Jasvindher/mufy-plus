#TODO
#Create a function called check_string that takes a string argument
#If the string starts with the letters "The", it should return "Found it!"
def check_string(s):
    if s.startswith("The"):
        return "Found it!"
    else:
        return "Nope"
#Test case
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'
print(check_string(str1))  # Output: Found it!
print(check_string(str2))  # Output: Nope
print(check_string(str3))  # Output: Found it!