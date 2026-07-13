#Generating random colors in an image
import random
import cv2
img = cv2.imread('/Users/swaroopmahendrashinde/Desktop/images.png', -1)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Copy pasting a certain part of an image to another part of the same image
import cv2
import random
img = cv2.imread('/Users/swaroopmahendrashinde/Desktop/images.png', -1)
tag = img[50:150, 50:150]
img[200:300, 200:300] = tag
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()