import os
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

# Aquí se colocan los datos de la cuenta Imgur donde se subirán las imágenes

clientId = ''
clientSecret = ''
accessToken = ''
refreshToken = ''

client = ImgurClient(clientId, clientSecret, accessToken, refreshToken)

#path = r"C:\Users\DELL\Downloads\wetransfer_fcgv0511-jpg_2024-06-17_1927\nuevasImagenes\FCGV0512.jpg"

class imageUploader:
    def __init__(self, path):
        self.path = path

    

    def uploadImages(self):    
        try:
            images = os.listdir()

            user = client.get_account('me')
            for image in images:

                # print(f'Username: {user.url}')
                
                imagesPath = self.path + "/" + image
                print(imagesPath)
                client.upload_from_path(path=imagesPath, config=None, anon=False)

        except ImgurClientError as error:
            print(f'Mensaje: {error.error_message}')
            print(f'Estatus: {error.status_code}')