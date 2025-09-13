Name = input("Enter your name: ")
Date = input("Enter Date: ")

letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''
# letter = letter.replace("<|Name|>", Name)
# letter = letter.replace("<|Date|>", Date)
# print(letter)

print(letter.replace("<|Name|>",Name).replace("<|Date|>", Date)) # chaining of .replace method