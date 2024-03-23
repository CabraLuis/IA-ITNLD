from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Abrir imagen
image = Image.open('image.bmp')
# Convertir pixeles de 8 bits
image_gr = image.convert('L')
# Obtener matriz de los pixeles
matrix = np.array(list(image_gr.getdata(band = 0 )), float)
# Definir tamano de matriz
matrix.shape = (image_gr.size[1], image_gr.size[0])

# Aplicar SVD con Numpy, obteniendo 3 matrices 
U, D, V = np.linalg.svd(matrix)
# La matriz D contiene los valores singulares de la imagen
# se usa para comprimir la imagen sin perder demasiada informacion.
# Para ello se trunca la matriz D, manteniendo solo los primeros k valores,
# k = 100, 50, 25, 10

print("Valores singulares originales: %s" % np.count_nonzero(D))

for i in [100, 50, 25, 10]:
    # Comprimir imagen modificando valores en D
    image_recons = np.matrix(U[:, 0:i]) * np.diag(D[0:i]) * np.matrix(V[0:i, :])
    # Mostrar imagen comprimida en blanco y negro
    plt.imshow(image_recons, cmap = 'gray')
    title = "Valores singulares = %s" % i
    plt.title(title)
    plt.show()