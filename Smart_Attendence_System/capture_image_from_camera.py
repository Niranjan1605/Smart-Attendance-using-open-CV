import cv2 as cv

cam = cv.VideoCapture(0)
# reading the input using the camera

inp = input('Enter person name  ')
# If image will detected without any error,
# show result
while(1): 
        result,image = cam.read()
        cv.imshow(inp, image)
        if cv.waitKey(0):
         cv.imwrite(inp+".png", image)
         print("image taken")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")
