import cv2, numpy, time

#Imagem de Entrada
imageIn = cv2.imread("imagensTeste/corrida_meio.jpeg")

#"Inteligencia Artifical", eh essa variável que vai identificar os padrões 
human_head_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_frontalface_default.xml')

#TRansformamos para cinza, a fim de obter melhores resultados
grey = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY )

#Aqui ele armazena em human_head as coordenadas dos locais onde há rostos
human_head = human_head_cascade.detectMultiScale(grey, 1.2, 5)

contador = 0
for (x,y,w,h) in human_head:
    print(x,y,w,h)
    contador += 1
    #codigo de Matson para identificar os rostos. dica : Usar um mapping rostos = {(id, coordenada), (id, coordenada)} 
    titulo = str(contador) + " Rosto"
    cv2.rectangle(imageIn, (x,y), (x+w, y+h), (255,0,0), 2) #Serve para criar os retângulos a partir das coordenadas
    cv2.putText(imageIn, titulo, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)#Serve para colocar texto ao lado dos retângulos

print("Rostos selecionados:")
time.sleep(2)

while True:
    cv2.imshow('Escolha o Rosto',imageIn) #Serve para exibir a imagem
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):  #Precione a tecla q para fechar a imagem
        break

cv2.destroyAllWindows()#fecha a imagem


escolha = input("Selecione um rosto para não esconder: ")
for (x,y,w,h) in human_head:
    print(x,y,w,h)
    #Código de Arley aqui pra borrar os rostos com as coordenadas, exeto o rosto escolhido


#Exibir o resultado Final:
while True:
    cv2.imshow('REsultado Final: ',imageIn) 
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'): 
        break

cv2.destroyAllWindows()

cv2.imwrite("resultado/detectface3.jpg", imageIn) #salva a imagem

