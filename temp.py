import cv2

image = cv2.imread("pages/page_3.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for x in gray:
    print(list(x))
