from PIL import Image
from math import ceil

ASCIIZ =   "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:," + "^" + "`'. "

CHAR_WIDTH = 8
CHAR_HEIGHT = 18

# spremeni velikost slike
def resize_image(image, scale):
    width, height = image.size
    resized_image = image.resize((int(width*scale), int(height*scale*(CHAR_WIDTH/CHAR_HEIGHT))))

    return resized_image

# naredi sivinsko sliko
def grayimage(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# vsakemu pikslu priredi ascii znak glede na njegovo sivost
def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCIIZ[ceil(pixel/ceil(255/len(ASCIIZ)))] for pixel in pixels])
    return chars


def main():
    # prejme vnos poti do slike
    path = input("Enter a valid path to an image:\n")
    
    # testira za napako pri vnosu
    try:
        image = Image.open(path)
    except:
        print(path, "is not a valid path to an image.")

    scale = float(input("Enter a scale:\n"))
    if scale < 0.1 or scale > 1.0:
        return -1, "min. scale is 0.1 and max. scale is 1.0"
    # dobi novo sliko v vsakem primeru
    new_image = resize_image(image, scale)

    new_image_data = pixels_to_ascii(grayimage(new_image))

    # sestavi sliko iz niza znakov
    pixel_count = len(new_image_data)
    ascii_art = "\n".join(new_image_data[i:(i+new_image.size[0])] for i in range(0, pixel_count, new_image.size[0]))

    # ascii art shrani v tekstovno detoteko
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_art)

main()
