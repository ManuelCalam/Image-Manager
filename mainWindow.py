import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from imageManager import *
from imageUploader import *

windowWidth = 500
windowHeight = 250 

imgManager = None
imgUploader = None

path = ""

def centerWindow(window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    pos_x = (screenWidth - windowWidth) // 2
    pos_y = (screenHeight - windowHeight) // 2

    window.geometry(f"{windowWidth}x{windowHeight}+{pos_x}+{pos_y}")


def getPath():
    global imgManager
    global imgUploader
    path = filedialog.askdirectory()
    if path != "":
        os.chdir(path)
        imgManager = imageManager(path)
        imgUploader = imageUploader(path)
    print(os.getcwd())
    pathTextField.delete(0, tk.END)
    pathTextField.insert(0, f"{path}")


def changeResWrapper():
    if imgManager is not None:
        try:
            width = int(widthTextField.get())
            height = int(heightTextField.get())
            imgManager.getRes(width, height)
            imgManager.changeResolution()
            # answer = messagebox.askyesno("Confirmacion", "Nueva carpeta creada ¿Quieres cambiar la ruta a la nueva carpeta?")
            # if answer:
            #     print
            # else:
            #     print
        except ValueError:
            print("Ingresa las dimensiones.")
    else:
        print("Selecciona una ruta.")


def uploadImagesWrapper():
    if imgUploader is not None:
        imgUploader.uploadImages()
    else:
        print("Selecciona una ruta.")


window = tk.Tk()
window.title("Image Manager")

pathLabel = tk.Label(window, text="Ruta: ", font=("", 11))
pathLabel.place(x=50, y=50)
pathTextField = tk.Entry(window, width=32, font=("", 10))
pathTextField.place(x=100, y=53)

selectPath_btn = tk.Button(window, text="Cambiar ruta", width=10, font=("", 11), command=getPath)
selectPath_btn.place(x=350, y=48)

widthTextField = tk.Entry(window, width=13, font=("", 10))
widthTextField.place(x= 50, y=100)
widthLabel = tk.Label(window, text="Ancho", font=("", 11))
widthLabel.place(x=50, y=125)

heightTextField = tk.Entry(window, width=13, font=("", 10))
heightTextField.place(x= 170, y=100)
heightLabel = tk.Label(window, text="Altura", font=("", 11))
heightLabel.place(x=170, y=125)

changeRes_btn = tk.Button(window, text="Redimensionar", width=15, font=("", 11), command=changeResWrapper)
changeRes_btn.place(x=304, y=95)

uploadImages_btn = tk.Button(window, text="Subir a Imgur", width=20, font=("", 11), command=uploadImagesWrapper)
uploadImages_btn.place(x=146, y=180)


centerWindow(window)
window.mainloop()


