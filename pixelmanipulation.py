from PIL import Image

def pixelswap(input_path, output_path, decrypted_img_path):
    img = Image.open(input_path)
    # print('Here is uploaded image')
    # img.show()
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i,j]
            encrypted_image_pixel = (b, g, r)
            pixels[i, j] = encrypted_image_pixel

    img.save(output_path)
    print('[ + ] Image encrypted successfully!')
    img.show()

    print('Start decryption process? (yes/no): ')

    x = input().strip().lower()
    if x =='yes':
        img = Image.open(output_path)
        pixels = img.load()
        width, height = img.size
        for i in range(width):
            for j in range(height):
                b, g, r = pixels[i,j]
                decrypted_image_pixel = (r, g, b)
                pixels[i, j] = decrypted_image_pixel

        img.save(decrypted_img_path)
        img.show()
        print('[ + ] Image decrypted successfully!')


def brightness_pixel_manipulation(input_path, output_path, decrypted_img_path, factor):
    factor = int(factor)
    img = Image.open(input_path)
    # print('Here is uploaded image')
    # img.show()
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i,j]
            r = r + factor
            g = g + factor
            b = b + factor
            encrypted_image_pixel = min(255, max(0,r)), min(255, max(0,g)), min(255, max(0,b))
            pixels[i, j] = encrypted_image_pixel

    img.save(output_path)
    print('[ + ] Image encrypted successfully!')
    img.show()

    print('Do you want to start the decryption process? Type yes or no')
    x = input().strip().lower()
    if x =='yes':
        img = Image.open(output_path)
        pixels = img.load()
        width, height = img.size
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i,j]
                r = r - factor
                g = g - factor
                b = b - factor
                decrypted_image_pixel = (r, g, b)
                pixels[i, j] = decrypted_image_pixel

        img.save(decrypted_img_path)
        img.show()
        print('[ + ] Image decrypted successfully!')

def contrast_pixel_manipulation(input_path, output_path, decrypted_img_path,factor):
    factor = float(factor)
    img = Image.open(input_path)
    # print('Here is uploaded image')
    # img.show()
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i,j]
            r = int(((r - 128) * factor) + 128)
            g = int(((g - 128) * factor) + 128) 
            b = int(((b - 128) * factor) + 128)
            encrypted_image_pixel = (min(255, max(0,r))), (min(255, max(0,g))),(min(255, max(0,b)))
            pixels[i, j] = encrypted_image_pixel

    img.save(output_path)
    print('[ + ] Image has been encrypted!!')
    # print('encrypted pixels:', r, b, g)
    img.show()

    print('Start decryption process? (yes/no): ')
    x = input().strip().lower()
    if x =='yes':
        img = Image.open(output_path)
        pixels = img.load()
        width, height = img.size
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i,j]
                r = int(((r - 128) / factor)) + 128
                g = int(((g - 128) / factor)) + 128
                b = int(((b - 128) / factor)) + 128
                decrypted_image_pixel =  (min(255, max(0,r))), (min(255, max(0,g))), (min(255, max(0,b)))
                pixels[i, j] = decrypted_image_pixel

        img.save(decrypted_img_path)
        img.show()
        print('[ + ] Image has been decrypted successfully!!')
        # print('decrypted pixels:',  r, b, g)

def main():
    input_image = r"C:\Users\aenpa\Downloads\1661272389602.jpeg"
    encrypted_image_path = r"C:\Users\aenpa\Downloads\encrypted.jpeg"
    decrypted_image_path = r"C:\Users\aenpa\Downloads\decrypted.jpeg"

    print('Choose pixel manipulation method:')
    print('1. Swap RGB values')
    print('2. Adjust brightness')
    print('3. Adjust contrast')

    h = input().strip().lower()
    if h == '1':
        pixelswap(input_image, encrypted_image_path, decrypted_image_path)

    elif h == '2':
        print('Enter the value of factor(integer) (With Higher Value of the factor, the precision of decrypted image will be lost)')
        factor = input()
        brightness_pixel_manipulation(input_image, encrypted_image_path, decrypted_image_path,factor)

    elif h == '3':
        print('Enter the value of factor (With Higher Value of the factor, the precision of decrypted image will be lost)')
        factor = input()
        contrast_pixel_manipulation(input_image, encrypted_image_path, decrypted_image_path,factor)

    else:
        print('invalid choice')
main()