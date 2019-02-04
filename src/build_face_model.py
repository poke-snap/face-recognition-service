import face_recognition

import glob
import os
import pickle

def build_face_encodings(image_dir, db_path):
    file_types = ('*.jpg', '*.png')
    image_paths = []
    for file_type in file_types:
        image_paths.extend(glob.glob(os.path.join(image_dir, file_type)))
    face_encodings = {}
    for image_path in image_paths:
        person_name = image_path.split('/')[-1].split('.')[0]
        image = face_recognition.load_image_file(image_path)
        face_encodings[person_name] = face_recognition.face_encodings(image)[0]
    with open(db_path, 'wb') as f:
        pickle.dump(face_encodings, f)

build_face_encodings('test_images', 'images.pkl')

    
    # for file_name in glob.glob(os.path.join('test_images', '*.jpg'))
    # all_face_encodings = {}
    # img1 = face_recognition.load_image_file(os.path.join('test_images', 'biden.jpg'))
    # all_face_encodings["obama"] = face_recognition.face_encodings(img1)[0]

    # img2 = face_recognition.load_image_file("biden.jpg")
    # all_face_encodings["biden"] = face_recognition.face_encodings(img2)[0]

    # with open('dataset_faces.dat', 'wb') as f:
    #     pickle.dump(all_face_encodings, f)
    