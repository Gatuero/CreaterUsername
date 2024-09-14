import data_processing
def createUsername(text_area,entry_length,var,tk):
    try:
        text_area.configure(state='normal')
        length = int(entry_length.get())
        consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        vowels = "AEIOU"
        username = str()
        username = ("\n" + data_processing.centerUsername(length) +
                    data_processing.processUsername(var,length,username,consonants,vowels))
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, username)
        text_area.configure(state='disabled')
    except ValueError as e:
        from tkinter import messagebox
        messagebox.showerror("Error", "No se entiende la longitud")
        return