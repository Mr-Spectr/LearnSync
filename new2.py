import tkinter as tk
from tkinter import messagebox
import os

class SetupWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Setup Window")

        # Styling
        self.root.geometry("1000x500")
        self.root.configure(bg="lightgray")
        self.root.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        # Widgets
        self.label = tk.Label(root, text="Setup", font=("Helvetica", 40), bg="lightgray")
        self.label.pack(pady=(20, 10))

        self.username_label = tk.Label(root, text="Set Username:", font=("Helvetica", 20), bg="lightgray")
        self.username_entry = tk.Entry(root, font=("Helvetica", 16))

        self.password_label = tk.Label(root, text="Set Password:", font=("Helvetica", 20), bg="lightgray")
        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 16))

        self.setup_button = tk.Button(root, text="Setup", command=self.setup, font=("Helvetica", 20), bg="#4CAF50", fg="white", height=1, width=10)

        self.username_label.pack(pady=0)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.setup_button.pack(pady=10)

    def setup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Save username and password to a text file
        with open("credentials.txt", "w") as file:
            file.write(f"{username}\n{password}")

        self.root.destroy()  # Close the setup window
        login_window = LoginWindow(tk.Tk())
        login_window.show_login_window()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")

        # Styling
        self.root.geometry("1000x500")
        self.root.configure(bg="lightgray")
        self.root.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        # Widgets
        self.label = tk.Label(root, text="Login", font=("Helvetica", 50), bg="lightgray")
        self.label.pack(pady=(20, 10))

        self.username_label = tk.Label(root, text="Username:", font=("Helvetica", 20), bg="lightgray")
        self.username_entry = tk.Entry(root, font=("Helvetica", 16))

        self.password_label = tk.Label(root, text="Password:", font=("Helvetica", 20), bg="lightgray")
        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 16))

        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 20), bg="green", fg="white", height=1, width=10)
        self.new_user_button = tk.Button(root, text="New User", command=self.show_setup_window, font=("Helvetica", 20), bg="#2196F3", fg="white", height=1, width=10)

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=10)
        self.new_user_button.pack(pady=10)

    def show_login_window(self):
        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Read stored credentials from the text file
        with open("credentials.txt", "r") as file:
            stored_username, stored_password = file.read().splitlines()

        # Check the entered credentials against stored credentials
        if username == stored_username and password == stored_password:
            self.root.destroy()  # Close the login window
            main_window = MainWindow(tk.Tk())
            main_window.show_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_setup_window(self):
        self.root.destroy()  # Close the login window
        setup_window = SetupWindow(tk.Tk())
        setup_window.root.mainloop()

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        # Styling
        self.root.geometry("1000x500")
        self.root.configure(bg="lightgray")
        self.root.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        # Widgets
        self.label = tk.Label(root, text="Welcome, User!", font=("Helvetica", 40), bg="lightgray")
        self.label.pack(pady=(30, 10))

        self.proceed_button = tk.Button(root, text="Proceed", command=self.show_logout_window, font=("Helvetica", 20), bg="green", fg="white", height=1, width=10)
        self.logout_button = tk.Button(root, text="Logout", command=self.logout, font=("Helvetica", 20), bg="red", fg="white", height=1, width=10)
        self.delete_account_button = tk.Button(root, text="Delete Account", command=self.delete_account, font=("Helvetica", 16), bg="red", fg="white", height=1, width=15)

        self.proceed_button.pack(pady=10)
        self.logout_button.pack(pady=10)
        self.delete_account_button.pack(pady=10)

    def show_main_window(self):
        self.root.mainloop()

    def show_logout_window(self):
        self.root.withdraw()  # Hide the main window
        logout_window = LogoutWindow(tk.Tk(), self.root)
        logout_window.show_logout_window()

    def logout(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()  # Close the main window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

    def delete_account(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete your account?")
        if confirm:
            os.remove("credentials.txt")  # Delete the credentials file
            self.root.destroy()  # Close the main window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

class LogoutWindow:
    def __init__(self, root, login_root):
        self.root = root
        self.login_root = login_root
        self.root.title("Logout Window")

        # Styling
        self.root.geometry("1000x500")
        self.root.configure(bg="lightgray")
        self.root.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        # Widgets
        self.logout_label = tk.Label(root, text="What would you like to do?", font=("Helvetica", 30), bg="lightgray")
        self.logout_label.pack(pady=(20, 10))

        self.logout_button = tk.Button(root, text="Logout", command=self.logout, font=("Helvetica", 20), bg="green", fg="white", height=1, width=10)
        self.delete_account_button = tk.Button(root, text="Delete Account", command=self.delete_account, font=("Helvetica", 16), bg="red", fg="white", height=1, width=15)

        self.logout_button.pack(pady=20)
        self.delete_account_button.pack(pady=20)

    def show_logout_window(self):
        self.root.mainloop()

    def logout(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()  # Close the logout window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

    def delete_account(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete your account?")
        if confirm:
            os.remove("credentials.txt")  # Delete the credentials file
            self.root.destroy()  # Close the logout window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

if __name__ == "__main__":
    # Check if the credentials file exists
    if os.path.exists("credentials.txt"):
        root = tk.Tk()
        login_window = LoginWindow(root)
        login_window.show_login_window()
    else:
        root = tk.Tk()
        setup_window = SetupWindow(root)
        root.mainloop()
