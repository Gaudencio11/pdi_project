import cv2, numpy

corrida_inicio = cv2.imread("imagensTeste/corrida_inicio.jpeg")
corrida_meio = cv2.imread("imagensTeste/corrida_meio.jpeg")
todoCorpo = cv2.imread("imagensTeste/todo_corpo.jpeg")

imageIn = corrida_meio


human_head_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_frontalface_default.xml')

grey = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY )

human_head = human_head_cascade.detectMultiScale(grey, 1.2, 5)

contador = 0
for (x,y,w,h) in human_head:
    print(x,y,w,h)
    cv2.rectangle(imageIn, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.putText(imageIn, 'Rosto ', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)



cv2.imwrite("resultado/detectface3.jpg", imageIn) 

""" 
upper_human = human_upper_boddy_cascade.detectMultiScale(grey, 1.1, 1)
human = human_full_boddy_cascade.detectMultiScale(grey, 1.1, 1)
human_upper_boddy_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_upperbody.xml')
human_full_boddy_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_fullbody.xml') """