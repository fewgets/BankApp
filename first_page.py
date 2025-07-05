import customtkinter as ctk
from PIL import Image
from datetime import datetime
from Database import SupabaseBankApp
import random

class MainPage:
    def __init__(self, window, account_name, account_number, account_balance):
        self.window = window
        self.window.title("NUML Digital Bank")
        self.account_name = account_name
        self.account_number = account_number
        self.account_balance = account_balance
        self.supabase = SupabaseBankApp()
        self.initgui()

    def initgui(self):

        # Creating left frame
        left_frame = ctk.CTkFrame(
            self.window,
            width = 400,
            height = 500,
            fg_color = "#ebebeb"
        )
        left_frame.place(x = 0, y = 0)

        # Apply logo
        logo_image = Image.open("Images/numl-logo.png")
        logo_photo = ctk.CTkImage(logo_image, size=(50, 50))
        logo_label = ctk.CTkLabel(
            left_frame,
            image = logo_photo,
            text = ""
        )
        logo_label.place(x=35, y=15)

        # Bank Name
        bank_name_label = ctk.CTkLabel(
            left_frame,
            text = "NUML Digital Bank",
            font = ("Arial", 28, "bold"),
            text_color = "#2f477f"
        )
        bank_name_label.place(x=90, y=24)

        # Set Date time label
        date_time_label = ctk.CTkLabel(
            left_frame,
            text = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            font = ("Arial", 12),
            text_color = "black"
        )
        date_time_label.place(x=43, y=76)

        # Set Account Name
        account_name_label = ctk.CTkLabel(
            left_frame,
            text = self.account_name,
            font = ("Arial", 14),
            text_color = "black"
        )
        account_name_label.place(x=255, y=76)

        # Set frame for balance
        self.balance_frame = ctk.CTkFrame(
            left_frame,
            width = 325,
            height = 100,
            fg_color = "white",
            corner_radius = 10
        )
        self.balance_frame.place(x = 38, y = 100)

        # Show balance Button
        show_balance_button = ctk.CTkButton(
            self.balance_frame,
            text = "Show\nBalance",
            font = ("Arial", 12, "bold"),
            text_color = "#2f477f",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 30,
            height = 30,
            command = lambda: self.show_balance_button_command()
        )
        show_balance_button.place(x = 5, y = 3)

        # Current Label
        current_label = ctk.CTkLabel(
            self.balance_frame,
            text = "Current",
            font = ("Arial", 18, "bold"),
            text_color = "#1d1b94"
        )
        current_label.place(x = 125, y = 10)

        # Account Number Label
        account_number_label = ctk.CTkLabel(
            self.balance_frame,
            text = self.account_number,
            font = ("Arial", 13),
            text_color = "#4a4a4a"
        )
        account_number_label.place(x = 108, y = 30)

        # Pkr Label
        pkr_label = ctk.CTkLabel(
            self.balance_frame,
            text = "Pkr",
            font = ("Arial", 13),
            text_color = "black"
        )
        pkr_label.place(x = 110, y = 55)

        # Acc Balance Label
        acc_balance_label = ctk.CTkLabel(
            self.balance_frame,
            text = "XXXXXX",
            font = ("Arial", 16, "bold"),
            text_color = "black"
        )
        acc_balance_label.place(x = 135, y = 55)

        # Create a Canvas for line
        line = ctk.CTkCanvas(
            left_frame,
            width = 470,
            height = 2
        )
        line.place(x = 60, y = 320)

        # Add a thin line
        line.create_line(0, 2, 480, 2, fill="#1d1b94", width = 15)  # Adjust y-values for the line's position

        # Mini Statement Button
        mini_statement_image = Image.open("Images/mini_statement.png")
        mini_statement_icon = ctk.CTkImage(mini_statement_image, size=(65, 65))
        mini_statement_button = ctk.CTkButton(
            left_frame,
            image = mini_statement_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width=2,
            border_color="#2f477f",
            command = lambda: self.mini_statement_button_command()
        )
        mini_statement_button.place(x = 42, y = 230)

        # Mini Statement Label
        mini_statement_label = ctk.CTkLabel(
            left_frame,
            text = "Mini Statement",
            font = ("Arial", 12, "bold"),
            text_color = "black",
            height = 0
        )
        mini_statement_label.place(x = 47, y = 335)

        # Bill Payment Button
        bill_pay_image = Image.open("Images/bill_pay.jpg")
        bill_pay_icon = ctk.CTkImage(bill_pay_image, size=(80, 80))
        bill_pay_button = ctk.CTkButton(
            left_frame,
            image = bill_pay_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width=2,
            border_color="#2f477f",
            command = lambda: self.bill_pay_button_command()
        )
        bill_pay_button.place(x = 150, y = 230)

        # Bill Payment Label
        bill_pay_label = ctk.CTkLabel(
            left_frame,
            text = "Bill Payment",
            font = ("Arial", 12, "bold"),
            text_color = "black",
            height = 0
        )
        bill_pay_label.place(x = 165, y = 335)

        # transfer Fund Button
        transfer_fund_image = Image.open("Images/transfer.jpg")
        transfer_fund_icon = ctk.CTkImage(transfer_fund_image, size=(80, 80))
        transfer_fund_button = ctk.CTkButton(
            left_frame,
            image = transfer_fund_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width=2,
            border_color="#2f477f",
            command = lambda: self.transfer_fund_button_command()
        )
        transfer_fund_button.place(x = 260, y = 230)

        # Fund Transfer Label
        fund_transfer_label = ctk.CTkLabel(
            left_frame,
            text = "Fund Transfer",
            font = ("Arial", 12, "bold"),
            text_color = "black",
            height = 0
        )
        fund_transfer_label.place(x = 270, y = 335)

        # Card Management Button
        card_image = Image.open("Images/card.jpg")
        card_icon = ctk.CTkImage(card_image, size=(80, 80))
        card_button = ctk.CTkButton(
            left_frame,
            image = card_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width=2,
            border_color="#2f477f",
            command = lambda: self.card_button_command()
        )
        card_button.place(x = 40, y = 360)

        # card management Label
        card_label = ctk.CTkLabel(
            left_frame,
            text = "Card Management",
            font = ("Arial", 11, "bold"),
            text_color = "black",
            height = 0
        )
        card_label.place(x = 45, y = 465)

        # Edit Account Detail Button
        edit_image = Image.open("Images/edit.jpg")
        edit_icon = ctk.CTkImage(edit_image, size=(80, 80))
        edit_button = ctk.CTkButton(
            left_frame,
            image = edit_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width=2,
            border_color="#2f477f",
            command = lambda: self.edit_button_command()
        )
        edit_button.place(x = 150, y = 360)

        # Edit Detail Label
        edit_label = ctk.CTkLabel(
            left_frame,
            text = "Edit Account Detail",
            font = ("Arial", 11, "bold"),
            text_color = "black",
            height = 0
        )
        edit_label.place(x = 152, y = 465)

        # Logout Button
        logout_image = Image.open("Images/logout.jpg")
        logout_icon = ctk.CTkImage(logout_image, size=(80, 80))
        logout_button = ctk.CTkButton(
            left_frame,
            image = logout_icon,
            text = "",
            fg_color = "white",
            hover_color = "white",
            cursor = "hand2",
            width = 100,
            height = 100,
            corner_radius = 10,
            border_width = 2,
            border_color = "#2f477f",
            command = lambda: self.logout_button_command()
        )
        logout_button.place(x = 260, y = 360)

        # Logout Label
        logout_label = ctk.CTkLabel(
            left_frame,
            text = "Logout",
            font = ("Arial", 12, "bold"),
            text_color = "black",
            height = 0
        )
        logout_label.place(x = 285, y = 465)

        # Set Right Frame
        self.right_frame = ctk.CTkFrame(
            self.window,
            width = 500,
            height = 500,
            fg_color = "#2f477f",
            corner_radius = 0
        )
        self.right_frame.place(x=400, y=0)

        # Adding a user's name
        user_name_label = ctk.CTkLabel(
            self.right_frame,
            text = self.account_name.title() + "!",
            font = ("Cambria", 50, "bold"),
            text_color = "white"
        )
        user_name_label.place(x = 15, y = 175)

        # Adding Welome label to the Right Frame
        welcome_label = ctk.CTkLabel(
            self.right_frame,
            text = "Welcome To Numl Online Bank.",
            font = ("Cambria", 24, "bold"),
            text_color = "white"
        )
        welcome_label.place(x = 15, y = 230)

    def show_balance_button_command(self):
        # Acc Balance Label
        balance = f"{float(self.account_balance):.3f}"
        acc_balance_label = ctk.CTkLabel(
            self.balance_frame,
            text = balance,
            font = ("Arial", 16, "bold"),
            text_color = "black"
        )
        acc_balance_label.place(x = 135, y = 55)

    def mini_statement_button_command(self):
        # Clear all widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add heading for Mini Statement
        heading_label = ctk.CTkLabel(
            self.right_frame,
            text="Mini Statement",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        heading_label.place(x = 130, y = 30)

        # Fetch transactions
        response = self.supabase.get_latest_transactions(self.account_number)
        formatted_transactions = []
        for transaction in response["transactions"]:
            date = datetime.fromisoformat(transaction["transaction_date"]).strftime('%d %b %Y')
            transaction_type = transaction["transaction_type"]
            amount = transaction["amount"]
            formatted_transactions.append((date, transaction_type, amount))

        # Header labels for the table
        headers = ["Date", "Transaction", "Amount (Rs)"]
        x_positions = [20, 180, 380]  # X-coordinates for the columns
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(
                self.right_frame,
                text=header,
                font=("Arial", 16, "bold"),
                text_color="white"
            )
            header_label.place(x=x_positions[col], y=80)

        # Populate the table with transaction data
        for row, transaction in enumerate(formatted_transactions, start=1):
            y_position = 80 + (row) * 30  # Calculate y-coordinate for each row
            for col, value in enumerate(transaction):
                cell_label = ctk.CTkLabel(
                    self.right_frame,
                    text=value,
                    font=("Arial", 12),
                    text_color="white",
                    anchor="w"
                )
                cell_label.place(x=x_positions[col], y=y_position)

    def bill_pay_button_command(self):
        # Clear all widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add heading for Mini Statement
        heading_label = ctk.CTkLabel(
            self.right_frame,
            text="Bill Payment",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        heading_label.place(x=150, y=30)

        # Adding a Label of Choose Bill type
        choose_label = ctk.CTkLabel(
            self.right_frame,
            text = "Choose Your Bill Type",
            text_color = "white",
            font = ("Arial", 14, "bold")
        )
        choose_label.place(x=100, y=100)

        # Creating a dropbox to select bill type
        dropbox = ctk.CTkComboBox(
            self.right_frame,
            values = ["Electricity", "Gas", "Water", "Internet"],
            width = 300,
            state = "readonly",
            font = ("Arial", 14),
            justify = "center"
        )
        dropbox.set("Choose Your Bill Type")
        dropbox.place(x = 100, y = 125)

        # Enter Bill number label
        bill_number_label = ctk.CTkLabel(
            self.right_frame,
            text = "Enter Bill Number",
            font = ("Arial", 14, "bold"),
            text_color = "white"
        )
        bill_number_label.place(x = 100, y = 170)

        # Bill Number Entry
        bill_number_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text = "Enter your bill number",
            font = ("Arial", 14),
            width = 300
        )
        bill_number_entry.place(x = 100, y = 195)

        # Check Button
        check_button = ctk.CTkButton(
            self.right_frame,
            text = "Check for Bill",
            width = 300,
            fg_color = "white",
            hover_color = "#d1d1d1",
            text_color = "#2f477f",
            cursor = "hand2",
            font = ("Arial", 14, "bold"),
            command = lambda: self.check_button_command()
        )
        check_button.place(x = 100, y = 255)

    def check_button_command(self):
        # Label for showing bill amount
        amount = random.randint(100, 2000)
        bill_amount = ctk.CTkLabel(
            self.right_frame,
            text = f"Your bill amount is : {amount}",
            text_color = "white",
            font = ("Arial", 16, "bold")
        )
        bill_amount.place(x = 100, y = 300)

        # Pay Button
        pay_button = ctk.CTkButton(
            self.right_frame,
            text = "Pay Bill",
            text_color = "#2f477f",
            fg_color = "white",
            hover_color = "#d1d1d1",
            width = 300,
            cursor = "hand2",
            font = ("Arial", 14, "bold"),
            command = lambda: self.pay_button_command(amount)
        )
        pay_button.place(x = 100, y = 350)

    def pay_button_command(self, amount):
        # Checking for balance
        balance = int(self.account_balance)
        amount = int(amount)
        if amount <= balance:
            text = "Bill paying sucessfully"
            self.supabase.store_histroy(self.account_number, amount, "bill payment")
            self.supabase.update_account_balance(self.account_number, amount)
        else:
            text = "Insufficient Balance"

        # Result label
        result_label = ctk.CTkLabel(
            self.right_frame,
            text = text,
            font = ("Arial", 16, "bold"),
            text_color = "white"
        )
        result_label.place(x = 170, y = 395)

    def transfer_fund_button_command(self):
        # Clear all widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add heading for Mini Statement
        heading_label = ctk.CTkLabel(
            self.right_frame,
            text="Transfer Fund",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        heading_label.place(x=130, y=30)

        # Adding a Label of Enter Account Number
        account_number_label = ctk.CTkLabel(
            self.right_frame,
            text="Enter account Number",
            text_color="white",
            font=("Arial", 14, "bold")
        )
        account_number_label.place(x=100, y=100)

        # account Number Entry
        account_number_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Enter reciever account number",
            font=("Arial", 14),
            width=300
        )
        account_number_entry.place(x=100, y=125)

        # Enter amount label
        amount_label = ctk.CTkLabel(
            self.right_frame,
            text="Enter Amount",
            font=("Arial", 14, "bold"),
            text_color="white"
        )
        amount_label.place(x=100, y=170)

        # Amount Number Entry
        amount_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Enter amount",
            font=("Arial", 14),
            width=300
        )
        amount_entry.place(x=100, y=195)

        # Send Button
        send_button = ctk.CTkButton(
            self.right_frame,
            text = "Send",
            width = 300,
            fg_color = "white",
            hover_color = "#d1d1d1",
            text_color = "#2f477f",
            cursor = "hand2",
            font = ("Arial", 14, "bold"),
            command = lambda: self.send_button_command(account_number_entry.get(), amount_entry.get())
        )
        send_button.place(x = 100, y = 255)

    def send_button_command(self, acc_number, amount):
        amount = float(amount)
        balance = int(self.account_balance)
        if amount <= balance:
            response = self.supabase.update_account_balance(acc_number, amount)
            status = response["status"]
            if status == "success":
                self.supabase.store_histroy(acc_number, amount, "fund transfer")
                text = "Transfer Successfully"
            else:
                text = "Account Not Found"
        else:
            text = "Insufficient balance"

        # Result label
        result_label = ctk.CTkLabel(
            self.right_frame,
            text = text,
            font = ("Arial", 16, "bold"),
            text_color = "white"
        )
        result_label.place(x = 170, y = 310)

    def card_button_command(self):
        # Clear all widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add heading for Mini Statement
        heading_label = ctk.CTkLabel(
            self.right_frame,
            text="Card Management",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        heading_label.place(x=110, y=30)

        # Adding a Label of Enter Account Number
        card_number_label = ctk.CTkLabel(
            self.right_frame,
            text="Enter new card pin",
            text_color="white",
            font=("Arial", 14, "bold")
        )
        card_number_label.place(x=100, y=100)

        # account Number Entry
        card_number_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Enter a new pin number",
            font=("Arial", 14),
            width=300
        )
        card_number_entry.place(x=100, y=125)

        # Change Button
        change_button = ctk.CTkButton(
            self.right_frame,
            text = "Change PIN",
            width = 300,
            fg_color = "white",
            hover_color = "#d1d1d1",
            text_color = "#2f477f",
            cursor = "hand2",
            font = ("Arial", 14, "bold"),
            command = lambda: self.change_button_command(card_number_entry.get())
        )
        change_button.place(x = 100, y = 195)

    def change_button_command(self, card_pin):
        self.supabase.update_card_pin(self.account_number, card_pin)

        # Success label
        success_label = ctk.CTkLabel(
            self.right_frame,
            text = "Successfully changed PIN",
            font = ("Arial", 16, "bold"),
            text_color = "white"
        )
        success_label.place(x = 140, y = 260)

    def edit_button_command(self):
        # Clear all widgets in the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add heading for Mini Statement
        heading_label = ctk.CTkLabel(
            self.right_frame,
            text="Change Account Number",
            font=("Arial", 32, "bold"),
            text_color="white"
        )
        heading_label.place(x = 70, y = 30)

        # Adding a Label of Enter Account Number
        account_name_label = ctk.CTkLabel(
            self.right_frame,
            text="Enter account Name",
            text_color="white",
            font=("Arial", 14, "bold")
        )
        account_name_label.place(x=100, y=100)

        # account Number Entry
        account_name_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Enter reciever account number",
            font=("Arial", 14),
            width=300
        )
        account_name_entry.place(x=100, y=125)

        # Send Button
        change_button = ctk.CTkButton(
            self.right_frame,
            text="Change Name",
            width=300,
            fg_color="white",
            hover_color="#d1d1d1",
            text_color="#2f477f",
            cursor="hand2",
            font=("Arial", 14, "bold"),
            command=lambda: self.change_name_button_command(account_name_entry.get())
        )
        change_button.place(x = 100, y = 200)

    def change_name_button_command(self, new_name):
        self.supabase.update_account_name(self.account_number, new_name)

        # Success label
        success_label = ctk.CTkLabel(
            self.right_frame,
            text = "Name changed sucessfully",
            font = ("Arial", 16, "bold"),
            text_color = "white"
        )
        success_label.place(x = 140, y = 260)

    def logout_button_command(self):
        from start import GetStarted
        GetStarted(self.window)
