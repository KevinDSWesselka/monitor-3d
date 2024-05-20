<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Monitor de Movimento de Impressora 3D</h1>
Este é um projeto de monitoramento de movimento para uma impressora 3D usando uma câmera. O objetivo é detectar quando não há movimento na área da impressora 3D por um determinado período de tempo e enviar um alerta.

<h2>Funcionalidades Implementadas até o Momento</h2>
Detecção de Movimento: O programa é capaz de capturar vídeo da câmera, aplicar um algoritmo de subtração de fundo para detectar movimento na área monitorada.

Alerta de Falta de Movimento: Quando não é detectado movimento por mais de 5 segundos, o programa emite um alerta, indicando a data e hora da última detecção de movimento.

Exibição Visual: Além dos alertas, o programa exibe visualmente o vídeo da câmera e a máscara de movimento em uma janela.

Requisitos:
Python 3.x
OpenCV
NumPy

Instale as dependências:

Copiar código
pip install opencv-python numpy
Execute o script monitor_3d_printer.py:

Copiar código
python monitor_3d_printer.py
A câmera será ativada e o programa começará a monitorar a área. Se não for detectado movimento por mais de 5 segundos, um alerta será emitido, mostrando a data e hora da última detecção de movimento.

Pressione a tecla ESC para sair do programa.

<h2>Próximos Passos</h2>
Integração MQTT: Implementar a integração com um servidor MQTT para enviar alertas para dispositivos externos.
Melhorias na Detecção de Movimento: Refinar o algoritmo de detecção de movimento para uma melhor precisão.
Interface Gráfica de Usuário: Desenvolver uma interface gráfica para facilitar a interação com o programa.<p/><br>
 <b>By: Kevin D.S. Wesselka</b>
</html>
