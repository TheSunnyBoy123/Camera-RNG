import cv2 
#features to be included:
#true random number generator
#pseudo random number generator
#data encryption
#data decryption
#file encryption
#file decryption



#true random number generator
def true_randint(lower, upper, method = None):
    if method == None:
        #raise error
        raise Exception("No method found")
    if lower >= upper:
        raise Exception("Range of numbers is wrong")
    if method == 'camera':
        #get frame
        vid = cv2.VideoCapture(0) 
        ret, frame = vid.read()
        vid.release()

        #choose central pixel
        central_pixel = frame[int(len(frame)/2)][0]
        # print(central_pixel)
        m = 1
        while m <= 10000 and (m!=0 and m!=1):
            print(m)
            for value in central_pixel:
                m *= value
        # print(m) 
        #m holds a true random number
        
        normalized_m = m
        while normalized_m > 10000:
            normalized_m %= 10
        normalized_m /= 10000


        return int((normalized_m * (upper-lower)) + lower)

    elif method == 'mic':
        #use mic for generation 
        return number
    else:
        raise Exception("Invalid method")

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

    
#data decryption
def decrypt(text, method = "caesar_cipher", shift = None):
    if method == "caesar_cipher":
        ret = ""
        for alpha in text:
            if shift == None:
                shift = 3
            ret += chr(ord(alpha)-shift)
        return ret


if __name__ == "__main__":    
    print(encrypt("this is a test!"))
    print(decrypt("wklv#lv#d#whvw$"))