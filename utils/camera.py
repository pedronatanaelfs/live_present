import cv2
from PIL import Image, ImageTk

def start_camera(camera_index=0):
    """
    Inicializa a câmera com o índice fornecido e retorna o objeto VideoCapture.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        return None
    return cap

def get_camera_frame(cap):
    """
    Captura um frame da câmera e o converte para um formato compatível com o Tkinter.
    """
    ret, frame = cap.read()
    if ret:
        # Converte a imagem de BGR (OpenCV) para RGB (Tkinter)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        return imgtk
    return None

def release_camera(cap):
    """
    Libera o recurso da câmera após o uso.
    """
    if cap:
        cap.release()

def find_active_cameras(max_cameras=10):
    """
    Procura por câmeras ativas, testando índices de 0 até max_cameras.
    Retorna uma lista dos índices das câmeras que estão ativas.
    """
    active_cameras = []
    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            active_cameras.append(index)
        cap.release()
    return active_cameras
