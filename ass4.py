Q-1 divisible by 3 & 5 print following Functions
number = int(input(" Please Enter any Positive Integer : "))
if((number % 3 == 0) or (number % 5 == 0)):
    print("Consultadd".format(number))
if((number % 3 == 0) and (number % 5 == 0)):
    print("Consultadd-python training".format(number))
else:
    print("Python training".format(number))
____________________________________________________________
Q-2 write a program to perform all operations: 

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number '))

add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
power = num1 ** num2
modulus = num1 % num2

print('Sum of ', num1, 'and', num2, 'is :', add)
print('Difference of ', num1, 'and', num2, 'is :', dif)
print('Product of ', num1, 'and', num2, 'is :', mul)
print('Division of ', num1, 'and', num2, 'is :', div)
print('Floor Division of ', num1, 'and', num2, 'is :', floor_div)
print('Exponent of ', num1, 'and', num2, 'is :', power)
print('Modulus of ', num1, 'and', num2, 'is :', modulus)
_______________________________________________________________
Q-3  Break Statement & Cont. Statement :-

for val in "string":
    if val == "i":
        break
    print(val)
	
print("It's Over ")
for letter in 'Python':    
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
var = 10            
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good Going!")

________________________________________________________________
Q-4 write a program which will find all such numbers are divisible by 7 but not multiple by 5 , between 2000 and 3000 .

nl=[]
for x in range(2000, 3000):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

___________________________________________
Q-5 
INPUT:
x=123
for i in x:
print(i)

OUTPUT:
IndentationError: expected an indented block

----------
INPUT
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break 
    else:
        print("error")

OUTPUT
0
error
1
error
2

-------------------
INPUT

count = 0
while True:
    print(count)
    count+=1
    if count>= 5:
        Break

OUTPUT
0
1
2
3
4
Traceback (most recent call last):
File "<string>", line 6, in <module>
NameError: name 'Break' is not defined
_____________________________________________________________________ 
q-6 write a program that Prints all the numbers from 0 to 6 except 3 and 6

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

_______________________________________
Q-7 

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

---- OUTPUT

Input a stringconsul72
Letters 6
Digits 2
________________________________________
Q-8
InPUT__

pas=1234
c=3
for i in range(3):
    c-=1
    inp=eval(input("enter your Password"))
    if inp==pas:
        print("correct")
        break
    else:
        print("wrong password, only{} attempts are left".format(c))

OutPUt:__

enter your Password2222
wrong password, only2 attempts are left
enter your Password1111
wrong password, only1 attempts are left
enter your Password1234
correct



 