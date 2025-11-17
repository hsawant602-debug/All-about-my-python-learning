text = (input("Enter the text: "))
a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

if ((a in text) or (b in text) or (c in text) or (d in text)):
    print("This text is detected as spam!")
else:
    print("This text is'n a spam text!")