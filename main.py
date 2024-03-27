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

        list_of_numbers = []
        for _ in range(3):
            m = 1
            for value in central_pixel:
                m *= value
            list_of_numbers.append(m)
        
        list_of_numbers.sort()

        upper_rng = list_of_numbers[-1]
        lower_rng = list_of_numbers[0]
        rng = list_of_numbers[1]

        dif_to_base = ((rng-lower_rng) * (upper-lower)/(upper_rng-lower_rng)) 
        return lower + dif_to_base
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