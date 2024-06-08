# CAESAR CIPHER 
alpha='abcdefghijklmnopqrstuvwxyz' #alphabets listed
def encrypt(txt,k): # encrypts input plain text to a cipher text based on the key 
    cipher='' # stores encrypted text
    for l in txt:
        l=l.lower()
        i = alpha.find(l) # alphabetical index
        if i == -1:
            cipher = cipher + l # non alphabets directly concatenated
        else:
            i1 = i + k # new index after shifting thru key
            if (k > 26):
                i1 = i1 - 26 
            cipher = cipher + alpha[i1]
    return cipher

def decrypt(cipher,k): # decrypts input cipher text to a plain text based on the key 
    txt='' # stores decrypted text
    for l in cipher: 
        l=l.lower()
        i = alpha.find(l) # alphabetical index
        if i == -1:
            txt = txt + l # non alphabets directly concatenated
        else:
            i1 = i - k # new index after shifting thru key
            if (k > 26):
                i1 = i1 - 26
            txt = txt + alpha[i1]
    return txt


choice = int(input("Press 1 for encryption, 2 for decryption: "))

if choice == 1: # encryption
    text = input("Enter text to encrypt: ")
    key=int(input("Enter key for encryption (key value expected between 1 and 26): "))
    cipher_text = encrypt(text , key)
    print(f"Encrypted text: {cipher_text}")

elif choice == 2: # decryption
    text = input("Enter text to decrypt:")
    key=int(input("Enter key for encryption (key value expected between 1 and 26): "))
    plain_text = decrypt(text , key)
    print(f"Decrypted text: {plain_text}")
else:
    print(f"Wrong input")
