"""A simple yet polished revision tool with text-to-speech support."""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import pyttsx3


class RevisionApp(tk.Tk):
    """Tkinter-based application for reading text aloud."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Revision Reader")
        self.geometry("700x500")

        # Use a themed style for a cleaner look
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#2b2b2b")
        style.configure(
            "TButton",
            font=("Helvetica", 12),
            padding=10,
        )

        self.configure(bg="#2b2b2b")

        self.engine = pyttsx3.init()
        self._create_widgets()

    def _create_widgets(self) -> None:
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.text_widget = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            font=("Helvetica", 14),
            bg="#1e1e1e",
            fg="white",
        )
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=5)

        open_btn = ttk.Button(btn_frame, text="Open File", command=self.open_file)
        open_btn.pack(side=tk.LEFT, padx=5)

        read_btn = ttk.Button(btn_frame, text="Read Text", command=self.read_text)
        read_btn.pack(side=tk.LEFT, padx=5)

    def open_file(self) -> None:
        """Load a text file into the editor."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, data)

    def read_text(self) -> None:
        """Read the text aloud using pyttsx3."""
        text = self.text_widget.get(1.0, tk.END)
        self.engine.say(text)
        self.engine.runAndWait()


def main() -> None:
    app = RevisionApp()
    app.mainloop()


if __name__ == "__main__":
    main()
