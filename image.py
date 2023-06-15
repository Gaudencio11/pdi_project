import cv2, numpy, time

while True:

    print("""
    Bem vindo ao removedor de Faces (ou quase isso) automático!
    Basta escolher a imagem e o rosto, o resto fazemos para você
    """)


    #While para evitar erros do usuário
    while True:
        escolhaImagem = int(input("Escolha a imagem que você gostaria de testar (1, 2 ou 3): "))
        if(escolhaImagem < 1 or escolhaImagem > 3 ):
            print("Valor digitado inválido")
        else:
            break

    #Imagem de Entrada
    imageIn = cv2.imread(f"imagensTeste/people{escolhaImagem}.jpg")
    imageOut = cv2.imread(f"imagensTeste/people{escolhaImagem}.jpg")

    #"Inteligencia Artifical", eh essa variável que vai identificar os padrões 
    human_head_cascade = cv2.CascadeClassifier('xmlFiles/haarcascade_frontalface_default.xml')

    #TRansformamos para cinza, a fim de obter melhores resultados
    grey = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY )

    #Aqui ele armazena em human_head as coordenadas dos locais onde há rostos
    human_head = human_head_cascade.detectMultiScale(grey, 1.2, 5)

    contador = 0

    lista_rostos = []

    for (x,y,w,h) in human_head:
        contador += 1

        lista_rostos.append((x,y,w,h))

        #codigo de Matson para identificar os rostos. dica : Usar um mapping rostos = {(id, coordenada), (id, coordenada)} 
        titulo = str(contador) +" Rosto" 
        cv2.rectangle(imageIn, (x,y), (x+w, y+h), (255,0,0), 2) #Serve para criar os retângulos a partir das coordenadas
        cv2.putText(imageIn, titulo, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)#Serve para colocar texto ao lado dos retângulos

        
    print("Faces selecionadas:")
    time.sleep(2)



    while True:
        cv2.imshow('Faces selecionadas: (pressione q para sair)',imageIn) #Serve para exibir a imagem
        
        if (cv2.waitKey(1) & 0xFF) == ord('q'):  #Precione a tecla q para fechar a imagem
            cv2.destroyAllWindows()#fecha a imagem
            break

    #While para evitar erros do usuário
    while True:
        rosto_escolhido = int(input("Digite qual face você não quer esconder: "))
        if(rosto_escolhido > len(lista_rostos) or rosto_escolhido <= 0):
            print("Valor digitado inválido")
        else:
            break


    #eliminando pelo valor da array -1  
    lista_rostos.pop(rosto_escolhido -1)


    # Pecorrer as faces detectadas
    for (x,y,w,h) in lista_rostos:

        # Recortar a região da face
        borrado = imageOut[y:y + h, x:x + w]

        # Aplicar o efeito de desfoque (blur) no rosto escolhido
        borrado = cv2.GaussianBlur(borrado, (55, 55), 5)

        # Substituir a região da face borrada pela imagem original
        imageOut[y:y + h, x:x + w] = borrado


    #Exibir o resultado Final:
    while True:
        cv2.imshow('Resultado Final: (pressione q para sair)', imageOut) 
        
        if (cv2.waitKey(1) & 0xFF) == ord('q'): 
            cv2.destroyAllWindows()
            break


    cv2.imwrite(f"resultado/detectface{escolhaImagem}.jpg", imageOut) #salva a imagem
    print("Imagem Salva com Sucesso!!")

    if input("Gostaria de continuar no programa?(S/N) ").upper() == "N":
        break

print("Obrigado, volte sempre")