from tkinter import Tk, Canvas, Frame, BOTH, W


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Текст и Шрифт в Tkinter")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(
            20, 30, anchor=W, font="DejavuSansLight",
            text="Красное солнце сгорает дотла"
        )

        canvas.create_text(
            20, 60, anchor=W, font="Arial",
            text="На пылающий город падает тень"
        )

        canvas.create_text(
            20, 130, anchor=W, font="TimesNewRoman",
            text="Перемен!"
        )

        canvas.create_text(
            20, 160, anchor=W, font="ComicSans",
            text="Требуют наши сердца"
        )

        canvas.create_text(
            20, 190, anchor=W, font="FreeSerif",
            text="Перемен!"
        )

        canvas.create_text(
            20, 220, anchor=W, font="LatoThin",
            text="Требуют наши глаза"
        )

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("420x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()