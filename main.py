import random
import string
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def generar_contraseña_estandar(longitud):
    """
    Genera una contraseña aleatoria de una longitud específica que incluye mayúsculas, minúsculas, números y caracteres especiales.
    
    Parámetros:
    longitud (int): La longitud deseada para la contraseña.
    
    Retorna:
    str: Una contraseña generada aleatoriamente que cumple con los requisitos estándar.
    """
    if longitud < 4:
        raise ValueError("La longitud mínima para una contraseña estándar es 4.")
    
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    contraseña = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    contraseña += [random.choice(caracteres) for _ in range(longitud - 4)]
    random.shuffle(contraseña)
    return ''.join(contraseña)

def guardar_contraseña(contraseña, identificacion, ruta_carpeta):
    """
    Guarda la contraseña y su identificación en un archivo de texto dentro de una carpeta específica.
    
    Parámetros:
    contraseña (str): La contraseña a guardar.
    identificacion (str): La identificación o descripción de la contraseña.
    ruta_carpeta (str): La ruta de la carpeta donde se guardará el archivo.
    """
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    
    archivo_ruta = os.path.join(ruta_carpeta, "contraseñas.txt")
    with open(archivo_ruta, 'a') as archivo:
        archivo.write(f"Identificación: {identificacion}\nContraseña: {contraseña}\n\n")
    messagebox.showinfo("Contraseña Guardada", f"La contraseña ha sido guardada correctamente en: {archivo_ruta}")

def seleccionar_carpeta():
    """
    Abre una ventana para que el usuario seleccione una carpeta y retorna la ruta seleccionada.
    
    Retorna:
    str: La ruta de la carpeta seleccionada por el usuario.
    """
    ruta_carpeta = filedialog.askdirectory()
    return ruta_carpeta

def generar_y_guardar_contraseña():
    """
    Genera una contraseña y la guarda en la carpeta seleccionada por el usuario.
    """
    try:
        longitud = simpledialog.askinteger("Longitud de la Contraseña", "Introduce la longitud de la contraseña:")
        if longitud is None or longitud < 4:
            messagebox.showerror("Error", "La longitud mínima para una contraseña estándar es 4.")
            return
        
        contraseña = generar_contraseña_estandar(longitud)
        tk.Label(root, text="Tu contraseña generada es:").pack()
        tk.Label(root, text=contraseña).pack()
        
        ruta_carpeta = seleccionar_carpeta()
        if not ruta_carpeta:
            messagebox.showerror("Error", "No se seleccionó ninguna carpeta. La contraseña no ha sido guardada.")
            return
        
        identificacion = simpledialog.askstring("Identificación", "Introduce una identificación o descripción para esta contraseña:")
        if not identificacion:
            messagebox.showerror("Error", "No se proporcionó identificación. La contraseña no ha sido guardada.")
            return
        
        guardar_contraseña(contraseña, identificacion, ruta_carpeta)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def mostrar_ayuda():
    """
    Muestra una ventana de ayuda con información sobre cómo usar el programa.
    """
    ayuda = tk.Toplevel(root)
    ayuda.title("Ayuda")
    
    texto_ayuda = ("Este programa genera contraseñas aleatorias y las guarda en un archivo de texto.\n\n"
                   "Pasos para usar el programa:\n"
                   "1. Introduce la longitud de la contraseña deseada.\n"
                   "2. Selecciona una carpeta donde se guardará la contraseña.\n"
                   "3. Proporciona una identificación para la contraseña.\n"
                   "4. Presiona el botón 'Generar y Guardar Contraseña'.\n")
    
    tk.Label(ayuda, text=texto_ayuda).pack(padx=20, pady=10)

def centrar_ventana(ventana):
    """
    Centra una ventana en la pantalla.
    """
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))

root = tk.Tk()
root.title("Generador de Contraseñas")

centrar_ventana(root)

tk.Button(root, text="Generar y Guardar Contraseña", command=generar_y_guardar_contraseña).pack(pady=10)
tk.Button(root, text="Ayuda", command=mostrar_ayuda).pack(pady=5)

root.mainloop()
