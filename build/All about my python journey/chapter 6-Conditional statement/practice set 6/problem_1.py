a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if a>b and a>c and a>d:
    print(f"The number {a} is greater")
elif b>a and b>c and b>d:
    print(f"The number {b} is greater")
elif c>a and c>b and c>d:
    print(f"The number {c} is greater")
else:
    print(f"The number {d} is greater")