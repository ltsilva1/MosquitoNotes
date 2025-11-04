import tkinter as tk
from ui.main_window import MosquitoNotesApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MosquitoNotesApp(root)
    root.mainloop()