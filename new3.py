import tkinter as tk
from tkinter import messagebox
import os
from tkinter import font

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

        self.setup_button = tk.Button(root, text="Setup", command=self.setup, font=("Helvetica", 20), bg="#4CAF50",
                                      fg="white", height=1, width=10)

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

        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 20), bg="green",
                                      fg="white", height=1, width=10)
        self.new_user_button = tk.Button(root, text="New User", command=self.show_setup_window, font=("Helvetica", 20),
                                         bg="#2196F3", fg="white", height=1, width=10)

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
        if os.path.exists("credentials.txt"):
            with open("credentials.txt", "r") as file:
                stored_username, stored_password = file.read().splitlines()

            # Check the entered credentials against stored credentials
            if username == stored_username and password == stored_password:
                self.root.destroy()  # Close the login window
                main_window = CareerPathAdvisorApp(tk.Tk(), username)
            else:
                self.show_error_message("Login Failed", "Invalid username or password")
        else:
            self.show_error_message("Login Failed", "No user credentials found")

    def show_error_message(self, title, message):
        messagebox.showerror(title, message)

    def show_setup_window(self):
        self.root.destroy()  # Close the login window
        setup_window = SetupWindow(tk.Tk())
        setup_window.root.mainloop()

class MainWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Main Window")

        # Styling
        self.root.geometry("1000x500")
        self.root.configure(bg="lightgray")
        self.root.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        # Widgets
        self.label = tk.Label(root, text=f"__________LearnSync__________\nWelcome, {username}!", font=("Helvetica", 40), bg="lightgray")
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
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()  # Close the main window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

    def logout(self):
        self.show_logout_window()

    def delete_account(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete your account?")
        if confirm:
            os.remove("credentials.txt")  # Delete the credentials file
            self.root.destroy()  # Close the main window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

class CareerPath:
    def __init__(self, name, required_skills, learning_resources):
        self.name = name
        self.required_skills = required_skills
        self.learning_resources = learning_resources

    def display_details(self):
        details = f"Career Path: {self.name}\n\nRequired Skills:\n"
        details += "\n".join([f"- {skill}" for skill in self.required_skills])
        details += "\n\nLearning Resources:\n"
        details += "\n".join([f"- {resource}" for resource in self.learning_resources])
        return details

class CareerPathAdvisor:
    def __init__(self):
        self.career_paths = []

    def add_career_path(self, career_path):
        self.career_paths.append(career_path)

    def get_career_path_details(self, career_path_name):
        for path in self.career_paths:
            if path.name.lower() == career_path_name.lower():
                return path.display_details()
        return f"Career path '{career_path_name}' not found."

class CareerPathAdvisorApp:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.master.title("Career Path Advisor")
        self.master.geometry("600x800")
        self.master.configure(bg="darkgray")
        self.master.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        self.advisor = CareerPathAdvisor()

        software_engineer = CareerPath(
            "Software Engineer",
            [" |Programming Languages-\n    -> JavaScript\n    -> Python\n    -> C++\n    -> Rust\n    -> Go\n    -> Swift",
             " |Algorithm Design", " |Database Management\n    ->SQL\n    -> Data Analsis\n    -> Data Integtity"],
            ["  ->Coursera", "  ->Udacity", "  ->Codecademy"]
        )

        data_scientist = CareerPath(
            "Data Scientist",
            ["Statistics", "Machine Learning", "Data Visualization"],
            ["Kaggle", "edX", "DataCamp"]
        )

        product_manager = CareerPath(
            "Product Manager",
            ["Market Analysis", "Product Development", "Project Management"],
            ["LinkedIn Learning", "Product School", "Harvard Business Review"]
        )

        self.advisor.add_career_path(software_engineer)
        self.advisor.add_career_path(data_scientist)
        self.advisor.add_career_path(product_manager)

        heading_font = font.Font(family="ArialBlack", size=20, weight="bold")

        self.label = tk.Label(master, text=f"__________LearnSync__________\nWelcome, {username}!", font=heading_font, fg="darkblue", bg="darkgray")
        self.label.pack()

        button_width = int(self.master.winfo_reqwidth() / len(self.advisor.career_paths))

        for path in self.advisor.career_paths:
            button = tk.Button(master, text=path.name, width=40, font=("Verdana", 15),
                               relief=tk.RAISED, bd=3, command=lambda p=path: self.show_details(p), bg="#d9d9d9",
                               activebackground="gray")
            button.pack(pady=5)

        chatbot_button = tk.Button(master, text="Chat with Chatbot", width=20, font=("Verdana", 15),
                                   relief=tk.RAISED, bd=3, command=self.open_chatbot, bg="gray", activebackground="#b3b3b3")
        chatbot_button.pack()

        logout_button = tk.Button(master, text="Logout", width=20, font=("Verdana", 15),
                                  relief=tk.RAISED, bd=3, command=self.logout, bg="red", fg="white",
                                  activebackground="#b3b3b3")
        logout_button.pack(side=tk.BOTTOM, pady=20)

        delete_account_button = tk.Button(master, text="Delete Account", width=20, font=("Verdana", 15),
                                          relief=tk.RAISED, bd=3, command=self.delete_account, bg="red", fg="white",
                                          activebackground="#b3b3b3")
        delete_account_button.pack(side=tk.BOTTOM, pady=10)

    def show_details(self, selected_career_path):
        second_window = tk.Toplevel(self.master)
        app = SecondWindow(second_window, selected_career_path)

    def open_chatbot(self):
        chatbot_window = tk.Toplevel(self.master)
        app = ChatbotWindow(chatbot_window)

    def logout(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to logout?")
        if confirm:
            self.master.destroy()  # Close the Career Path Advisor window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()

    def delete_account(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete your account?")
        if confirm:
            os.remove("credentials.txt")  # Delete the credentials file
            self.master.destroy()  # Close the Career Path Advisor window
            login_window = LoginWindow(tk.Tk())
            login_window.show_login_window()


class SecondWindow:
    def __init__(self, master, selected_career_path):
        self.master = master
        self.master.title("Career Path Details")
        self.master.geometry("1000x700")
        self.master.configure(bg="gray")
        self.master.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        self.details = tk.Text(master, wrap=tk.WORD, font=("Verdana", 15), bg="lightgray")
        self.details.insert(tk.END, selected_career_path.display_details())
        self.details.pack(padx=20, pady=10)

class ChatbotWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        self.master.geometry("800x600")
        self.master.configure(bg="lightblue")
        self.master.iconbitmap("P:\IDT\IDT\IDT\hello.ico")

        self.label = tk.Label(master, text="Chatbot Window", font=("Helvetica", 30), bg="lightblue")
        self.label.pack(pady=(20, 10))

        self.chat_area = tk.Text(master, wrap=tk.WORD, font=("Verdana", 15), bg="white")
        self.chat_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        self.message_entry = tk.Entry(master, font=("Helvetica", 16))
        self.message_entry.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message, font=("Helvetica", 20),
                                     bg="green", fg="white", height=1, width=10)
        self.send_button.pack(pady=10)

    def send_message(self):
        message = self.message_entry.get()
        self.chat_area.insert(tk.END, f"User: {message}\n")
        # Add chatbot response logic here
        self.message_entry.delete(0, tk.END)

def main():
    if os.path.exists("credentials.txt"):
        root = tk.Tk()
        login_window = LoginWindow(root)
        login_window.show_login_window()
    else:
        root = tk.Tk()
        setup_window = SetupWindow(root)
        root.mainloop()

if __name__ == "__main__":
    main()
