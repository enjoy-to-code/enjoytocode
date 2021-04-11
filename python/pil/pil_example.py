# pip install pil
from PIL import Image  

# Load original image
original_image = Image.open("model_ruby.jpg") 
# rotate 180 degrees
rotated_image = original_image.rotate(180)
# create grayscale image
grayscale_image = original_image.convert("L")

# Display images
original_image.show() 
rotated_image.show()
grayscale_image.show()
