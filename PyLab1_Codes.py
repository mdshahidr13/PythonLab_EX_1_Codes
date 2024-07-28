# Question 1 code

print("\n----------------Question 1 code-------------------")
def Add():
    num_list = [1, 2, 3, 4, 5]
    total_sum = sum(num_list)
    print("Sum of the list is: ", total_sum)

def Multiply():
    num_list = [1, 2, 3, 4, 5]
    product = 1
    for num in num_list:
        product *= num
    print("Product of the list is: ", product)

def Largest():
    num_list = [1, 2, 3, 4, 5]
    max_num = max(num_list)
    print("Largest number in the list is: ", max_num)

def Smallest():
    num_list = [1, 2, 3, 4, 5]
    min_num = min(num_list)
    print("Smallest number in the list is: ", min_num)

def main():
    Add()
    Multiply()
    Largest()
    Smallest()

if __name__ == "__main__":
    main()

print("-----------------------------------------------------------")

# Question 2 code
print("\n------Question 2 code-----------")
A = ['abc', 'xyz', 'aba', '1221']

for index in range(len(A)):
    string = A[index]
    if string[0] == string[-1]:
        print(f"String: '{string}' at index {index}")

print("---------------------------------\n")

# Question 3 code

print("-----------Question 3 Code-----------------\n")
row = 5
for i in range(1,row+1):
    print(" " * (row - i), end="")
    for j in range(i):
        print(chr(65+j), end=" ")
    print()

print("\n")
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
print("-----------------------------------------------------")

# Question 4 code
print("\n----------Question 4 code----------")

print("\n")
ListColor = ["Black", "Red", "Maroon", "Yellow"]
ListColorCode = ["000000", "FF0000","800000", "FFFF00"]
ListDict = []
for i in range(len(ListColor)):
    color = ListColor[i]
    colorCode = ListColorCode[i]
    ListDict.append({'colorName':color, 'colorCode':colorCode})
print(ListDict)
print("-------------------------------------------------")

#Question 5 code
print("\n------------Question 5 code--------------")
print("\nEven numbers and their squares in range(1, 50):")
for num in range(1, 50):
    if num % 2 == 0:
        print(f"Even Number: {num}, Square: {num ** 2}")

print()

print("Even numbers and their squares in range(1, 100):")
for num in range(1, 100):
    if num % 2 == 0:
        print(f"Even Number: {num}, Square: {num ** 2}")
print("-------------------------------------------------------")

#Question 6 code
print("\n------------Question 6 code--------------")

number = int(input("Enter the four digit number = "))
sum_of_digits = 0
reverse = 0
original_number = number
while number > 0:
    digit = number % 10  
    sum_of_digits += digit  
    reverse = reverse * 10 + digit 
    number = number // 10
print("Sum of digits: " ,sum_of_digits)
print("Reverse: ",reverse)

print("----------------------------------------------------")

#Question 7 code
print("\n------------Question 7 code--------------")
print("Enter the sides of the first triangle:")
a1 = float(input("Side a1: "))
b1 = float(input("Side b1: "))
c1 = float(input("Side c1: "))

s1 = (a1 + b1 + c1) / 2
area1 = (s1 * (s1 - a1) * (s1 - b1) * (s1 - c1)) ** 0.5

print("Enter the sides of the second triangle:")
a2 = float(input("Side a2: "))
b2 = float(input("Side b2: "))
c2 = float(input("Side c2: "))

s2 = (a2 + b2 + c2) / 2
area2 = (s2 * (s2 - a2) * (s2 - b2) * (s2 - c2)) ** 0.5

total_area = area1 + area2

percentage1 = (area1 / total_area) * 100 if total_area > 0 else 0
percentage2 = (area2 / total_area) * 100 if total_area > 0 else 0

print("Area of the first triangle:", area1)
print("Area of the second triangle:", area2)
print("Total area enclosed by both triangles:", total_area)
print("First triangle's contribution: {:.2f}%".format(percentage1))
print("Second triangle's contribution: {:.2f}%".format(percentage2))

print("---------------------------------------------------------")

# Question 8 code

print("----------------Question 8 code-----------------")
people_info = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "A-"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "B+"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "O-"},
    {"name": "James Thomas", "age": 45, "blood_group": "AB+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "A+"},
]

# Print each person's information
for person in people_info:
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("Blood Group:", person["blood_group"])
    print("-" * 20)

print("\n------------------------------------------------------")

# Question 9 code
print("\n----------------Question 9 code-----------------\n")

input_tuple = ("python", "learn", "includehelp")
last_chars = [s[-1] for s in input_tuple]
print(last_chars)

print("\n--------------------------------------------------")

# Question 10 code
print("\n----------------Question 10 code-----------------\n")

months_days = [
    ("January", 31),
    ("February", 28),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]
month = input("Enter the month name: ")
for m, days in months_days:
    if m == month:
        month_found = True
        if month == "February":
            year = int(input("Enter the year: "))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days = 29
        print("The number of days in", month, "is:", days)
        break           
print("\n----------------------------------------------")