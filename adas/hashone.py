import cv2
img = cv2.imread('/Users/swaroopmahendrashinde/Desktop/logo.png', 1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img= cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('/Users/swaroopmahendrashinde/Desktop/newlogo.png', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()