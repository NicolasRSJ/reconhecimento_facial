import cv2
import mediapipe as mp

#Inicializando o opencv e o mediapipe
webcam =  cv2.VideoCapture(0)
solucao_reconhecimento_facial = mp.solutions.face_detection
reconhecedor_facil = solucao_reconhecimento_facial.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Capturando informações da Webcam
    verificador, frame = webcam.read()

    if not verificador:
        break

    # Reconhecimento de rostos
    lista_rostos = reconhecedor_facil.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenho do rosto na imagem
            desenho.draw_detection(frame, rosto)
    cv2.imshow("Webcam", frame)

    # Manipulando apresentação da imagem
    if cv2.waitKey(5) == 27: # 27 é o código da tecla ESC.
        break

webcam.release()
