import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import subprocess
from utils.camera import start_camera, get_camera_frame, release_camera, find_active_cameras

# Variáveis globais
current_camera_index = 0  # Índice da câmera atual
cap = None
active_cameras = []  # Lista de câmeras ativas
slides_images = []  # Lista de imagens dos slides
current_slide_index = 0  # Índice do slide atual

# Função para alternar entre câmeras ativas
def switch_camera():
    global current_camera_index, cap
    release_camera(cap)  # Libera a câmera atual
    
    # Passa para o próximo índice de câmera disponível
    current_camera_index = (current_camera_index + 1) % len(active_cameras)
    
    # Inicializa a nova câmera
    cap = start_camera(active_cameras[current_camera_index])

    # Verifica se a câmera foi aberta corretamente
    if not cap or not cap.isOpened():
        current_camera_index = 0  # Se houver um problema, volta para a primeira câmera
        cap = start_camera(active_cameras[current_camera_index])

# Função para atualizar o feed da câmera
def update_camera_frame():
    frame = get_camera_frame(cap)
    if frame:
        camera_label.imgtk = frame
        camera_label.configure(image=frame)
    camera_label.after(10, update_camera_frame)

# Função para converter o arquivo .pptx em imagens usando LibreOffice
def pptx_to_images(pptx_path):
    # Define a pasta temporária para salvar os slides convertidos
    output_dir = os.path.join(os.getcwd(), "pptx_slides")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Caminho para o executável do LibreOffice (ajuste o caminho conforme necessário)
    libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

    # Comando para converter o arquivo .pptx para PNG usando LibreOffice
    convert_command = [
        libreoffice_path,
        "--headless",
        "--convert-to", "png",
        "--outdir", output_dir,
        pptx_path
    ]

    # Executa o comando de conversão
    print("Iniciando a conversão com LibreOffice...")
    subprocess.run(convert_command, check=True)
    print("Conversão concluída.")

    # Verifica e lista os arquivos PNG gerados
    slide_images = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".png")])
    print(f"Imagens dos slides geradas: {slide_images}")
    
    return slide_images

# Função para carregar um arquivo .pptx e exibir os slides
def load_pptx():
    global slides_images, current_slide_index
    pptx_path = filedialog.askopenfilename(filetypes=[("PowerPoint Files", "*.pptx")])
    
    if not pptx_path:
        print("Nenhum arquivo .pptx selecionado.")
        return
    
    # Converte o arquivo pptx em imagens
    slide_image_paths = pptx_to_images(pptx_path)
    
    if not slide_image_paths:
        print("Nenhuma imagem de slide foi gerada.")
        return
    
    # Carrega as imagens no formato correto para exibir no Tkinter
    slides_images = []
    for image_path in slide_image_paths:
        img = Image.open(image_path)
        img_resized = img.resize((600, 400), Image.ANTIALIAS)
        slides_images.append(ImageTk.PhotoImage(img_resized))
    
    print(f"Total de slides carregados: {len(slides_images)}")

    # Exibe o primeiro slide
    current_slide_index = 0
    update_slide()

# Função para atualizar o slide atual
def update_slide():
    global current_slide_index
    if slides_images:
        print(f"Exibindo slide {current_slide_index + 1} de {len(slides_images)}")
        slide_label.imgtk = slides_images[current_slide_index]
        slide_label.configure(image=slides_images[current_slide_index])

# Funções para navegação entre slides
def next_slide():
    global current_slide_index
    if slides_images:
        current_slide_index = (current_slide_index + 1) % len(slides_images)
        update_slide()

def prev_slide():
    global current_slide_index
    if slides_images:
        current_slide_index = (current_slide_index - 1) % len(slides_images)
        update_slide()

# Inicializa a janela principal
root = tk.Tk()
root.title("Apresentação com Câmera")
root.geometry("900x600")

# Encontra as câmeras ativas
active_cameras = find_active_cameras()
if not active_cameras:
    raise Exception("Nenhuma câmera ativa foi encontrada.")

# Inicializa a câmera com o primeiro índice ativo
current_camera_index = 0
cap = start_camera(active_cameras[current_camera_index])

# Label para a captura da câmera
camera_label = tk.Label(root)
camera_label.place(x=650, y=50, width=200, height=150)

# Label para exibir os slides
slide_label = tk.Label(root)
slide_label.place(x=20, y=50, width=600, height=400)

# Botões para carregar slides e navegar
load_button = tk.Button(root, text="Carregar .PPTX", command=load_pptx)
load_button.place(x=150, y=500)

prev_button = tk.Button(root, text="Anterior", command=prev_slide)
prev_button.place(x=250, y=500)

next_button = tk.Button(root, text="Próximo", command=next_slide)
next_button.place(x=350, y=500)

# Botão para alternar câmeras
switch_button = tk.Button(root, text="Trocar Câmera", command=switch_camera)
switch_button.place(x=450, y=500)

# Inicia o loop de captura da câmera
update_camera_frame()

# Inicia a interface gráfica
root.mainloop()

# Libera a câmera após fechar a aplicação
release_camera(cap)
