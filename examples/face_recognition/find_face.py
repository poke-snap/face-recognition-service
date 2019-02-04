from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
herman_image = face_recognition.load_image_file("herman.png")
sean_image = face_recognition.load_image_file('sean.jpg')
herman_face_encoding = face_recognition.face_encodings(herman_image)[0]
sean_face_encoding = face_recognition.face_encodings(sean_image)[0]


# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image) # face_recognition.face_locations(image, model='cnn')

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save('herman_face.jpg')