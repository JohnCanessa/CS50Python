# Find faces in picture
# https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py


# **** import libraries and modules ****
from PIL import Image
import face_recognition


# **** define main method ****
def main():

    # **** load the jpg file into a numpy array ****
    image = face_recognition.load_image_file("rome_italy.jpg")

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=2)

    # **** loop through all detected faces ****
    for face_location in face_locations:

        # **** get and print the location of each face in this image ****
        top, right, bottom, left = face_location
        print(f"top: {top} right: {right} bottom: {bottom} left: {left}")

        # **** show the detected face ****
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()


# **** call main method ****
main()