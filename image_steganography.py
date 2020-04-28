import PIL.Image as Image
import numpy as np
import random

def main():

    print( '1. Encode Image\t\t2. Decode Image\t\t3. Exit\n')
    choice = int(input('Enter your Choice: '))

    if choice == 1:
        image = input('Enter path of image you want to encode: ')
        secret_message = input('Enter the message you want to hide : ')
        encode(image, secret_message)

    elif choice == 2:
        image = input('Enter path of image you want to decode: ')
        decode(image)

    elif choice == 3:
        exit()

    else:
        print('Invalid choice entered... Exiting the program...')
        exit()

def decode(image):

    try:
        secret_message  = ''
        img = Image.open(image)
        img_ar = np.array(img)
        length = img_ar[0][0][2]
        skip = img_ar[0][1][2]
        width, height = img.size
        pixels = width * height
        j = 0
        j += skip

        while j < pixels:
            k = j % width
            i = j // height
            if len(secret_message) > length:
                break

            else:
                secret_message += chr(img_ar[i][k][2])
            j += skip

        print('Decoded Message: ' + secret_message)

    except FileNotFoundError:
        print('Please specify a valid path.')
        exit()

def encode(image,secret_message):

    try:
        secret_message = list(secret_message)
        img = Image.open(image)
        width, height = img.size
        pixels = width*height
        if pixels<len(secret_message):
            print('Encoding is not possible')
            exit()

        else:
            while True:
                skip = random.randint(3,209)
                if pixels//skip >= len(secret_message):
                    break
            edit_image = np.array(img)
            counter = 0
            info = False
            j = 0

            while j < pixels:
                k = j%width
                i = j//height
                if counter >= len(secret_message):
                    break
                elif j == 0 and info == False:
                    edit_image[i][k][2] = len(secret_message)-1
                    edit_image[i][k+1][2] = skip
                    info = True
                else:
                    edit_image[i][k][2] = ord(secret_message[counter])
                    counter += 1
                j+=skip
            new_img = Image.fromarray(edit_image)
            new_img.save('img_with_secretmsg.png')
            print('Image saved successfully with name img_with_secretmsg.png\n')
            
    except FileNotFoundError:
        print('Please specify a valid path.')
        exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Thanks for using!')
