import os
import face_recognition
import random
# i=0
count=0
# face_locations = []
# face_encodings = []
path = '.'
for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        fname_path = os.path.join(dirname, filename)
        fext = os.path.splitext(fname_path)[1]
        if fext == '.png':
            print (fname_path)
            if filename.endswith('.png') :
                count = count + 1  
print('images:', count)
images=fname_path
    print(images)
# while True:
#     face_locations = face_recognition.face_locations(fname_path)
#     face_encodings = face_recognition.face_encodings(fname_path, face_locations)
#     face_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(fname_path, face_encoding)
#         name = "Unknown"
#         if True in matches:
#            first_match_index = matches.index(True)
#            name = fname_path[first_match_index]
