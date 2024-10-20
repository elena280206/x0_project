def motion(cell):
    flag = False
    while not flag:
        answer = input("Выберите клетку и походите " + cell + ": ")
        try:
            answer = int(answer)
        except:
            print("Ошибка, введите число")
            continue
        if answer >= 1 and answer <= 9:
            if(str(board[answer - 1]) not in "XO"):
                board[answer - 1] = cell
                flag = True
        else:
            print("Выберите другую клетку!")
    else:
        print("Введите число от 1 до 9.")
def win_control(board):
    win_combinations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for number in win_combinations:
        if board[number[0]] == board[number[1]] == board[number[2]]:
          return board[number[0]]
    return False

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