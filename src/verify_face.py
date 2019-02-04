# from PIL import Image
import face_recognition
import pickle
import numpy as np



def load_face_encodings():
    # Load face encodings
    with open('images.pkl', 'rb') as f:
        return pickle.load(f)

    # # Grab the list of names and the list of encodings
    # face_names = list(all_face_encodings.keys())
    # face_encodings = np.array(list(all_face_encodings.values()))

    # # Try comparing an unknown image
    # unknown_image = face_recognition.load_image_file("obama_small.jpg")
    # unknown_face = face_recognition.face_encodings(unknown_image)
    # result = face_recognition.compare_faces(face_encodings, unknown_face)

    # # Print the result as a list of names with True/False
    # names_with_result = list(zip(face_names, result))
    # print(names_with_result)


def verify_face(face_image_path):
    all_face_encodings = load_face_encodings()
    known_face_names = list(all_face_encodings.keys())
    known_face_encodings = np.array(list(all_face_encodings.values()))

    face_image = face_recognition.load_image_file(face_image_path)
    face_locations = face_recognition.face_locations(face_image)
    face_encodings = face_recognition.face_encodings(face_image, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            return name
    return name


