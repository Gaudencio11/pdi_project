import cv2, numpy

imageIn = cv2.imread("praia.jpeg")
videoIN = cv2.VideoCapture("quadriciculo.mp4")

frame_width = int(videoIN.get(3))
frame_height = int(videoIN.get(4))
fps = videoIN.get(cv2.CAP_PROP_FPS)

videoOUT = cv2.VideoWriter("resultado/teste.avi", cv2.VideoWriter_fourcc('M','J','P','G'),fps, (frame_width,frame_height))

#videoOUT = cv2.VideoWriter("resultado/teste.mp4", cv2.VideoWriter_fourcc(*'MP4V'),fps, (frame_width,frame_height))

success, image = videoIN.read()
count = 1

height = image.shape[0]
width = image.shape[1]


print(frame_width)
print(frame_height)

while success and count<600:
    success, image = videoIN.read()

    
    """ for i in range(0,frame_height-1):
        for j in range(0,frame_width-1):
            rgb = image[i][j]
            vermelho = int(rgb[0])
            verde = int(rgb[1])
            azul = int(rgb[2])
            soma =  vermelho + verde + azul
            media = soma/3
            image[i][j] = [media,media,media] """
    if success :
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
        videoOUT.write(gray)
        count +=1
print(count)


""" height = imageIn.shape[0]
width = imageIn.shape[1]

for i in range(0,height-1):
    for j in range(0,width-1):
        rgb = imageIn[i][j]
        vermelho = int(rgb[0])
        verde = int(rgb[1])
        azul = int(rgb[2])
        soma = 0
        soma =  vermelho + verde + azul
        media = soma/3
        imageIn[i][j] = [media,media,media]

cv2.imwrite("resultado/blackWhiteImage.jpg", imageIn)  """


"""
height = imageIn.shape[0]
width = imageIn.shape[1]

 for i in range(0,height-1):
    for j in range(0,width-1):
        rgb = imageIn[i][j]
        vermelho = int(rgb[0])
        verde = int(rgb[1])
        azul = int(rgb[2])
        soma = 0
        soma =  vermelho + verde + azul
        media = soma/3
        imageIn[i][j] = [media,media,media] """