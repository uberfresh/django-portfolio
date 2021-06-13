import cv2

def get_filtered_image(image,action):
	img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	if action =='NO_FILTER':
		filtered = img
	elif action =='COLORIZED':
		filtered = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	return filtered