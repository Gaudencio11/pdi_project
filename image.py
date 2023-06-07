import cv2, numpy, time

corrida_meio = cv2.imread("imagensTeste/corrida_meio.jpeg")

imageIn = corrida_meio


human_head_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_frontalface_default.xml')

grey = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY )

human_head = human_head_cascade.detectMultiScale(grey, 1.2, 5)

contador = 0

for (x,y,w,h) in human_head:
    print(x,y,w,h)
    contador += 1
    #codigo de Matson para identificar os rostos. dica : Usar um mapping rostost = {(id, coordenada), (id, coordenada)} 
    titulo = str(contador) + " Rosto"
    cv2.rectangle(imageIn, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.putText(imageIn, titulo, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

print("Rostos selecionados:")
time.sleep(5)

while True:
    cv2.imshow('Escolha o Rosto',imageIn)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

escolha = input("Selecione um rosto para não esconder: ")
#Código de Arley aqui pra borrar os rostos com as coordenadas 

cv2.imwrite("resultado/detectface3.jpg", imageIn) 

