import pygame
import random
def print_board(board, screen):
    screen.fill(BLUE)
    pygame.draw.line(screen, WHITE,
                     [0, 90],
                     [360, 90], 3)
    pygame.draw.line(screen, WHITE,
                     [0, 180],
                     [360, 180], 3)
    pygame.draw.line(screen, WHITE,
                     [0, 270],
                     [360, 270], 3)
    pygame.draw.line(screen, WHITE,
                     [90, 0],
                     [90, 360], 3)
    pygame.draw.line(screen, WHITE,
                     [180, 0],
                     [180, 360], 3)
    pygame.draw.line(screen, WHITE,
                     [270, 0],
                     [270, 360], 3)

    font = pygame.font.SysFont(None, 50)

    for row in range(4):
        for col in range(4):
            ch = str(board[row][col])
            if ch == "None":
                continue
            img = font.render(ch, True, WHITE)
            screen.blit(img, (90 * col + 30, 90 * row + 30))

    return screen


def swap(board, empty_pos, new_pos):
    board[empty_pos[0]][empty_pos[1]], board[new_pos[0]][new_pos[1]] = board[new_pos[0]][new_pos[1]], \
    board[empty_pos[0]][empty_pos[1]]


def get_empty_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] is None:
                return i, j


def make_move(board, moves, direction):
    move = moves[direction]
    empty_pos = get_empty_position(board)
    new_pos = (empty_pos[0] + move[0], empty_pos[1] + move[1])

    if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
        swap(board, empty_pos, new_pos)


def shuffle_board(board, moves, num_moves=100):
    for _ in range(num_moves):
        move = random.choice(list(moves.keys()))
        make_move(board, moves, move)


def is_solved(board):
    correct_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    return board == correct_board





WIDTH = 360
HEIGHT = 360

# Создаём игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пятнашки")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Цикл игры
running = True
board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, None]
]
moves = {
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1),
}

shuffle_board(board, moves, 200)

while running:
    screen = print_board(board, screen)
    if is_solved(board):
        font = pygame.font.SysFont(None, 50)
        screen.fill(BLUE)
        img = font.render("Вы победили!", True, RED)
        screen.blit(img, (30 + 30, 90 + 30))
    for event in pygame.event.get():



        # Проверка на закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w, pygame.K_UP]:
                make_move(board, moves, 'w')
            elif event.key in [pygame.K_s, pygame.K_DOWN]:
                make_move(board, moves, 's')
            elif event.key in [pygame.K_a, pygame.K_LEFT]:
                make_move(board, moves, 'a')
            elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                make_move(board, moves, 'd')
    # Рендеринг


    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()