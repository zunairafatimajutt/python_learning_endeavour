#Encryption: The process of converting information or data, into a code.
#Decryption: The process of converting coded messages or unclear messages, into understandable and comprehensive information. 
#Ceaser Cipher: Simplest and oldest methods of encrypting messages It works by shifting the letters in the plaintext message by a certain number of positions, known as the "shift" or "key".
#Plain alphabet text is the standard alphabet order (ABCDEFG...) and Cipher is the plain alphabet text shifted left or right by a certain number of positions. 
#Encryption-

def ceasar(message, key, mode): #1-define the function. 2-place the variables (mode can either be encrypt or decrypt,)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #The ruler
    translation = '' #empty string for the new letters
    message = message.upper() #Everything in CAPS to match the ruler.
    key = key % 26 #The number we'll assign will be here. % will make sure out key is in between the range 0-25 which is 26.
    for i in message: #Look at the number of each letter (we'll print later)
        temporary_letters = LETTERS.find(i) #find the number on which the alphabets are.
        if mode == 'encrypt':
            temporary_letters += key 
        elif mode == 'decrypt':
            temporary_letters -= key 
        temporary_letters = temporary_letters % len(LETTERS) #will keep inside the range
        translation += LETTERS[temporary_letters]
    return translation #give the secret word back
print(ceasar("CYBRARY", 11, 'encrypt')) #values of variables respectively eh~

#Explanation:THE NESTED BOXES (My Analogy)
#1. The Big Cage: The Function (def ceasar...)
#You build a big cage and put a label on it. Everything inside this cage belongs to this specific tool. It won't run until you call its name.
#2. The Middle Box: The Loop (for i in messege:)
#You put a box inside the cage. This box is a machine that says, "I am going to grab every letter in the message, one by one." Everything inside this box will happen over and over again for every letter.
#3. The Small Box: The Conditionals (if / elif)
#You put a smaller box inside the loop box. This box makes a decision: "Are we encrypting or decrypting?" It only runs the math for the specific mode.
#4. The Accessories (The final steps)
#After the decision is made in the if/elif box, you add the accessories (the modulo wrap-around and the translation += ...). These are also inside the for loop, so they happen for every single letter.
#5. The Output (The return statement)
#You take the finished product out of the loop box, out of the function cage, and hand it to the user.

#fun try:
def ceasar(message, secret_num, mode):
    RULER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Translation = ''
    message = message.upper()
    secret_num = secret_num % 26
    for i in message:
        temporary_letters = RULER.find(i)
        if mode == 'encrypt':
            temporary_letters += secret_num
        elif mode == 'decrypt':
            temporary_letters -= secret_num
        temporary_letters = temporary_letters % 26
        Translation += RULER[temporary_letters]
    return Translation
print(ceasar("I hate chocolate", 28, 'encrypt'))

#KBJCVGBEJQEQNCVG
def ceasar(message, secret_num, mode):
    RULER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Translation = ''
    message = message.upper()
    secret_num = secret_num % 26
    for i in message:
        temporary_letters = RULER.find(i)
        if mode == 'encrypt':
            temporary_letters += secret_num
        elif mode == 'decrypt':
            temporary_letters -= secret_num
        temporary_letters = temporary_letters % 26
        Translation += RULER[temporary_letters]
    return Translation
print(ceasar("KBJCVGBEJQEQNCVG", 28, 'decrypt'))

#experiment2:
def ceasar(message, secret_num, mode):
    RULER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Translation = ''
    message = message.upper()
    secret_num = secret_num % 26
    for i in message:
        temporary_letters = RULER.find(i)
        if mode == 'encrypt':
            temporary_letters += secret_num
        elif mode == 'decrypt':
            temporary_letters -= secret_num
        temporary_letters = temporary_letters % 26
        Translation += RULER[temporary_letters]
    return Translation
print(ceasar("I AM SO FRUSTRATED RIGHT NOW", 9, 'encrypt'))

#I AM ABOUT TO DECRYPT the Mssg WITHOUT THE KEY. Also without they key: here's what you're going to do nere, brute force it. hehe. let's try
def ceasar(Message, Key, Mode):
    RULER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    TRANSLATION = ''
    Message = Message.upper()
    Key = Key % 26
    for i in Message :
        Tempoletters = RULER.find(i)
        if Mode == 'Encrypt':
            Tempoletters += Key 
        elif Mode == 'Decrypt':
            Tempoletters -= Key
        Tempoletters = Tempoletters % 26
        TRANSLATION += RULER[Tempoletters]
    return TRANSLATION #ok, i found some random gibberish, let add a little magic to find all the possibilites and then ill know one of them was indeed the secret message
#the magic recipe:
Message = "RIJVIBXIOADBCAJCNMIARPQCIWXF" #create the variable that holds the scrambled text
for key in range(1, 26):#loop will run 25 times. the key in first run will be 1 and so on and on.
    print(f"Key {key}: {ceasar(Message, key, 'Decrypt')}")
#the secret message was on line 9: IZAMZSOZFRUSTRATEDZRIGHTZNOW remove the Z because that is space. I AM SO FRUSTRATED RIGHT NOW.