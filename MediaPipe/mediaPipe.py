import cv2 as cv
import mediapipe as mp

cap=cv.VideoCapture(0)

mp_drawing= mp.solutions.drawing_utils
mp_holistic= mp.solutions.holistic

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame= cap.read()
        frame=cv.flip(frame, 1)
        
        # Recolor the feed
        img= cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Make the detections
        results=holistic.process(img)

        # Recolor the feed back to BGR
        img=cv.cvtColor(img, cv.COLOR_RGB2BGR)

        # Draw Face Landmarks
        #mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

        # Draw Right Hand Landmarks
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Draw Left Hand Landmarks
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Pose Detection
        #mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv.imshow('Raw feed', img)

        if cv.waitKey(1)== ord('q'):
            break

cap.release()
cv.destroyAllWindows()