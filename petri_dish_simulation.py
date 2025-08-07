import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensões da grade
GRID_SIZE = 250
# Número de gerações
GENERATIONS = 200
# Probabilidade de célula inicial estar viva (densidade)
INITIAL_DENSITY = 0.2

def inicializar_grade(tamanho, densidade):
    """Cria uma grade inicial com células vivas aleatórias."""
    return np.random.choice([0, 1], size=(tamanho, tamanho), p=[1 - densidade, densidade])

def contar_vizinhos(grade, x, y):
    """Conta os vizinhos vivos de uma célula na posição (x, y)."""
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            total += grade[(x + i) % GRID_SIZE][(y + j) % GRID_SIZE]
    return total

def atualizar_grade(grade):
    """Aplica as regras do Jogo da Vida e retorna a nova geração."""
    nova_grade = np.copy(grade)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            vizinhos = contar_vizinhos(grade, x, y)
            if grade[x][y] == 1:
                if vizinhos < 2 or vizinhos > 3:
                    nova_grade[x][y] = 0  # Morre
            else:
                if vizinhos == 3:
                    nova_grade[x][y] = 1  # Nasce
    return nova_grade

def atualizar_frame(frameNum, img, grade):
    """Função chamada a cada frame da animação."""
    nova = atualizar_grade(grade[0])
    img.set_data(nova)
    grade[0][:] = nova[:]
    return img,

def executar_simulacao():
    """Executa a simulação com visualização."""
    grade_inicial = inicializar_grade(GRID_SIZE, INITIAL_DENSITY)
    fig, ax = plt.subplots()
    img = ax.imshow(grade_inicial, interpolation='nearest', cmap='Greys')
    ani = animation.FuncAnimation(fig, atualizar_frame, fargs=(img, [grade_inicial]),
                                  frames=GENERATIONS, interval=200, save_count=50)
    plt.title("Simulação de Crescimento Bacteriano (Jogo da Vida)")
    plt.show()

if __name__ == "__main__":
    executar_simulacao()