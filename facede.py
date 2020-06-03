from face_detector import FaceDetector

img_addr = "image.jpeg"

# First parameter in FaceDetector constructor specifies face detection method (dlib: fl_5 or fl_68, mtcnn is default: mtcnn)
face_detector = FaceDetector()
faces = face_detector.get_faces(img_addr)

# Or to get the most prominent face in photo
main_face = face_detector.get_main_face(img_addr)

# Show image with bounding boxes and landmarks
import cv2
img = cv2.imread(img_addr)

for face in faces:
    bb = face.bounding_box
    landmarks = face.landmarks
    cv2.rectangle(img, (int(bb.x), int(bb.y)), (int(bb.x + bb.w), int(bb.y+bb.h)), (0, 255, 0), 1)
    for l in landmarks:
        cv2.circle(img, (l.x, l.y), 2, (0,0,255))

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()