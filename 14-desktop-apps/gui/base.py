import tkinter
from gui.frames import PizzaListFrame


class Application:
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.geometry('1000x800')
        self._window.winfo_toplevel().title('DESKTOP-APP')

    def _draw(self):
        pizza_list_frame = PizzaListFrame(self._window)
        pizza_list_frame.draw()
        pizza_list_frame.pack(side=tkinter.TOP)

    def run(self):
        self._draw()
        self._window.mainloop()
