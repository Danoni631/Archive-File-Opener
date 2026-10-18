# fuck you Minty
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class ArchiveViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(".archive viewer")
        self.root.geometry("600x400")

        self.current_file_path = None

        menubar = tk.Menu(root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open .archive", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save as...", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 11))
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.status_label = tk.Label(root, text="No file open", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open .archive file",
            filetypes=[("Archive text file", "*.archive"), ("Text file", "*.txt"), ("Any file", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                # Limpa a tela e insere o conteúdo do arquivo
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
                
                self.current_file_path = file_path
                self.status_label.config(text=f"Open: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Can't open file:\n{e}")

    def save_file(self):
        if self.current_file_path:
            try:
                content = self.text_area.get("1.0", tk.END)
                with open(self.current_file_path, "w", encoding="utf-8") as file:
                    file.write(content.strip())
                messagebox.showinfo("Success", "File saved with success!")
            except Exception as e:
                messagebox.showerror("Erroe", f"Can't save file:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".archive",
            filetypes=[("Archive text file", "*.archive"), ("Any file", "*.*")],
            title="Save as..."
        )
        
        if file_path:
            try:
                content = self.text_area.get("1.0", tk.END)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content.strip())
                
                self.current_file_path = file_path
                self.status_label.config(text=f"Open: {os.path.basename(file_path)}")
                messagebox.showinfo("Success", "File saved with success!")
            except Exception as e:
                messagebox.showerror("Error", f"Can't save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArchiveViewerApp(root)
    root.mainloop()
