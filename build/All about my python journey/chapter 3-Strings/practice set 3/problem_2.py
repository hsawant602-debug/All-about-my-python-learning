letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''
print(letter.replace("<|Name|>","Harshad").replace("<|Date|>","3rd November 2025"))     #Chaining of .replace