"""
Developer: Ersin ÖZTÜRK
Program Name: Count The Letters (we assumed no punctuations)
Date: 07.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the string and count the letters with dictionary format.
"""

input_text = input("Write the text to count the letters:\n").lower()   # Sentences take as string without punctuation
letters = [i for i in input_text if i !=' ']                           # convert the letters from string to list
my_dict={}                                                             # produce the dictionary as none
for i in range(len(letters)):                                          # Hold each different items as key in the list
    my_dict[letters[i]]=0                                              # Assign to "0" value to each different key
    for j in range(len(letters)):                                      # Compare letters with eachother
        if input_text[i]==input_text[j]:                               # No problem because the keys are unic
            my_dict[letters[i]] +=1                                    # If letters are equal, increment the counter
print(my_dict)                                                         # Print the dictionary


