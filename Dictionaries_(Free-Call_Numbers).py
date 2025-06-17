import os

mapping = {
    'A': '2','B': '2','C': '2',
    'D': '3','E': '3','F': '3',
    'G': '4','H': '4','I': '4',
    'J': '5','K': '5','L': '5',
    'M': '6','N': '6','O': '6',
    'P': '7','Q': '7','R': '7','S': '7',
    'T': '8','U': '8','V': '8',
    'W': '9','X': '9','Y': '9','Z': '9',
    '0': '+'
}

os.system('clear')

print('-- Enter the free-call number --')
user = input(':').upper()

if len(user) > 7:
    print('E!r*r, To many characters.')
    exit()

else:
    print('')

    listed = list(user)

    while ' ' in listed:
        listed.remove(' ')

    result = ""                                    

    for char in user:
        if char in mapping:
            result += mapping[char]

    spacing = list(result)

    print(spacing)

    print('-- The converted free-call number  --')
    print(":" + "0800",result)

    print('')