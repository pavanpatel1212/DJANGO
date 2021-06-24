odd = [1, 2, 3, 4]

odd.append([10])

print(odd)

odd.extend([100,300,500,600,800])
odd.extend([600,700])
odd.extend([800,700,600,[1,2,3,4,5,[10,20,30,40,50],6,7,8],500,400,300,200,100])
odd.append([])
res = []
for i in odd:
    if i not in res:
        res.append(i)
print(odd)
-------------------------------------------
a = range(1,10000)
x = xrange(1,10000)

print ("The size allotted using range() is : ")
print (sys.getsizeof(a))

print ("The size allotted using xrange() is : ")
print (sys.getsizeof(x))
-------------------------------------------
some tuples can be used as dictionary keys(tuples that contain immutable values like stings, number  & other tuples)
list are not immutable.
-------------------------------------------
def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
print(reverse_vowels("pavanpatel"))
print(reverse_vowels("Python"))
print(reverse_vowels("trainingCONSTULTADD"))
print(reverse_vowels("USA"))

---------------------------------------------------------------
string_name = "welcome to new way of writing"
for element in string_name:
    print(element, end=' ')
print("\n")
string_name = "hello my name is pavan"
for element in range(0, len(string_name)):
    print(string_name[element])

---------------------------------------------------------------
def findPair(A, sum):
     for i in range(len(A) - 1):
         for j in range(i + 1, len(A)):
             if A[i] + A[j] == sum:
                print("Pair found", (A[i], A[j]))
                return
     print("Pair not found")
 if __name__ == '__main__':
     A = [1,2,3,4,5,6,7,8,9,-1]
    sum = 8
     findPair(A, sum)
--------------------------------------------------------------
evTuple = (1,2,3,4,5,6,7,8,9,10)
print("Tuple Items = ", evTuple)

print("\nThe Even Numbers in this evTuple Tuple are:")
for i in range(len(evTuple)):
    if(evTuple[i] % 2 == 0):
        print(evTuple[i], end = "  ")