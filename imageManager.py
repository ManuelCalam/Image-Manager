import os
import shutil
from PIL import Image



class imageManager:

    def __init__(self, path):
        self.path = path

    def getRes(self, width, height):
        self.width = width
        self.height = height

        print(f"Ancho y alto recibidos: Width: {self.width} y Height: {self.height}")


    def changeResolution(self):

        #os.chdir(self.path)

        images = os.listdir()
        newFileName = "nuevasImagenes"

        try:
            os.mkdir(newFileName)
            os.chdir(os.path.join(self.path, newFileName))
        except FileExistsError:
            shutil.rmtree(newFileName)
            os.mkdir(newFileName)   
            os.chdir(os.path.join(self.path, newFileName))


        for image in images:
            try:
                image_container = Image.open(os.path.join(self.path, image))
                image_container = image_container.resize((self.width, self.height))

                image_container.save(image, image_container.format)
                image_container.close()
                print(f"Se cambió el tamaño de {image}")
            except Exception as error:
                print(f"{image} no se puede modificar. Error {error}")

        os.chdir(self.path)
