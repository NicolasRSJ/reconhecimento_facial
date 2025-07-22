Reconhecimento Facial em Tempo Real com OpenCV e MediaPipe
Este projeto utiliza a webcam do computador para detectar rostos em tempo real usando as bibliotecas OpenCV e MediaPipe.

Pré-requisitos
Antes de executar o código, instale as bibliotecas necessárias:

bash
Copiar
Editar
pip install opencv-python mediapipe
Como funciona?
A webcam é ativada e captura os frames em tempo real.

O MediaPipe processa cada frame para identificar rostos.

Caso algum rosto seja detectado, um retângulo é desenhado em volta dele.

O processo continua até que a tecla ESC seja pressionada para encerrar.

Como usar
Clone ou baixe este repositório.

Execute o script Python:

bash
Copiar
Editar
python seu_arquivo.py
Uma janela da webcam será aberta.

Pressione ESC para sair.

Código-fonte
python
Copiar
Editar
import cv2
import mediapipe as mp

# Inicializando o OpenCV e o MediaPipe
webcam = cv2.VideoCapture(0)
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

Observações
O código utiliza a câmera padrão do computador (cv2.VideoCapture(0)).
Caso não possua webcam, o código não irá funcionar corretamente.
Funciona melhor com boa iluminação.

