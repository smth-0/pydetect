import cv2

def diflist(a, b):
	c =  []
	c.append(abs(a[0] - b[0]))
	c.append(abs(a[1] - b[1]))
	c.append(abs(a[2] - b[2]))
	return sum(c)




def main(x1, y1, x2, y2):
	colours = [[100, 190, 100], [50, 130, 210], [60, 160, 130], [210, 70, 70], [170, 115, 60], [75, 75, 240]]
	cam = cv2.VideoCapture(0)
	while True:
		retval, img = cam.read()
		cv2.imshow('Camera', img)
		R = []
		G = []
		B = []
		for i in range(x1, x2):
			for k  in range(y1, y2):
				R.append(img[i][k][2]) 
				G.append(img[i][k][1])
				B.append(img[i][k][0])
		meanR = sum(R) // len(R)
		meanG = sum(G) // len(G)
		meanB = sum(B) // len(B)
		RGB = [meanR, meanG, meanB]
		printcolour = str(meanR) + '  ' + str(meanG) + '  ' + str(meanB)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, printcolour, (5, 20), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
		cv2.rectangle(img, (x1, y1), (x2, y2),  (255, 0, 0), 2)
		cv2.imshow('Camera', img)
		minimum = 1000
		answer = 90
		for i in range(len(colours)):
			if minimum > diflist(RGB, colours[i]):
				minimum = diflist(RGB, colours[i])
				answer = i
		print(answer)
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()


if __name__ == '__main__':
	x1, y1 = map(int, input().split()) 
	x2, y2 = map(int, input().split())
	main(x1, y1, x2, y2)
