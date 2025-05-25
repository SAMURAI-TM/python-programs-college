#to find any letter which is present in the string

def find_letter_in_string(string, letter):
    if letter in string:
        return f"The letter '{letter}' is present in the string."
    else:
        return f"The letter '{letter}' is not present in the string."

# Example usage
string = int(input("Enter the string:"))
letter = int(input("Enter the letteer to find:"))
result = find_letter_in_string(string, letter)
print(result)
