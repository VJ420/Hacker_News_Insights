import tkinter as tk
from tkinter import scrolledtext, filedialog
import pyttsx3

# Simple revision app with voice support

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_file(text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, data)

def main():
    root = tk.Tk()
    root.title("Revision Reader")
    root.geometry("600x400")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_widget.pack(expand=True, fill=tk.BOTH)

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill=tk.X)

    open_btn = tk.Button(btn_frame, text="Open File", command=lambda: open_file(text_widget))
    open_btn.pack(side=tk.LEFT, padx=5, pady=5)

    read_btn = tk.Button(btn_frame, text="Read Text", command=lambda: speak_text(text_widget.get(1.0, tk.END)))
    read_btn.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
