#comprehension
string = "hello my name is josh"
list1 = []
for letter in string:
    list1.append(letter)

list1 = [letter for letter in string]

mylist = [s for s in "samsung"]

mylist = [num for num in range(31,45)


mylist = [x for x in range(0,20) if x%2==0]


#cels to fahren
celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp + 32)for temp in celcius]


#second way cels to fahren
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32)) 
#If else 
results = [x if x%2==0 else "ODD" for x in range(0,11)]

# nested loop 

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)


#nested loop list comprehension 
mylist = [x*y for x in [2,4,6]for y in [1,10,1000]]

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == "s":
        print(word)


#Use range() to print all the even numbers from 0 to 10.
for num in range(0,11,2):
    print(num)
#OR
list(range(0,11,2))

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

[x for x in range(1,51) if x%3 == 0 ]

#Go through the string below and if the length of a word is even print "even!"
st  ==  'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) %2 ==0:
        print(word)


#Good old FizzBuzz
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('fizzbuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]



#Pig latin 

def pig_latin(word):
    
    first_letter = word[0]
    
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word




def myfunc(a,b,c=0,d=0,e=0):
#returns 5% of the sum of a and b 
return sum((a,b,c,d,e)) *0.05

# *args takes in an arbitary amount of arguments 
def myfunc(*args):
    return sum(args) * 0.05



# **kwargs creates a dictionary of the arguments used 
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

#using the function like 

myfunc(fruit='apple',veggie = 'lettuce')


def myfunc(*args,**kwargs):
    
    print('I would like {} {}'.format(args[0],kwargs['food']))

#using the code
myfunc(10,20,30, fruit='orange',food='eggs',animal='dog')

#output "I would like 10 eggs"


#take arbitrary num of arguments return a list containing even nums

def myfunc(*args):
    s = []
    for x in args:
        if x %2==0:
            s.append(x)
    return s

#retuns lesser of the two evens but returns greater if one of bon number are odd
def lesser_of_two_evens(a,b):
	if a %2 ==0 and b%2==0:
		if a <b:
			result = a
		else:
			result = b
	else :
		if a >b:
			result = a
		else:
			result = b

	return result

#Clean verstion 
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)


#Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    wordlist = text.split().lower()
    return wordlist[0][0] == wordlist[1][0]


#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20




#Write a function that capitalizes the first and fourth letters of a name

def  old_macdonaldold_macd (name):
	if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
	else:
        return 'Name is too short!'

#Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False
#Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'


#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# Lambda functions

def square(num):
	return num **2

#turns into 
square = lambda num: num **2


#using map with lambda
mynums = [1,2,3,4,5,6]

list(map(lambda num:num**2,mynums))


# Calculate the volume of a sphere given its Radius

def vol(rad):
    return (4/3) * (3.14) *(rad**3)

#checks whether a number is in a given range (inclusive of high and low)
 def ran_check(num,low,high):
    if num in range(low,high+1):
        print ('{} is in range between {} and {}'.format(num,low,high))
    else:
        print ('this number is out of range')

#gives out a boolean true or false


def  ran_boolran_boo (num,low,high):
    return num in range(low,high+1)


#Counts the number of upper and lower charcters in a list 

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

#takes a list and returns only unique numbers
def unique_list(lst):
    x = []
    for s in lst:
        if s not in x:
            x.append(s)
    return x

# multiply all numbers in a list 

def multiply(numbers):
	total = 1 
	for x in numbers:
		total *= x 
	return total



#checks whether a passed string is a palindrome or not

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing


#check whether a string contains every letter in the alphabet 

import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())






class Book():
    
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title}, by {self.author} it has {self.pages} pages"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print ("A book object has been deleted")


#Calculate Line distance and slope

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2 
        
        
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x1-x2)**2 + (y2-y1)**2)**0.5
        
        
        
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y2-y1)/(x2-x1)

#Calculate Cylinder volume and surface area 


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * 3.14 * (self.radius)**2
    
    def surface_area(self):
        top = 3.14* (self.radius**2)
        
        return (2*top) + (2*3.14*self.radius*self.height)
#Account Class 

class Account:
    def __init__(self,owner,balance=0):
        
        self.owner = owner 
        self.balance = balance
        
    def deposit(self,dep_amt):
        
        self.balance = self.balance + dep_amt
        print (f"Added {dep_amt} to the balance")
        
    def withraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print ("Withraw accepted")
        else:
            print("Sorry Not enough funds")
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

        
