import numpy as np
import matplotlib.pyplot as plt

# Определяем координаты вершин пирамиды
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [0, 1, 0],
                     [1, 1, 0],
                     [0.5, 0.5, 1]])

# Определяем список граней пирамиды
faces = [[0, 1, 3, 2],
         [0, 1, 4],
         [1, 3, 4],
         [3, 2, 4],
         [2, 0, 4]]

# Функция для визуализации пирамиды


def plot_pyramid(vertices, faces, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        x = [vertices[vertex][0] for vertex in face]
        y = [vertices[vertex][1] for vertex in face]
        z = [vertices[vertex][2] for vertex in face]
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    plt.show()


# Визуализация исходной пирамиды
plot_pyramid(vertices, faces, "Пирамида")
