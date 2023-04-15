# PABUNA, KATRINA B.
# PROBLEM 2: DECRYPTION 
# Pseudocode
# Ask the user for an encrypted text then save it
print("\033[93m=" * 80, "\n")
encrypted_str = input("\033[92mEnter a string to decrypt: \033[97m")
decrypted_str = ""

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
print("\n", "\033[93m=" * 80, "\n")
print("\033[1m\033[95mThe Plain Text:\x1B[3m\033[97m", decrypted_str)
print("\n", "\033[93m=" * 80, "\n")