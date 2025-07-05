import customtkinter as ctk
from PIL import Image
from login_page import LoginPage
from signup_page import SignupPage

class GetStarted():
    def __init__(self, window):
        self.window = window
        self.window.title("Get Started - NUML Islamic Bank")
        self.window.geometry("900x500")
        self.initgui()

    def initgui(self):

        # Background Image
        image = Image.open('Images/start.jpg')
        bg_image = ctk.CTkImage(image, size = (900,500))
        label = ctk.CTkLabel(
            self.window,
            text='',
            image=bg_image
        )
        label.place(x=0,y=0)

        bank_name_label = ctk.CTkLabel(
            self.window,
            text='NUML Islamic Bank',
            text_color="white",
            fg_color='#151730',
            font=('Arial',40,'bold')
        )
        bank_name_label.place(x=20,y=150)

        slogan_label = ctk.CTkLabel(
            self.window,
            text='AP K DIL MN HAMARA ACCOUNT',
            text_color="WHITE",
            fg_color='#151730',
            font=('Arial', 20)
        )
        slogan_label.place(x=45, y=210)


        login_button = ctk.CTkButton(
            self.window,
            text = 'LOGIN',
            fg_color = "#2f477f",
            hover_color = "#201f54",
            text_color = 'White',
            cursor = "hand2",
            font = ("Arial", 20,'bold'),
            command = lambda: self.login_button_command()
        )
        login_button.place(x=60, y=300)

        signup_button = ctk.CTkButton(
            self.window,
            text='SIGN UP',
            fg_color="#2f477f",
            hover_color="#201f54",
            text_color='White',
            font=("Arial", 20,'bold'),
            command = lambda: self.signup_button_command()
        )
        signup_button.place(x=220, y=300)

    def login_button_command(self):
        LoginPage(self.window)

    def signup_button_command(self):
        SignupPage(self.window)