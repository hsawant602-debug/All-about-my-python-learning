#Types of strings
name1 = "Harshad"
name2 = 'Harshad'
name3 = """Harshad"""
name3 = '''Harshad'''

#String Slicing      
nameshort1 = name1[0:5]
nameshort2 = name2[-7:-2]  #Negative Slicing
print(nameshort1)
print(nameshort2) 
print(name1[3])
print(name1[:5])  #is same as 0:5
print(name1[3:])  #is same as 3:7
print(name1[1:6:2])