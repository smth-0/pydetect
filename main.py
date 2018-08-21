import cv2

def diflist(a, b):
	c =  []
	c.append(abs(a[0] - b[0]))
        c.append(abs(a[1] - b[1]))
	c.append(abs(a[2] - b[2]))
	return sum(c)


def main(a, b, c):
	colours = [[100, 190, 100], [50, 130, 210], [60, 160, 130], [210, 70, 70], [170, 115, 60], [75, 75, 240]]
	cam = cv2.VideoCapture(0)
	while True:
		retval, img = cam.read()
		cv2.imshow('Camera', img)
		cv2.rectangle(img, (300, 300), (350, 350), (255, 0, 0), 4)
		R = []
		G = []
		B = []
		for i in range(a, b):
			for k  in range(a, c):
				R.append(img[i][k][2]) 
				G.append(img[i][k][1])
			        B.append(img[i][k][0])
		meanR = sum(R) // len(R)
		meanG = sum(G) // len(G)
		meanB = sum(B) // len(B)
		RGB = [meanR, meanG, meanB]
		minimum = 1000
		answer = 90
		for i in range(len(colours)):
			if minimum > diflist(RGB, colours[i]):
				minimum = diflist(RGB, colours[i])
				answer = i
		print[answer]
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	c = int(input())
	main(a, b, c)
