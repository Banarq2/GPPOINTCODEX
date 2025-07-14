import open3d as o3d
import os
import numpy as np

# Ruta relativa al archivo .ply dentro de la carpeta 'data'
nube_path = os.path.join("data", "mi_nube.ply")

# Cargar la nube
pcd = o3d.io.read_point_cloud(nube_path)

# Escalar si estuviera en metros
# pcd.scale(1000.0, center=(0, 0, 0))  # solo si es necesario

# Imprimir info básica
print(pcd)
print("Número de puntos:", np.asarray(pcd.points).shape[0])

# Visualizar
o3d.visualization.draw_geometries([pcd])
