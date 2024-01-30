import tkinter as tk
from tkinter import messagebox
import pyperclip

class ClipboardStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

class ClipboardManager:
    def __init__(self):
        self.clipboard = ClipboardStack()
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        self.previous_clipboard_content = pyperclip.paste()
        self.root.after(100, self.check_clipboard)  # Check clipboard every 100ms
        self.root.mainloop()

    def check_clipboard(self):
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != self.previous_clipboard_content:
            self.clipboard.push(current_clipboard_content)
            self.previous_clipboard_content = current_clipboard_content
        self.root.after(100, self.check_clipboard)

    def paste(self):
        content = self.clipboard.pop()
        if content:
            pyperclip.copy(content)
        else:
            messagebox.showinfo("Info", "Clipboard is empty")

if __name__ == "__main__":
    manager = ClipboardManager()