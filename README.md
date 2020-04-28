# Image-Steganography
A python script to encode/decode text within/from an image using Least Significant Bit (LSB) algorithm. Image to be used in <code>.png</code> format.
## Image Steganography using LSB

Steganography is a method of hiding secret data, by embedding it into an audio, video, image or text file. 
It is one of the methods employed to protect secret or sensitive data from malicious attacks.
The idea behind LSB embedding is that if we change the last bit value of a pixel, there won’t be much visible change in the color.
It exploits the fact that the level of precision in many image formats is far greater than that perceivable by average human vision. 
Therefore, an altered image with slight variations in its colors will be indistinguishable from the original by a human being, 
just by looking at it.
For example, 0 is black. Changing the value to 1 won’t make much of a difference since it is still black, just a lighter shade.
## Example Images
You can view the example images in the folder test_images. One of them is encoded with a text and other is not, you may not see the difference between the two as it is undetectable by human eyes.
