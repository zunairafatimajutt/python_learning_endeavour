x = """If I come to think of them, Id say whatever action I committed was grandiose and laudable in some ways, if not all sorts of ways. I loved it there, but sometimes I hate it there. But right now, I can only think of great compassion and love for the young self that once went to that institute of education. I have no complaints whatsoever, I am thankful for all that has happened. And all that has come into being and still is proceeding. Im just tired of waiting for the indomitable moment when the sun will rise with my name scorching in the sky. When the ocean waves will carry my strong and courageous will with it and bring serendipity and great tranquility with my patience and love. 
"""
print (x)
print ("print is actually output")
print ('g')
print (34)
print (8.90)
print ("Dean Winchester")
g = 5
h = 12.45
m = g + h
print (int (m))
i = 18
o = 32
l = i % o 
print (float (l))
cars = ["Dodge", "Ford", "BMW", "Chevrolet"]
for x in cars:
    if x == "Dodge":
        print(x, "-Because of Fast and Furious")
    else:
        print(x)
word = ["hellow", "hellow", "hellow", "hellow", "hellow"]
for y in word:
    print(y)
def countdown(z): #define the function
    if z > 0: #add the if statement otherwise it would be a never-ending recursion
        print(z) #putting the z first will make it print in the descending order i.e, the value asisgned will be printed and then decreased, decreased, decreased.
        countdown (z - 1) #countdown (z -1) means when the function will be called after assigning the z a value, the loop will run and as it runs, it will subtract a value from the whole so that we do reach an end.
    else:
        print(z) #otherwise just make it a never-ending loop which can cause trouble hehe
z = 10 #assigned the value to z
countdown (z) #called z and the whole function will start running

def count(o):
    while o > 0:
        print(o)
        o -=1 #is equvalent to o = o-1
o = 16
count(o)
def birthday_countdown(n):
    if n > 0 and n!= 0:
        print(n)
        n -=1
        birthday_countdown(n)
    elif n == 0:
        print("Happy Birthday, Raza")
    else:
        print(n)
n = 0
birthday_countdown(n)