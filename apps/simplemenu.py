from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Простое меню")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Выход", command=self.onExit)
        menubar.add_cascade(label="Файл", menu=fileMenu)

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()