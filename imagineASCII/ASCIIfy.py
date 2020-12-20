from PIL import Image
from math import ceil

ASCIIZ =   "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:," + "^" + "`'. "

CHAR_WIDTH = 8
CHAR_HEIGHT = 18

# resize the image.. just as the name implies
def resize_image(image, scale):
    width, height = image.size
    resized_image = image.resize((int(width*scale), int(height*scale*(CHAR_WIDTH/CHAR_HEIGHT))))

    return resized_image

# convert image to grayscale image
def grayimage(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# convert each pixel to ascii character based on their grayscale avrage
def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCIIZ[ceil(pixel/ceil(255/len(ASCIIZ)))] for pixel in pixels])
    return chars


def main():
    path = input("Enter a valid path to an image:\n")
    # path = "C:/Users/jerry/Desktop/FRI/P1/zajc.jpg"
    try:
        image = Image.open(path)
    except:
        print(path, "is not a valid path to an image.")

    scale = float(input("Enter a scale:\n"))
    if scale < 0.1 or scale > 1.0:
        return -1, "min. scale is 0.1 and max. scale is 1.0"
    # get image (new) size if resized or not
    new_image = resize_image(image, scale)

    new_image_data = pixels_to_ascii(grayimage(new_image))

    # reconstruct the image form a string
    pixel_count = len(new_image_data)
    ascii_art = "\n".join(new_image_data[i:(i+new_image.size[0])] for i in range(0, pixel_count, new_image.size[0]))

    # put the ascii art into a text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_art)

main()