import numpy as np
import cv2

img = cv2.imread('/Users/swaroopmahendrashinde/Desktop/football.png',0)
template = cv2.imread('/Users/swaroopmahendrashinde/Desktop/ball.png',0)

h, w = template.shape
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

annotated = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.rectangle(annotated, top_left, bottom_right, (0, 0, 255), 2)

print(f'Best match confidence: {max_val:.3f} at {top_left}')

cv2.imshow('Detected Object', annotated)
cv2.imshow('Matching Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
