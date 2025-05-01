import tkinter as tk
from tkinter import messagebox
from tkinter import font



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
    def __init__(self, master):
        self.master = master
        self.master.title("Career Path Advisor")
        self.master.geometry("800x400")  # Set the window size
        self.master.configure(bg="#f0f0f0")  # Set background color
        self.master.iconbitmap("P:\IDT\IDT\IDT\hello.ico")
        

        # Create an instance of CareerPathAdvisor
        self.advisor = CareerPathAdvisor()

        # Define career paths and their details
        software_engineer = CareerPath(
            "Software Engineer",
            ["Programming Languages (e.g., Python, Java)", "Algorithm Design", "Database Management"],
            ["Coursera", "Udacity", "Codecademy"]
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

        # Add career paths to the advisor
        self.advisor.add_career_path(software_engineer)
        self.advisor.add_career_path(data_scientist)
        self.advisor.add_career_path(product_manager)

        # Set the font for the heading
        heading_font = font.Font(family="Helvetica", size=18, weight="bold")

        # Create UI elements
        self.label = tk.Label(master, text="Select a Career Path:", font=heading_font, fg="blue", bg="#f0f0f0")
        self.label.pack()

        # Calculate proportional button size
        button_width = int(self.master.winfo_reqwidth() / len(self.advisor.career_paths))

        # Create buttons for each career path
        for path in self.advisor.career_paths:
            button = tk.Button(master, text=path.name, width=button_width + 10, font=("Helvetica", 14),
                               relief=tk.RAISED, bd=3, command=lambda p=path: self.show_details(p), bg="#d9d9d9", activebackground="#b3b3b3")
            button.pack(pady=5)

        # Add a button for the chatbot
        chatbot_button = tk.Button(master, text="Chat with Chatbot", width=20, font=("Helvetica", 14),
                                   relief=tk.RAISED, bd=3, command=self.open_chatbot, bg="#d9d9d9", activebackground="#b3b3b3")
        chatbot_button.pack(pady=10)

    def show_details(self, selected_career_path):
        second_window = tk.Toplevel(self.master)
        app = SecondWindow(second_window, selected_career_path)

    def open_chatbot(self):
        chatbot_window = tk.Toplevel(self.master)
        app = ChatbotWindow(chatbot_window)

class SecondWindow:
    def __init__(self, master, selected_career_path):
        self.master = master
        self.master.title("Career Path Details")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")
        self.master.iconbitmap("IMG_20231218_115201.ico")
       

        self.details = tk.Text(master, wrap=tk.WORD, font=("Helvetica", 12), bg="#ffffff")
        self.details.insert(tk.END, selected_career_path.display_details())
        self.details.pack(padx=20, pady=10)

def main():
    root = tk.Tk()
    app = CareerPathAdvisorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
