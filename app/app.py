import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode


class PistaQR:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

    def generar_qr(self):

        qr = qrcode.make(self.enunciado)
        return qr

    def verificar_respuesta(self, respuesta):
        return respuesta.strip().lower() == self.respuesta_correcta.strip().lower()


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pistas_resueltas = 0


class JuegoEscapeQR:
    def __init__(self):
        self.pistas = [
            PistaQR(
                "Resuelve el siguiente sistema usando Gauss o Gauss-Jordan:\n"
                "4x - 3y + 2z = 13\n"
                "2x + y - z = 5\n"
                "x - 2y + 3z = 7\n"
                "Escribe la solución completa como (x, y, z):",
                "(3, -1, 2)"
            ),
            PistaQR(
                "Halla el determinante de la matriz:\n[[3, 2], [1, 4]]",
                "10"
            ),
            PistaQR(
                "Halla la inversa de la matriz [[2, 1], [3, 5]].\n"
                "Escribe como [[a/b, c/d], [e/f, g/h]]:",
                "[[5/7, -1/7], [-3/7, 2/7]]"
            )
        ]
        self.jugador = None
        self.root = tk.Tk()
        self.root.title("Juego Escape QR")
        self.root.geometry("500x500")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        self.pista_actual = None

    def iniciar_juego(self, nombre_jugador):
        self.jugador = Jugador(nombre_jugador)
        self.mostrar_pista()

    def mostrar_pista(self):
        if self.jugador.pistas_resueltas < len(self.pistas):
            self.pista_actual = self.pistas[self.jugador.pistas_resueltas]


            self.clear_frame()


            qr_imagen = self.pista_actual.generar_qr()
            qr_imagen.save("pista_qr.png")
            qr_imagen_tk = ImageTk.PhotoImage(qr_imagen)


            tk.Label(self.frame, text="Escanea el código QR para obtener la pista", font=("Arial", 14, "bold")).pack()
            tk.Label(self.frame, image=qr_imagen_tk).pack()
            self.frame.image = qr_imagen_tk


            self.respuesta_entry = tk.Entry(self.frame, font=("Arial", 12))
            self.respuesta_entry.pack(pady=10)


            tk.Button(self.frame, text="Verificar respuesta", command=self.verificar_respuesta).pack()

        else:
            self.clear_frame()
            tk.Label(self.frame, text="🎉 ¡Felicidades, resolviste todas las pistas! 🎉", font=("Arial", 14)).pack()

    def verificar_respuesta(self):
        respuesta = self.respuesta_entry.get()
        if self.pista_actual.verificar_respuesta(respuesta):
            messagebox.showinfo("Respuesta Correcta", "✅ ¡Correcto! Vamos a la siguiente pista.")
            self.jugador.pistas_resueltas += 1
            self.mostrar_pista()
        else:
            messagebox.showerror("Respuesta Incorrecta", "❌ Incorrecto. Intenta otra vez.")

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# --------- Ejecución del juego ---------
if __name__ == "__main__":
    juego = JuegoEscapeQR()

    # Ventana de inicio
    def iniciar_juego():
        nombre = nombre_entry.get()
        if nombre:
            juego.iniciar_juego(nombre)
            start_frame.pack_forget()

    start_frame = tk.Frame(juego.root)
    start_frame.pack(pady=20)

    tk.Label(start_frame, text="¡Bienvenido al Juego Escape QR!", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(start_frame, text="Ingresa tu nombre: ", font=("Arial", 12)).pack(pady=5)
    nombre_entry = tk.Entry(start_frame, font=("Arial", 12))
    nombre_entry.pack(pady=5)
    tk.Button(start_frame, text="Iniciar Juego", command=iniciar_juego).pack(pady=20)

    juego.root.mainloop()

