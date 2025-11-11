import customtkinter as ctk

class MainWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Title Label
        self.label = ctk.CTkLabel(self, text="API Tester", font=("Arial", 28, "bold"))
        self.label.pack(pady=30)

        # Simple Info
        self.info = ctk.CTkLabel(self, text="Welcome! You can test APIs here.")
        self.info.pack(pady=10)
