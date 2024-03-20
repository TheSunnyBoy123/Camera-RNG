#features to be included:
#true random number generator
#pseudo random number generator
#data encryption
#data decryption
#file encryption
#file decryption



#data encryption
def encrypt(text, method = "caesar_cipher", shift = None):
    #caesar cipher
    if method == "caesar_cipher":
        ret = ""
        for alpha in text:
            if shift == None:
                shift = 3
            ret += chr(ord(alpha)+shift)

        return ret

    

def decrypt(text, method = "caesar_cipher", shift = None):
    if method == "caesar_cipher":
        ret = ""
        for alpha in text:
            if shift == None:
                shift = 3
            ret += chr(ord(alpha)-shift)
        return ret

    
print(encrypt("this is a test!"))
print(decrypt("wklv#lv#d#whvw$"))