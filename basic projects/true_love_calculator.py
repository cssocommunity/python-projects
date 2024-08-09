print("true love calculator!")

name0 = input("what's your name? ")
name1 = input("what's your name? ")

name = name0 + name1  # concatenate the names to get a single string

# Define the word "superpower"
word = "truelove"

# Initialize a counter for matches
match_count = 0

# Count the occurrences of each letter in the name
for letter in word:
    match_count += name.lower().count(letter)

print("your score is " + str(match_count) + " \n thank you for using our program")
