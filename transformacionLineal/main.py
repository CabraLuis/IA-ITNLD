import cv2

img = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
# img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)

rows,cols=img.shape
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow("Rotacion de 90 grados",img_cw_180)
cv2.imshow("Rotacion de 180 grados",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()