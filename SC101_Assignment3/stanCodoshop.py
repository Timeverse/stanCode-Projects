"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixels_count = len(pixels)
    red_total = 0
    green_total = 0
    blue_total = 0
    for i in range(pixels_count):
        red_total += pixels[i].red
        green_total += pixels[i].green
        blue_total += pixels[i].blue
    red_avg = red_total // pixels_count
    green_avg = green_total // pixels_count
    blue_avg = blue_total // pixels_count
    rgb = [red_avg, green_avg, blue_avg]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb = get_average(pixels)
    best_pixel = ''
    best_dist = 10000
    for i in range(len(pixels)):
        dist = get_pixel_dist(pixels[i], rgb[0], rgb[1], rgb[2])
        if dist < best_dist:
            best_dist = dist
            best_pixel = pixels[i]
        else:
            pass
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    pixel_lst = []
    for j in range(width):
        for k in range(height):
            # This double for loop is here to address every pixel of the process picture
            for i in range(len(images)):
                # This for loop is here to address the number of pictures the user feeds in
                pixel_lst.append(images[i].get_pixel(j, k))
                # This line takes the same pixel from each feeded-in picture and puts it into the list
                best_pixel = get_best_pixel(pixel_lst)
                result_pixel = result.get_pixel(j, k)
                result_pixel.red = best_pixel.red
                result_pixel.green = best_pixel.green
                result_pixel.blue = best_pixel.blue
            pixel_lst = []
            # This line resets the list to continue for next pixel
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
