import cv2
import numpy as np
import time
import datetime

# Inicializa a captura de vídeo
capture = cv2.VideoCapture(0)

# Inicializa o Background Subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Variáveis para rastrear o tempo desde o último movimento e a última data e hora de movimento
last_movement_time = None

while True:
    # Captura o quadro atual
    ret, frame = capture.read()
    if not ret:
        break

    # Aplica a máscara do fundo
    fgmask = fgbg.apply(frame)

    # Encontra os contornos na máscara
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verifica se há contornos significativos
    movement_detected = False
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Ajuste o valor conforme necessário
            # Desenha um retângulo ao redor do objeto em movimento
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            movement_detected = True

    # Atualiza o tempo desde o último movimento detectado
    current_time = time.time()
    if movement_detected:
        last_movement_time = current_time

    # Verifica se o alerta deve ser emitido
    if last_movement_time is not None:
        time_since_last_movement = current_time - last_movement_time
        if time_since_last_movement > 5:
            last_movement_datetime = datetime.datetime.now()
            print(f"Alerta: Não foi detectado movimento desde {last_movement_datetime}.")
            last_movement_time = None  # Reseta o tempo desde o último movimento

    # Exibe o quadro original e a máscara
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', fgmask)

    # Verifica se a tecla ESC foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera os recursos e fecha as janelas
capture.release()
cv2.destroyAllWindows()
