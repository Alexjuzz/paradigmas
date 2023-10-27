import tkinter as tk

class Field:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"  # Игрок, который делает текущий ход

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", height=7, width=12, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
        else:
            return  # Ячейка уже занята символом X или O

        # Проверьте, выиграл ли текущий игрок или ничья и обновите интерфейс, если это так
        if self.check_win() == self.current_player:
            print(f"Игрок {self.current_player} победил!")
            self.root.quit()
        elif self.check_draw():
            print("Ничья!")
            self.root.quit()

        # Поменяйте текущего игрока
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Проверьте, есть ли выигрышная комбинация
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return self.buttons[i][0]['text']
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return self.buttons[0][i]['text']
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return self.buttons[0][0]['text']
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return self.buttons[0][2]['text']
        return None

    def check_draw(self):
        # Проверьте, закончилась ли игра вничью
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    return False  # Есть хотя бы одна пустая ячейка
        return True

if __name__ == "__main__":
    root = tk.Tk()
    field = Field(root)
    root.mainloop()
