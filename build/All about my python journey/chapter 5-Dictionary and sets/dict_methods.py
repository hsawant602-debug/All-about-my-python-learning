marks = {
    "Harshad":100,
    "Harry":98,
    "Sawant":95,
    0:"Harshad"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harshad":99, "harshu":89})
print(marks.get("Harry2"))  # Returns none
# print(marks["Harry2"])  # Returns an error
marks.pop(0)
marks.popitem()
print(marks)