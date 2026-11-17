# #find the sum of the digits 
# n=int(input("num: "))
# sum = 0
# while n > 0:
#     a=n % 10
#     sum +=a
#     n=n//10
    
# print(sum)    
# s=input()
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev == s)     

# a= "abc"
# print(a[1:2])
def display(**kwargs):
    student = {}
    for key, value in kwargs.items():
        print(key, ":", value)
        student[key] = value
    print(student)
display(name="Sonal", age=22, city="Pune")


students = {
    "Amit": [80, 70, 65],
    "Neha": [35, 60, 70],
    "Raj": [55, 65, 75]
}

passed_students = []
subjects = {"Python", "DBMS", "Python", "Networking"}

for name, marks in students.items():
    if all(m >= 40 for m in marks):
        passed_students.append(name)

print("Passed students:", passed_students)
print("Unique subjects:", subjects)