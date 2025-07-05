import customtkinter as ctk
from PIL import Image
from forgot_password import ForgotPassword
from Database import SupabaseBankApp
from first_page import MainPage
import webbrowser

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Page - NUML Islamic Bank")
        self.supabase = SupabaseBankApp()
        self.initgui()

    def initgui(self):
        # Setting left frame side
        self.left_frame = ctk.CTkFrame(
            self.window,
            width=370,
            height=500,
            fg_color="white",
            corner_radius=0
        )
        self.left_frame.place(x=0, y=0)

        # Apply logo
        logo_image = Image.open("Images/numl-logo.png")
        logo_photo = ctk.CTkImage(logo_image, size=(50, 50))
        logo_label = ctk.CTkLabel(
            self.left_frame,
            image=logo_photo,
            text="",
            fg_color="white")
        logo_label.place(x=20, y=20)

        # Bank Name
        bank_name_label = ctk.CTkLabel(
            self.left_frame,
            text="NUML Islamic Bank",
            font=("Arial", 28, "bold"),
            text_color="#2f477f")
        bank_name_label.place(x=78, y=29)

        # Welcome Back Label
        welcome_back_label = ctk.CTkLabel(
            self.left_frame,
            text="Welcome Back!",
            font=("Arial", 24, "bold"),
            text_color="#201f54"
        )
        welcome_back_label.place(x=40, y=110)

        # Username Label
        username_label = ctk.CTkLabel(
            self.left_frame,
            text="Username",
            font=("Arial", 14),
            text_color="black"
        )
        username_label.place(x=40, y=165)

        # Username Entry
        self.username_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter your username",
            width=300,
        )
        self.username_entry.place(x=40, y=195)

        # Password Label
        password_label = ctk.CTkLabel(
            self.left_frame,
            text="Password",
            font=("Arial", 14),
            text_color="black"
        )
        password_label.place(x=40, y=240)

        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter your password",
            show="●",
            width=300,
        )
        self.password_entry.place(x=40, y=270)

        # Forgot Password Label
        forgot_password_label = ctk.CTkButton(
            self.left_frame,
            text="Forgot Password?",
            font=("Arial", 12),
            text_color="#2f477f",
            fg_color="white",
            width=0,
            height=0,
            hover_color="white",
            cursor="hand2",
            command = lambda: self.forgot_password_button_command()
        )
        forgot_password_label.place(x=232, y=314)

        # Login Button
        login_button = ctk.CTkButton(
            self.left_frame,
            text="Login",
            fg_color="#2f477f",
            hover_color="#201f54",
            cursor="hand2",
            font=("Arial", 12, "bold"),
            width=300,
            command = lambda: self.login_button_command(self.username_entry.get(), self.password_entry.get())
        )
        login_button.place(x=40, y=350)

        # Warning
        warning_text = ctk.CTkLabel(
            self.left_frame,
            text="Warning! NUML Islamic Bank does not require\ninstallation of additional software.",
            font=("Arial", 10),
            text_color="gray"
        )
        warning_text.place(x=40, y=420)

        # More Button
        more_button = ctk.CTkButton(
            self.left_frame,
            text="MORE",
            width=70,
            fg_color="gray",
            hover_color="#525252",
            font=("Arial", 10, "bold"),
            command = lambda: self.more_button_command()
        )
        more_button.place(x=270, y=420)

        # Right Side Image
        bg_Image = Image.open("Images/Login_image.jpg")
        bg_Photo = ctk.CTkImage(bg_Image, size=(530, 500))
        bg_Label = ctk.CTkLabel(
            self.window,
            image=bg_Photo,
            text="",
            corner_radius=0
        )
        bg_Label.place(x=370, y=0)

    # Log in functionality
    def login_button_command(self, username, password):
        response = self.supabase.login(username, password)
        if response["status"] == "success":
            acc_balance = response['account_details']['account_balance']
            acc_name = response['account_details']['account_name']
            acc_num = response['account_details']['account_number']
            MainPage(self.window, acc_name, acc_num, acc_balance)
        else:
            error_label = ctk.CTkLabel(
                self.left_frame,
                text = "Invalid username or password.",
                text_color = "red",
                font = ("Arial", 14)
            )
            error_label.place(x = 100, y = 380)

    # Forgot password Functionality
    def forgot_password_button_command(self):
        ForgotPassword(self.window)

    # More button functionality
    def more_button_command(self):
        webbrowser.open("https://askaribank.com/services/alternate-delivery-channels/privacy-policy/")