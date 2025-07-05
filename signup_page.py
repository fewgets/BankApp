import customtkinter as ctk
from PIL import Image
from login_page import LoginPage
import webbrowser
from Database import SupabaseBankApp

class SignupPage:
    def __init__(self, window):
        self.supabase = SupabaseBankApp()
        self.window = window
        self.window.title("Signup Page - NUML Islamic Bank")
        self.initgui()

    def initgui(self):

        left_frame = ctk.CTkFrame(
            self.window,
            fg_color = "white",
            width = 530,
            height = 500
        )
        left_frame.place(x = 0, y = 0)
        # Setting Image on Left side
        bg_image = Image.open("Images/numl-logo.png")
        bg_photo = ctk.CTkImage(bg_image, size=(320, 320))
        bg_label = ctk.CTkLabel(
            left_frame,
            image = bg_photo,
            text=""
        )
        bg_label.place(x=100, y=70)

        # Label of NUML ISLAMIC Bank
        bank_name_logo = ctk.CTkLabel(
            left_frame,
            text = "NUML ISLAMIC BANK",
            font = ("Arial", 32, "bold"),
            text_color = "#201f54"
        )
        bank_name_logo.place(x=100, y=400)

        # Setting frame for right side
        right_frame = ctk.CTkFrame(
            self.window,
            width = 370,
            height = 500,
            fg_color = "white",
        )
        right_frame.place(x=530, y=0)

        # "Let's" Label
        let_s_label = ctk.CTkLabel(
            right_frame,
            text = "Let's",
            font = ("Arial", 24),
            text_color = "black"
        )
        let_s_label.place(x = 35, y = 3)

        # "Get Started" Label
        get_started_label = ctk.CTkLabel(
            right_frame,
            text = "Get Started",
            font = ("Arial", 24, "bold"),
            text_color = "#1d1b94"
        )
        get_started_label.place(x = 95, y = 3)

        # "Provide Info" Label
        provide_info_label = ctk.CTkLabel(
            right_frame,
            text = "Provide Following Information To",
            font = ("Arial", 12),
            text_color = "black"
        )
        provide_info_label.place(x = 35, y = 28)

        # SignUp Label in second line
        signup_label_2 = ctk.CTkLabel(
            right_frame,
            text = "Signup!",
            font = ("Arial", 12, "bold"),
            text_color = "#201f54"
        )
        signup_label_2.place(x = 214, y = 28)

        # Acount Number label
        account_number_label = ctk.CTkLabel(
            right_frame,
            text = "Account Number",
            font = ("Arial", 14),
            text_color = "black"
        )
        account_number_label.place(x = 40, y = 52)

        # Account Number Entry
        account_number_entry = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter your account number",
            width = 300,
            font = ("Arial", 14)
        )
        account_number_entry.place(x = 40, y = 75)

        # Account Name label
        account_name_label = ctk.CTkLabel(
            right_frame,
            text = "Account Name",
            font = ("Arial", 14),
            text_color = "black"
        )
        account_name_label.place(x = 40, y = 107)

        # Account Name Entry
        account_name_entry = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter your account name",
            width = 300,
            font = ("Arial", 14)
        )
        account_name_entry.place(x = 40, y = 130)

        # Contact Label
        contact_label = ctk.CTkLabel(
            right_frame,
            text = "Contact",
            font = ("Arial", 14),
            text_color = "black"
        )
        contact_label.place(x = 40, y = 162)

        # contact Entry
        contact_entry = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter your contact number",
            width = 300,
            font = ("Arial", 14),
        )
        contact_entry.place(x = 40, y = 185)

        # User Id Label
        user_id_label = ctk.CTkLabel(
            right_frame,
            text = "User Id",
            font = ("Arial", 14),
            text_color = "black"
        )
        user_id_label.place(x = 40, y = 217)

        # User Id Entry
        user_id_entry = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter unique user id",
            width = 300,
            font = ("Arial", 14)
        )
        user_id_entry.place(x = 40, y = 240)

        # Password label
        password_label = ctk.CTkLabel(
            right_frame,
            text = "Password",
            font = ("Arial", 14),
            text_color = "black"
        )
        password_label.place(x = 40, y = 272)

        # Password Entry
        password_enrty = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter a strong password",
            width = 300,
            font = ("Arial", 14),
            show = "●"
        )
        password_enrty.place(x = 40, y = 295)

        # secret word Label
        secret_name_label = ctk.CTkLabel(
            right_frame,
            text = "Enter a secret word (used for password recovery)",
            font = ("Arial", 14),
            text_color = "black"
        )
        secret_name_label.place(x = 40, y = 327)

        # secret word Entry
        secret_name_entry = ctk.CTkEntry(
            right_frame,
            placeholder_text = "Enter a secret word",
            width = 300,
            font = ("Arial", 14)
        )
        secret_name_entry.place(x = 40, y = 350)

        # Check box for term and condition
        check_box = ctk.CTkCheckBox(
            right_frame,
            text = "I have read and agree to the",
            font = ("Arial", 12),
            text_color = "black",
            checkbox_width = 20,
            checkbox_height = 20,
            hover_color = "white",
            checkmark_color = "green",
            cursor = "hand2",
            fg_color = "white"
        )
        check_box.place(x = 40, y = 387)

        # Term and Conddition Button
        term_and_condition_button = ctk.CTkButton(
            right_frame,
            text = "Term and Condition",
            font = ("Arial", 12, "bold", "underline"),
            text_color = "black",
            fg_color = "white",
            hover_color = "white",
            width = 0,
            height = 0,
            cursor = "hand2",
            command = lambda: self.term_and_condition_command()
        )
        term_and_condition_button.place(x = 218, y = 389)

        # Signup Button
        signup_button = ctk.CTkButton(
            right_frame,
            text = "SIGN UP",
            font = ("Arial", 12, "bold"),
            fg_color = "#1d1b94",
            hover_color = "#14136e",
            width = 300,
            cursor = "hand2",
            text_color = "white",
            command = lambda: self.signup_button_command(account_number_entry.get(), account_name_entry.get(), contact_entry.get(), user_id_entry.get(), password_enrty.get(), secret_name_entry.get())
        )
        signup_button.place(x = 40, y = 422)

        # Already Have Account Label
        already_have_acc_label = ctk.CTkLabel(
            right_frame,
            font = ("Arial", 12),
            text = "Already Have account?",
            text_color = "black",
        )
        already_have_acc_label.place(x = 100, y = 455)

        # Login Button
        login_button = ctk.CTkButton(
            right_frame,
            text = "Log in",
            width = 0,
            height = 0,
            text_color = "#0d36db",
            hover_color = "white",
            cursor = "hand2",
            font = ("Arial", 12, "bold", "underline"),
            fg_color = "white",
            command = lambda: self.login_button_command()
        )
        login_button.place(x = 228, y = 458)

    def term_and_condition_command(self):
        webbrowser.open("https://secure.askaribank.com.pk/Askari/Content/html/terms.html")

    def signup_button_command(self, account_number, account_name, contact, user_id, password, secret_name):
        self.supabase.signup(account_number, account_name, contact, user_id, password, secret_name)
        LoginPage(self.window)

    def login_button_command(self):
        LoginPage(self.window)