from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Панель инструментов")

        menubar = Menu(self.master)
        self.fileMenu = Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Выход", command=self.onExit)
        menubar.add_cascade(label="Файл", menu=self.fileMenu)

        toolbar = Frame(self.master, bd=1, relief=RAISED)

        self.img = Image.open("img/exit.png")
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Button(
            toolbar, image=eimg, relief=FLAT,
            command=self.quit
        )

        exitButton.image = eimg
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()