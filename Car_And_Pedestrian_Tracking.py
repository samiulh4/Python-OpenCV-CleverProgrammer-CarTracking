from typing import DefaultDict
import cv2


"""
img_file = 'images/cars.jpg'
classifier_file = 'xmls/car_detector.xml'
car_tracker = cv2.CascadeClassifier(classifier_file)

img = cv2.imread(img_file)

#percent by which the image is resized
scale_percent = 50
#calculate the percent of original dimensions
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
# dsize
dsize = (width, height)
# resize image
img2 = cv2.resize(img, dsize)
#cv2.imwrite('D:/cv2-resize-image-50.png',output)


# Convert to Gray Scale
black_n_while = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(black_n_while)

#print(cars)


for (x, y, w, h) in cars:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow('Clever Programmer Car Detector', img2)
cv2.waitKey()


"""

video = cv2.VideoCapture('videos/v1.mp4')
classifier_file = 'xmls/car_detector.xml'
car_tracker = cv2.CascadeClassifier(classifier_file)


while True:
    (read_successful, frame) = video.read()
    if read_successful:
         grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break     
    cv2.imshow('Clever Programmer Car Detector', frame)
    key = cv2.waitKey(1)
    if key == 81 or key== 113:
        break    



print('Code Completed')