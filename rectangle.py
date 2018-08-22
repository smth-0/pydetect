import cv2

def main():
	cam = cv2.VideoCapture(0)
	while True:
		retval, img = cam.read()
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, 'QWERTY', (10, 200), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
		cv2.rectangle(img, (200, 200), (400, 400), (255, 255, 255), 3)
		cv2.imshow('Name', img)
		if cv2.waitKey(1) == 27:
			break

main()

