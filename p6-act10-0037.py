import numpy as np
import cv2
# Vision Artificial Act10 NC 0037
# Lee la imagen en escala de grises
img = cv2.imread("btSS.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea 
print(" La linea 0037")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen 
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Circulos 0037")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen 
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Texto 0037")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "young forever", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

# Abre la ventana con la imagen 
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Trackbars 0037")
def on_trackbar(val):
  print(val)

# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('btSS 0037')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R','btSS 0037',0,255,on_trackbar)
cv2.createTrackbar('G','btSS 0037',0,255,on_trackbar)
cv2.createTrackbar('B','btSS 0037',0,255,on_trackbar)

while(True):
    cv2.imshow('btSS 0037',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R','btSS 0037')
    g = cv2.getTrackbarPos('G','btSS 0037')
    b = cv2.getTrackbarPos('B','btSS 0037')

    img[:] = [b,g,r]

# Abre la ventana con la imagen 
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Thresholding 0037")
# Cargar la imagen en escala de grises (0)
img = cv2.imread('btSS.jpg', 0)

# Verificar que la imagen se haya cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen 'image1.png'. Verifica que esté en la misma carpeta del script.")
else:
    # Aplicar los diferentes tipos de umbralizado (thresholding)
    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    # Mostrar la imagen original y los resultados
    cv2.imshow('Original', img)
    cv2.imshow('BINARY', thr1)
    cv2.imshow('BINARY_INV', thr2)
    cv2.imshow('TRUNC', thr3)
    cv2.imshow('TOZERO', thr4)
    cv2.imshow('TOZERO_INV', thr5)
# Abre la ventana con la imagen 
cv2.imshow("btSS 0037", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Programa realizado por Angela Correa NC = 0037")