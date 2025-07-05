import customtkinter as ctk
from start import GetStarted
class Main:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("NUML Islamic Bank")
        self.window.geometry("900x500")
        self.window.resizable(False, False)
        GetStarted(self.window)
        self.window.mainloop()

if __name__ == "__main__":
    Main()
