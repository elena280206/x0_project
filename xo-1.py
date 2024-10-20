print(" Игра Крестики-нолики для двух игроков: ")
board = list(range(1,10))
def draw(board):
    print("_" * 13)
    for i in range(3):
       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
       print("_" * 13)

def main(board):
    counter = 0
    flag = False
    while not flag:
        draw(board)
        if counter % 2 == 0:
            motion("X")
        else:
            motion("O")
        counter += 1
        if counter > 4:
            control = win_control(board)
            if control:
                print(control, "выиграл!")
                flag = True
                break
            if counter == 9:
                print("Ничья!")
                break
    draw(board)
main(board)
input("Нажмите Enter для выхода!")