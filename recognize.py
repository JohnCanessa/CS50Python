# Identify and draw box on a specified person
# https://github.com/ageitgey/face_recognition/blob/master/examples/identify_and_draw_boxes_on_faces.py


# **** imports ****
import face_recognition
import numpy as np
from PIL import Image, ImageDraw

# **** message ****
print("please wait ...")

# **** load a sample picture and learn how to recognize it ****
known_image = face_recognition.load_image_file("carmen.jpg")
encoding = face_recognition.face_encodings(known_image)[0]

# **** load an image with unknown faces ****
unknown_image = face_recognition.load_image_file("rome_italy.jpg")

# **** find all the faces and face encodings in the unknown image ****
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# **** convert the image to a PIL-format image so that we can draw on top of it with the Pillow library ****
# see http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)

# **** create a Pillow ImageDraw Draw instance to draw with ****
draw = ImageDraw.Draw(pil_image)

# **** loop through each face found in the unknown image ****
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    # **** see if the face is a match for the known face(s) ****
    matches = face_recognition.compare_faces([encoding], face_encoding)

    # **** use the known face with the smallest distance to the new face ****
    face_distances = face_recognition.face_distance([encoding], face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:

        # **** draw a box around the face using the Pillow module ****
        draw.rectangle(((left - 20, top - 20), (right + 20, bottom + 20)), outline=(255, 0, 0), width=20)

# **** remove the drawing library from memory as per the Pillow docs ****
del draw

# **** message ****
print("... done !!!")

# **** display the resulting image ****
pil_image.show()