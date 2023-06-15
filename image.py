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

lista_rostos = []

for (x,y,w,h) in human_head:
    print(x,y,w,h)
    contador += 1

    lista_rostos.append((contador,(x,y), (x+w, y+h)))

    #codigo de Matson para identificar os rostos. dica : Usar um mapping rostos = {(id, coordenada), (id, coordenada)} 
    titulo = " Rosto" + str(contador) 
    cv2.rectangle(imageIn, (x,y), (x+w, y+h), (255,0,0), 2) #Serve para criar os retângulos a partir das coordenadas
    cv2.putText(imageIn, titulo, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)#Serve para colocar texto ao lado dos retângulos

    

print(lista_rostos)

rosto_escolhido = int(input("Qual rosto você não quer borrar ?"))

    #eliminando pelo valor da array -1  
lista_rostos.pop(rosto_escolhido -1)

print(lista_rostos) 


time.sleep(2)

while True:
    cv2.imshow('Escolha o Rosto',imageIn) #Serve para exibir a imagem
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):  #Precione a tecla q para fechar a imagem
        break

cv2.destroyAllWindows()#fecha a imagem

for (x,y,w,h) in human_head:
    print(x,y,w,h)
    
   #Código de Arlley aqui pra borrar os rostos com as coordenadas, exeto o rosto escolhidos

    # Pecorrer as faces detectadas
    for (contador) in lista_rostos:
        # Recortar a região da face
        borrado = imageIn[y:y + h, x:x + w]

        # Aplicar o efeito de desfoque (blur) no rosto escolhido
        borrado = cv2.GaussianBlur(borrado, (55, 55), 15)

        # Substituir a região da face borrada pela imagem original
        imageIn[y:y + h, x:x + w] = borrado


#Exibir o resultado Final:
while True:
    cv2.imshow('Resultado Final: ',imageIn) 
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'): 
        break

cv2.destroyAllWindows()

cv2.imwrite("resultado/detectface3.jpg", imageIn) #salva a imagem

