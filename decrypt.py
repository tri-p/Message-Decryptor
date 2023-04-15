# PABUNA, KATRINA B.
# PROBLEM 2: DECRYPTION 
# Pseudocode
# Ask the user for an encrypted text then save it
encrypted_str = input("Enter a string to decrypt: ")

# Check every character
for i in range(len(encrypted_str)):

# Convert '*' to 'a'
    if encrypted_str[i] == "*":
        decrypted_str += "a"

# Convert '&' to 'e'
    elif encrypted_str[i] == "&":
        decrypted_str += "e"

# Convert '#' to 'i'
    elif encrypted_str[i] == "#":
        decrypted_str += "i"

# Convert '+' to 'o'
    elif encrypted_str[i] == "+":
        decrypted_str += "o"

# Convert '!' to 'u'
    elif encrypted_str[i] == "!":
        decrypted_str += "u"
    else:
        decrypted_str += encrypted_str[i]

# Print the output