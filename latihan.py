# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#Print on shell
print("Hello world")

#create a variable
name = "Muzaffar"
print(name)

#getting an input from user...
number = input("Enter a number: ")
print("You have entered",number)

# String
profession = "Lecturer"
print(profession)

# Operation - Concatenation (+)
print("My name is "+name)
print("My name is "+name+" and I am a "+profession)


# Number and it's operation

num1 = 10
num2 = 3

plus = num1+num2
print(plus)

minus = num1 - num2
print(minus)

product = num1 * num2
print(product)

division = num1 / num2
print(division)

modulo = num1 % num2
print(modulo)

power  = num1 ** num2;
print(power)

umur = 20

print("Umur saya adalah",umur,"tahun")
print("Umur saya adalah "+str(umur))

# Boolean and it's operation -> AND 
# FALSE and FALSE = FALSE
# TRUE and  FALSE = FALSE
# FALSE and  TRUE = FALSE
# TRUE and  TRUE = TRUE

hungry = True
sleepy = False

print(hungry and sleepy)
print(hungry or sleepy)
print(not hungry)

#Control Flow


# Conditional

# Show if and alse

age = 15

#If else
if (age > 18):
    print("You can watch the movie")
else:
    print("You cannot watch the movie")
#If elif dan else

if (age < 13):
    print("You cannot watch the movie")
elif (age < 18):
    print("You can watch the movie with parents")
else:
    print("You can watch the movie")

# Check if a number is odd or even..
# pattern recognition - The remainder of it's division operation with 2 is 0 (L1)
## If else , string concatenation , math operation (%)
newNum = 13
if (newNum % 2 == 0):
    print(newNum,"is an even number")
else:
    print(newNum,"is an odd number")

## TIcket validation based on following rules: (L1)
## 18 ke bawah = diskaun 50 percent
## 19-25 diskaun = 25%
## 26-65 -tiada diskaun 
## 65 ke atas = diskaun 50 percent
## and  ataupun emphasize susunan 
## If else , string concatenation , math operation (*)

passengerAge = 70
ticketPrice = 100
if (age < 18):
    print("The ticket price is",ticketPrice*0.5)
elif (age < 25):
    print("The ticket price is",ticketPrice*0.75)
elif (age < 65):
    print("The ticket price is",ticketPrice)
else:
    print("The ticket price is {ticketPrice*0.5}")
    
# Repetition

