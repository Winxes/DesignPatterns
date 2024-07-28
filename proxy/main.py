from abc import ABC, abstractmethod

# Objeto Abstrato
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Imagem Real
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Simulacao do Client
image = ProxyImage("pfp.jpg")
image.display()  # Imagem sera carregada e exibida
image.display()  # Imagem sera apenas exibida
image.display()
image.display()
