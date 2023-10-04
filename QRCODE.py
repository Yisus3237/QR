import qrcode
from PIL import Image
import random
import string
import time
import Conexion

def generate_random_token():
    conexion = Conexion.conectar_bd()
    cursor = conexion.cursor()
    #selectQuery = "SELECT * FROM estudiante WHERE Identificacion = %s"
    updateQuery = "UPDATE estudiante SET QR = %s WHERE Identificacion = %s"
    #cursor.execute(selectQuery, ('1001940173'))
    #resultados = cursor.fetchall()
    characters = string.ascii_letters + string.digits + string.punctuation + "!#$%&'*+-.^_`|~:"
    random_token = ''.join(random.choice(characters) for i in range(40))
    cursor.execute(updateQuery, (random_token, '1001940173'))
    conexion.commit()
    print("Token saved successfully:", random_token)
    return random_token

def create_qr_code(random_token):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(random_token)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def add_logo(qr_code_img, logo_path):
    logo = Image.open(logo_path)
    logo_size = 50
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    position = ((qr_code_img.size[0] - logo_size) // 2, (qr_code_img.size[1] - logo_size) // 2)
    qr_code_img.paste(logo, position)
    return qr_code_img

def main():
    while True:
        random_token = generate_random_token()
        qr_code_img = create_qr_code(random_token)
        logo_path = "img\Img.jpeg"
        qr_code_img = add_logo(qr_code_img, logo_path)
        qr_code_img.save("img\QR.png")
        time.sleep(3)
        
if __name__ == "__main__":
    main()