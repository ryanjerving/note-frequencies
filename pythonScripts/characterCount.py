# Script to count characters in string

# import module to make printing look better

import pprint

# Generate string

message = input("Type in a sentence, any sentence: ")
print("You typed: " + message)

print("Now, I'll count the letters.")



# Create a dictionary that will store counts of each letter

count = {}

# Go through character by character,
# check to see if already in dictionary as key.
# If not, create key and initialize at one;
# if so, add one to the key

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Print it out

print(pprint.pformat(count))
                
      
