from supabase import create_client
from config import url, key
class SupabaseBankApp:
    def __init__(self):
        self.client = create_client(url, key)

    def signup(self, account_number, account_name, contact, user_id, password, secret_name):
        # Check if the account already exists
        existing_user = self.client.table("users").select("account_number").eq("account_number", account_number).execute()

        if existing_user.data:
            return {"status": "error", "message": "Account number already exists."}

        # Insert new user into the database
        signup_response = self.client.table("users").insert({
            "account_number": account_number,
            "account_name": account_name,
            "contact": contact,
            "user_id": user_id,
            "password": password,
            "secret_name": secret_name,
            "account_balance": 10000  # Initialize account balance to 10000
        }).execute()

        self.client.table("card_management").insert({
            "account_number": account_number,
            "card_pin": 0000
        }).execute()

        return {"status": "success", "message": "Signup successful."}

    def login(self, user_id, password):
        # Check if the user exists
        user_response = self.client.table("users").select("user_id", "password").eq("user_id", user_id).execute()

        if not user_response.data:
            return {"status": "error", "message": "User ID not found."}

        # Verify if the provided password matches
        if user_response.data[0]["password"] == password:
            # Retrieve account details for the logged-in user
            account_response = self.client.table("users").select("account_balance, account_name, account_number").eq("user_id", user_id).execute()

            # Prepare response with additional account details
            account_data = account_response.data[0]
            return {
                "status": "success",
                "message": "Login successful.",
                "account_details": {
                    "account_balance": account_data["account_balance"],
                    "account_name": account_data["account_name"],
                    "account_number": account_data["account_number"]
                }
            }
        else:
            return {"status": "error", "message": "Incorrect password."}

    def forgot_password(self, account_number, secret_name, new_password):
        # Check if the account number and secret word match
        user = self.client.table("users").select("account_number", "secret_name", "password").eq("account_number",account_number).execute()

        if not user.data:
            return {"status": "error", "message": "Account number not found."}

        if user.data[0]["secret_name"] != secret_name:
            return {"status": "error", "message": "Incorrect secret word."}

        # Update the password
        update_response = self.client.table("users").update({"password": new_password}).eq("account_number",account_number).execute()

        return {"status": "success", "message": "Password successfully updated."}

    def get_latest_transactions(self, account_number):
        # Retrieve the 12 latest transactions for the given account number
        transactions = self.client.table("transaction").select("*").eq("account_number", account_number).order("transaction_date", desc=True).limit(12).execute()

        if not transactions.data:
            return {"status": "error", "message": "No transactions found for this account."}

        return {"status": "success", "transactions": transactions.data}

    def store_histroy(self, account_number, amount, account_type):
        amount = float(amount)

        # Insert the transaction into the Transaction table
        self.client.table("transaction").insert({
            "account_number": account_number,
            "transaction_type": account_type,
            "amount": amount
        }).execute()

        return {"status": "success", "message": "Bill payment transaction recorded successfully."}

    def update_card_pin(self, account_number, new_pin):

        # Ensure the new PIN is a 4-digit number
        if len(new_pin) != 4 or not new_pin.isdigit():
            return {"status": "error", "message": "PIN must be a 4-digit number."}

        # Update the card pin in the database
        update_response = self.client.table("card_management").update({"card_pin": new_pin}).eq("account_number",account_number).execute()

        return {"status": "success", "message": "Card PIN successfully updated."}

    def update_account_name(self, account_number, new_account_name):

        # Check if the account exists
        user = self.client.table("users").select("account_number").eq("account_number", account_number).execute()

        if not user.data:
            return {"status": "error", "message": "Account number not found."}

        # Update the account name
        update_response = self.client.table("users").update({"account_name": new_account_name}).eq("account_number",
                                                                                                       account_number).execute()

        return {"status": "success", "message": "Account name successfully updated."}

    def update_account_balance(self, account_number, new_balance):
        # Check if the account exists
        response = self.client.table("users").select("account_balance").eq("account_number", account_number).execute()

        if not response.data or len(response.data) == 0:
            return {"status": "error", "message": "Account number not found."}

        account_balance = response.data[0]["account_balance"]
        new_balance = float(new_balance)
        updated_balance = account_balance-new_balance

        # Update the account name
        update_response = self.client.table("users").update({"account_balance": updated_balance}).eq("account_number",account_number).execute()

        return {"status": "success", "message": "Account name successfully updated."}
