#In transposition cipher, the strings are 'transposed' (as the name suggests). Therefore, it is a bit hard to crack than Caesar cipher.
def Encrypt(key, message): #While encrypting, function name will be 'Encrypt'. Then, assign two variables. Message will hold the value we want to encrypt. Key will hold the value for transposition. 
    Cipher_Text = [''] * key #Our new text in an empty string being multiplied by the key. 
    for x in range(key):
        pointer = x

        while pointer < len(message):
            Cipher_Text[x] += message[pointer]
            pointer += key
    return''.join(Cipher_Text)

def main():
    message = input("Enter a message:")
    key = int(input("Enter a key:"))
    print(Encrypt(key, message))

if __name__ == '__main__':
    main()
#Enter a message:This is my first transposition cipher code.
#Enter a key:7
#Encrypted Code:'T ssoe.hmtpnriy o  s tscc friioiiatpdsrnihe'