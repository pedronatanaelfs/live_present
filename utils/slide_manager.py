from PIL import Image, ImageTk

class SlideManager:
    def __init__(self):
        self.slides = []
        self.current_index = 0

    def load_slides(self, slide_paths):
        """
        Carrega os slides a partir de uma lista de caminhos de arquivos.
        """
        self.slides = slide_paths
        self.current_index = 0

    def next_slide(self):
        """
        Avança para o próximo slide.
        """
        if self.slides:
            self.current_index = (self.current_index + 1) % len(self.slides)
        return self.get_current_slide()

    def prev_slide(self):
        """
        Volta para o slide anterior.
        """
        if self.slides:
            self.current_index = (self.current_index - 1) % len(self.slides)
        return self.get_current_slide()

    def get_current_slide(self):
        """
        Retorna o slide atual redimensionado e formatado para o Tkinter.
        """
        if not self.slides:
            return None
        img = Image.open(self.slides[self.current_index])
        img = img.resize((600, 400), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)
        return imgtk
