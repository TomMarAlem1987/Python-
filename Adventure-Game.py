'''
#Intro to Python, Adventure Game:
'''
I intend to write a game that is a mix between Zelda and American Gladiators in an adventure format.
'''
main_character= [
    {'name':'Iron Hammer', 'power':'Smash Attack','status':'First Class'},
    {'name':'White Lotus', 'power':'Slish Slash Attack', 'status':'Second Class'},
    {'name':'Jake From State Farm', 'power':'Incendiary Flatulence Attack', 'status':'First Class'}
]

# Iterate through the list of dictionaries
for character in main_character:
    # Iterate through the key-value pairs in each dictionary
    for key, value in character.items():
        print(f'{key}: {value}')
    print()  # Add an empty line between characters
    
print('\n')
#Level One:
print("LEVEL ONE: \n")
print("Welcome to the Lilly Pad of Doom \n")
print("\n")

#Getting player input as to which character they want to play:
player_choice= print(input("Please select a player: "))
'''