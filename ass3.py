Q-1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

a=2
b=5.5
c="Pavan"

print(id(a))
print(id(b))
print(id(c))
(venv)   C:\pavan training>python demo.py
2839260719440
2839266633808
2839266550384
------------------------------------
a=2
b=5.5
c="Pavan"

print(type(a))
print(type(b))
print(type(c))

  (venv)    C:\pavan training>python demo.py
<class 'int'>
<class 'float'>
<class 'str'>

Q- 2. Create a variable of type complex and swap it with another variable of type integer.

a=int(input('Enter the first number ='))
b=int(input('Enter the Second number='))
sum=a+b

print(sum)

(venv) C:\pavan training>python demo.py
Enter the first number =5
Enter the Second number =5
10

Q-3. Swap two numbers using a third variable and do the same task without using any third variable.

a=6
b=10
print("A",a)
print("B",b)
a,b=b,a
print("A")
print("B")

Q-4 write a program with using 2x version and 3x version

2x--> print "pavan"
	x=raaw_input()
3x--> print("pavan")
	x=input()

Q-5 write a program to check the data type of the entered values in python

number1 = input("Enter number and hit enter ")
print("Printing type of input value")
print("type of number ", type(number1))

Q-6 create variable using formats such as camel case in python

def change_case(str):
         return ''.join(['_'+i.lower() if i.isupper()
               else i for i in str]).lstrip('_')
     str = "PavanVishnukumarPatel"
print(change_case(str))