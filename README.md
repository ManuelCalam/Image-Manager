1. Ingresar a: https://api.imgur.com/oauth2/addclient rellenar y envíar el formulario y te redirigirá a una página donde se copiará el Client ID y el Client Secret
2. Ingresar a: https://api.imgur.com/oauth2/authorize?client_id=CLIENT ID AQUÍ&response_type=token e ingresar el clientId copiado, dar click en el botón "Allow" lo un que
   abrirá un enlace como este:
   https://www.postman.com/oauth2/callback/#access_token=ACCESS TOKEN AQUÍ&expires_in=315360000&token_type=bearer&refresh_token=REFRESH TOKEN ACÁ&account_username=TUUSUARIO&account_id=USUARIOID
   y copiar el access token y el refresh token, todos estos datos pegarlos en imageUploader.py
   

