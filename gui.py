import file_manager

def openRoot():
    import tkinter as tk
    root = tk.Tk()
    root.title("Generador de Apodos")
    root.resizable(width=False, height=False)

    # Etiqueta y entrada para la longitud
    tk.Label(root, text="Escribe la longitud:").grid(row=0, column=0, padx=20, pady=10)
    entry_length = tk.Entry(root, width=14)
    entry_length.grid(row=0, column=1, padx=0, pady=10)

    # Radiobuttons para seleccionar si iniciar con consonantes o vocales
    var = tk.IntVar(value=1)
    frm1 = tk.LabelFrame(root, text="  Iniciar con:  ", borderwidth=2, relief="groove", height=50, width=170).grid(
        row=1, column=0, columnspan=2, padx=25)
    tk.Radiobutton(frm1, text="Consonantes", variable=var, value=1).grid(row=1, column=0, rowspan=2, padx=0, pady=0)
    tk.Radiobutton(frm1, text="Vocales", variable=var, value=2).grid(row=1, column=1, rowspan=2, padx=0, pady=0)

    # Área de texto para mostrar la palabra generada
    text_area = tk.Text(root, height=3, width=20, font=("console", 20))
    text_area.grid(row=0, column=2, rowspan=3, padx=25, pady=10)
    text_area.configure(state='disabled')

    # Botón para crear la palabra
    btn_create = tk.Button(root, text="CREAR APODO", command=lambda:
        file_manager.createUsername(
            text_area,entry_length,var,tk
        )
    )
    btn_create.grid(row=3, column=0, columnspan=3, pady=10)

    # Actualiza la ventana y la centra en la pantalla
    root.update_idletasks()
    root.geometry(
        centerRoot(
            root.winfo_width(),
            root.winfo_height(),
            root.winfo_screenwidth(),
            root.winfo_screenheight()
        )
    )

    # Ejecutar la aplicación
    root.mainloop()

def centerRoot(rootWidth, rootHeight, screenWidth, screenHeight):
    x = (screenWidth // 2) - (rootWidth // 2)
    y = (screenHeight // 2) - (rootHeight // 2)
    return f'{rootWidth}x{rootHeight}+{x}+{y}'

def testWithoutRoot():
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    array_alphabet=list(alphabet)
    word = input("Ingresa una palabra: ")
    array_word = list(word.upper())
    save_letters=str()
    count_combinations=0
    for i in range(len(word)):
        for j in range(len(alphabet)):
            aux = save_letters
            aux += array_alphabet[j]
            for k in range(len(word)-(i+1)):
                aux+=array_alphabet[0]
            count_combinations+=1
            print(str(count_combinations)+" "+aux)
            if array_word[i]==array_alphabet[j]:
                save_letters += array_alphabet[j]
                break
