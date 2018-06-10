# Based on https://github.com/ageitgey/face_recognition
import urllib
import webbrowser

import cv2
import face_recognition
from firebase import firebase

# TODOs:
# - Create a cached version of firebase to link of the customer

video_capture = cv2.VideoCapture(0)

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

# pull images from db and train them
fb = firebase.FirebaseApplication('https://adidas-hack-amsterdam-2018.firebaseio.com/', None)
known_customers = fb.get('/users', None)
for user, val in known_customers.items():
    # Load a sample picture and learn how to recognize it.
    picture_url = val['picture']
    img_location = "/tmp/" + user + ".jpg"
    urllib.urlretrieve(picture_url, img_location)
    training_image = face_recognition.load_image_file(img_location)
    trained_face_encoding = face_recognition.face_encodings(training_image)[0]
    known_face_encodings.append(trained_face_encoding)
    known_face_names.append(user)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    # Display the resulting image
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if top <= y <= bottom and left <= x <= right:
                if name is not 'Unknown':
                    webbrowser.open('http://48217499.ngrok.io?name=' + name)


    cv2.imshow('Video', frame)
    cv2.setMouseCallback('Video', click_event)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
