
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("380x300")
ventana.title("Problema 4")
ventana.configure(background='#37474f')
var = tk.DoubleVar()

c1 = tk.Label(ventana, text="Calificación 1", bg="violet", fg="purple", font=("Arial", 12))
c1.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack()
entrada1.config(fg="purple", justify="center", font="Arial")

c2 = tk.Label(ventana, text="Calificación 2", bg="violet", fg="purple", font=("Arial", 12))
c2.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack()
entrada2.config(fg="purple", justify="center", font="Arial")

c3 = tk.Label(ventana, text="Calificación 3", bg="violet", fg="purple", font=("Arial", 12))
c3.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada3 = tk.Entry(ventana, textvariable= entrada1)
entrada3.pack()
entrada3.config(fg="purple", justify="center", font="Arial")

c4 = tk.Label(ventana, text="Nota Examen final", bg="violet", fg="purple", font=("Arial", 12))
c4.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada4 = tk.Entry(ventana)
entrada4.pack()
entrada4.config(fg="purple", justify="center", font="Arial")

c5 = tk.Label(ventana, text="Nota trabajo final", bg="violet", fg="purple", font=("Arial", 12))
c5.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada5 = tk.Entry(ventana)
entrada5.pack()
entrada5.config(fg="purple", justify="center", font="Arial")


def promedioSuma():
    c1 = float(entrada1.get()) + float(entrada2.get()) + float(entrada3.get())
    c1 = c1 / 3 * float(0.55)
    c4 = float(entrada4.get()) * float(0.30)
    c5 = float(entrada5.get()) * float(0.15)
    cf = c1 + c4 + c5

    return var.set(cf)

resultado= tk.Label(ventana, textvariable = var, padx = 5, pady= 5, width = 20 )
resultado.pack()
resultado.config(fg="purple", justify="center", font="Arial")
boton1 = tk.Button(ventana, text= "Resultado",command = promedioSuma, bg="violet", fg="purple", font=("Arial", 13))
boton1.pack(side=tk.TOP)

ventana.mainloop()
