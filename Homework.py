import os

#Question 1:
print("What would you like to name your file?")
name = input()

print("What would you like to do with your file?")
print("Type r for read, x for write or a for append.")
action = input()

file = open(f"{name}.txt", f"{action}")        
print("Your file is ready! \n")

#Question 2: How many lines are in the file?:
count = 0
with open(f"{name}.txt" , "r") as my_file:
    for line in my_file:
        count +=1
print(f"There are {count} lines in your file")
    
#Question 3: Replacing a line of text:
file_path = input('Input a file path: ')
line_number = int(input('Input a line number: ')) # ensure we get a number for the variable
new_text = input('Input new text: ')

with open(file_path, 'r') as file:
    lines = file.readlines()

if line_number <= len(lines):
    lines[line_number - 1] = new_text + '\n'
else:
    print('Error, line does not exist')
    exit()

# lines   

with open(file_path, 'w') as file:
    file.writelines(lines)
    
#Question 4: Word count:

directory_path = os.getcwd()

total_word_count = 0

for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            total_word_count += word_count

print('Total words across all txt files: ', total_word_count)

