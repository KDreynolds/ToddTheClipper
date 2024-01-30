import tkinter as tk
from tkinter import messagebox, Listbox, END
import pyperclip
import logging
import keyboard

logging.basicConfig(level=logging.INFO)

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
        self.root.title("Clipboard Manager")
        self.listbox = Listbox(self.root)
        self.listbox.pack()
        self.previous_clipboard_content = pyperclip.paste()
        self.root.after(100, self.check_clipboard)  # Check clipboard every 100ms
        keyboard.add_hotkey('ctrl+alt+v', self.paste)  # Bind Ctrl+Alt+V to paste method
        keyboard.add_hotkey('ctrl+alt+c', self.check_clipboard)  # Bind Ctrl+Alt+C to check_clipboard method
        self.root.mainloop()

    def check_clipboard(self):
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != self.previous_clipboard_content:
            logging.info(f"New clipboard content detected: {current_clipboard_content}")
            self.clipboard.push(current_clipboard_content)
            self.listbox.insert(END, current_clipboard_content)
            self.previous_clipboard_content = current_clipboard_content
        self.root.after(100, self.check_clipboard)

    def paste(self):
        content = self.clipboard.pop()
        if content:
            logging.info(f"Pasting content: {content}")
            pyperclip.copy(content)
        else:
            messagebox.showinfo("Info", "Clipboard is empty")

if __name__ == "__main__":
    manager = ClipboardManager()