import tkinter as tk

class ExposureUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulated Exposure Therapy UI")
        self.label = tk.Label(self.root, text="Intensity: 0.0", font=("Arial", 24))
        self.label.pack(pady=20)

    def update_intensity(self, value):
        self.label.config(text=f"Intensity: {value:.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = ExposureUI()
    ui.update_intensity(0.5)
    ui.run()
