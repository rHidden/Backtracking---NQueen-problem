from tkinter import *
import tkinter.simpledialog as simpledialog


class NQueen():
    def __init__(self, chessboard, count, N):
        self.chessboard = chessboard
        self.count = count
        self.N = N

    def isFree(self, chessboard, row, column): 

        for i in range(column): 
            if chessboard[row][i] == "Q": 
                return False

        for i, j in zip(range(row, -1, -1), range(column, -1, -1)): 
            if chessboard[i][j] == "Q": 
                return False

        for i, j in zip(range(row, self.N, 1), range(column, -1, -1)): 
            if chessboard[i][j] == "Q": 
                return False
  
        return True
  

    def search(self, chessboard, column): 
        if column == self.N: 
            return True

        for i in range(self.N): 
            if self.isFree(chessboard, i, column): 
                chessboard[i][column] = "Q"

                if self.search(chessboard, column + 1) == True and self.count!=-999: 
                    self.count += 1
                    if self.count == -999:
                        size=((2+N)*50)
                        can = Canvas(width=size, height=size)
                        background = PhotoImage(file = 'pozadie.png')
                        chess_queen_image = PhotoImage(file='chess_queen.png')
                        can.create_image(size/2, size/2, image=background)

                        color="white"
                        can.create_rectangle(48,48,size-48,size-48, outline="white", width=7)
                        can.create_rectangle(47,47,size-47,size-47, outline="black", width=3)
                        for i in range(N):
                            for j in range(N):
                                if (j+i) % 2 == 0:
                                    color="white"
                                if (j+i) % 2 == 1:
                                    color="black"
                                can.create_rectangle(i * 50 + 50, j * 50 + 50 , i * 50 + 100, j * 50 + 100, outline = "black", fill = color)
                                if chessboard[i][j]=="Q":
                                    can.create_image(i * 50 + 75, j * 50 + 75, image = chess_queen_image)

                        can.pack()
                        can.mainloop()

                    if self.count > -1000 and self.count != -999:
                        self.draw(chessboard)

                chessboard[i][column] = "I"
  
        if self.count==0:
            return False

  

    def draw(self, chessboard): 
        for i in range(self.N): 
            print(chessboard[i]) 
        print("\n")

    def solve(self):
        if self.search(self.chessboard,0) == False:
            print("Nonexistent solutions for N =",N)
        
        print(self.count, "total solutions", "\n")
        self.draw()

    def draw(self):
        self.count = -1000
        self.search(self.chessboard,0)


root = Tk()
root.withdraw()
N = simpledialog.askinteger("Input", "Enter resolution of chessboard and number of queens")
root.destroy()
chessboard = [["I" for i in range(N)] for j in range(N)]
count = 0

solution=NQueen(chessboard, count, N)
solution.solve()
