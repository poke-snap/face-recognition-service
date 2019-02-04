from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
herman_image = face_recognition.load_image_file("herman.png")
sean_image = face_recognition.load_image_file('sean.jpg')
herman_face_encoding = face_recognition.face_encodings(herman_image)[0]
sean_face_encoding = face_recognition.face_encodings(sean_image)[0]

biden_image = face_recognition.load_image_file('biden.jpg')
obama_image = face_recognition.load_image_file('obama.jpg')
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

known_face_encodings = [
    herman_face_encoding,
    sean_face_encoding,
    biden_face_encoding,
    obama_face_encoding,
]

print(sean_face_encoding)
print(len(sean_face_encoding))
print(type(sean_face_encoding))
known_face_names = [
    "Herman Li",
    "Sean Takafuji",
    'Joe Biden',
    'Obama',
]

face_names = []
sean_verify_image = face_recognition.load_image_file('sean_3.jpg')
face_locations = face_recognition.face_locations(sean_verify_image)
face_encodings = face_recognition.face_encodings(sean_verify_image, face_locations)

for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        print(matches)
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        print(name)
    # face_names.append(name)

