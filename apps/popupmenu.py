from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Всплывающее меню")
        self.menu = Menu(self.master, tearoff=0)

        self.menu.add_command(label="Бип!", command=self.bell)
        self.menu.add_command(label="Выход", command=self.onExit)

        self.master.bind("<Button-3>", self.showMenu)
        self.pack()

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()