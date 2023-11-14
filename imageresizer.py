# import cv2

# src = cv2.imread("arqam.jpg", cv2.IMREAD_UNCHANGED)

# #Percent by which the image is resized
# scale_percent = 50

# #Calculate the 50 percent of original dimensions
# new_width = int(src.shape[1] * scale_percent/100)
# new_height = int(src.shape[0] * scale_percent/100)

# #Resize image 
# output = cv2.resize(src, (new_width, new_height))

# cv2.imwrite('newimage.png', output)
# cv2.waitKey(0)  