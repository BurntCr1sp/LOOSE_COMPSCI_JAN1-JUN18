English_words = ['Colour', 'Favourite', 'Honour', 'Labour', 'Neighbour', 'Odour', 'Parour', 'Rumour', 'Flavour', 'Savour']
print(English_words.strip("[]","''"))

User_input = input('Input: ').lower()

placeholder = (User_input)
letters = list(placeholder)

for i in range(len(letters) - 2):
    if letters[i:i+3] == ['o', 'u', 'r']: 
        letters.remove('u') 

output = "".join(letters)
print('Output:',output)

