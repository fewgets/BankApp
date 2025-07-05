import customtkinter as ctk
from Database import SupabaseBankApp

class ForgotPassword:

    def __init__(self, window):
        self.supabase = SupabaseBankApp()
        self.window = window
        self.window.title("Forgot Password - NUML Islamic Bank")
        self.window.geometry("400x300")
        self.initgui()

    def initgui(self):

        # Creating a frame
        frame = ctk.CTkFrame(
            self.window,
            fg_color="white",
            corner_radius=0,
            width = 400,
            height = 300
        )
        frame.place(x=0, y=0)

        # Account Number Label
        account_label = ctk.CTkLabel(
            frame,
            text = "Account Number:",
            fg_color = "white",
            text_color = "black",
            font = ("Arial", 14)
        )
        account_label.place(x = 57, y = 25)

        # Account Number Entry
        account_entry = ctk.CTkEntry(
            frame,
            placeholder_text = "Enter your account number",
            fg_color = "white",
            width = 300,
            font = ("Arial", 14)
        )
        account_entry.place(x = 55, y = 50)

        # Secret word Label
        secret_label = ctk.CTkLabel(
            frame,
            text = "Secret Word",
            fg_color = "white",
            text_color = "black",
            font = ("Arial", 14)
        )
        secret_label.place(x = 57, y = 90)

        # Secret word Entry
        secret_entry = ctk.CTkEntry(
            frame,
            placeholder_text = "Enter your secret word",
            fg_color = "white",
            width = 300
        )
        secret_entry.place(x = 55, y = 115)

        # New Password label
        new_password_label = ctk.CTkLabel(
            frame,
            text = "New Password:",
            fg_color = "white",
            font = ("Arial", 14),
            text_color = "black"
        )
        new_password_label.place(x = 57, y = 155)

        # New Password Entry
        new_password_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Enter your new password",
            fg_color="white",
            width=300
        )
        new_password_entry.place(x=55, y=180)

        # Submit Button
        submit_button = ctk.CTkButton(
            frame,
            text = "Submit",
            width = 300,
            cursor = "hand2",
            fg_color = "#1d1b94",
            text_color = "white",
            hover_color = "#14136e",
            font = ("Arial", 14),
            command = lambda: self.submit_button(account_entry.get(), secret_entry.get(), new_password_entry.get())
        )
        submit_button.place(x = 55, y = 235)

    def submit_button(self, account_entry, secret_entry, new_password_entry):
        self.supabase.forgot_password(account_entry, secret_entry, new_password_entry)
        from start import GetStarted
        GetStarted(self.window)
