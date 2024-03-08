import customtkinter as ctk
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Timer Example")
        self.geometry("300x150")

        self.label = ctk.CTkLabel(self, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=20)

        self.start_button = ctk.CTkButton(self, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.seconds = 5

    def start_timer(self):
        self.update_timer()

    def update_timer(self):
        self.seconds -= 1
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.seconds))
        self.label.configure(text=formatted_time)
        if(self.seconds>0):
          self.after(1000, self.update_timer)
if __name__ == "__main__":
    app = App()
    app.mainloop()