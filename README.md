# Timg
A python program for generating various images.
## What's this
This program can be used for generating various images， which can be used for evaluating the display quality, some optical testing or simply just for fun :)
### Various images including: 
* The image with a cross in the middle (for aligning)
* Red/Green/Blue/Black/White image with a grayscale of 255
* Some images for testing the crosstalk of your display device
* The gif image with frames changing from one grayscale to a bigger grayscale
* A checkboard image, and the shape of inner element is square
* Five images for testing the flicker characteristics of your display device
* White/Red/Green/Blue images with typical grayscale
* Some images with a white rectangle in the middle, the aspect ratio of the rectangle keeps up with the image, and a funny gif image
### Sample images:
|:---:|:---:|:---:|
| ![Align](https://github.com/FunsomMars/Timg/raw/master/sample/image_align.png) | ![Crosstalk](https://github.com/FunsomMars/Timg/raw/master/sample/crosstalk_black_0.png) | ![Checkerboard](https://github.com/FunsomMars/Timg/raw/master/sample/image_checkerboard.png) |
| Align | Crosstalk | Checkerboard |
| ![Flicker](https://github.com/FunsomMars/Timg/raw/master/sample/flicker3_column.png "Flicker") | ![Responsetime](https://github.com/FunsomMars/Timg/raw/master/sample/gray_responsetime63_127.gif "Responsetime") | ![Funny](https://github.com/FunsomMars/Timg/raw/master/sample/rect_scaling.gif "funny") |
| Flicker | Responsetime | Funny |
## How to use it
1. Clone the program to your local disk
2. Open the terminal/cmd, get into the path of the program
3. Run: ```python3 image_generator.py [-ppi PPI] [-gl GL] height width folder type```
### The meaning of various parameters are:
### positional arguments:
* height: The height of your image
* width: The width of your image
* folder: The folder name for storing your image
* type: The type of your image to generate, the input should be one of the values in the list: [align, purity, crosstalk, responsetime, checkerboard, flicker, grayscale, funny]
### optional arguments:
* -ppi: The ppi of your image, the default value is 401, it should be provided when generating your crosstalk image
* -gl: The gray scale list for generating images, the default value is [0, 128, 255]
* -h: For more helps please input '-h' or '--help'
## Enjoy the code！
