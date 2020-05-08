# **** ****
from PIL import Image, ImageFilter

# **** load the image ****
before = Image.open("bridge.jpg")

# **** blur the image ****
after = before.filter(ImageFilter.BLUR)

# **** save the image ****
after.save("out.jpg")