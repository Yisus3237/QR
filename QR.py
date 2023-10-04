import cv2
import numpy as np
import string
from pyzbar.pyzbar import decode
import Conexion

conexion = Conexion.conectar_bd()
cursor = conexion.cursor()
selectQuery = "SELECT QR FROM estudiante"
cursor.execute(selectQuery)
resultados = cursor.fetchall()
registered_qr_codes = [resultado[0] for resultado in resultados]
print(registered_qr_codes)

def decode_qr(frame):
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        qr = obj.data.decode('utf-8')
        print("Data: ", qr)
        print("Type: ", obj.type)
        x, y, w, h = obj.rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(obj.data), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Check if the QR code is registered or not
        if qr in registered_qr_codes:
            print("This QR code is registered.")
        else:
            print("This QR code is not registered.")

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = decode_qr(frame)
    cv2.imshow('QR Code Reader', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()