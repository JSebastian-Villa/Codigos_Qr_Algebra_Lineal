import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
from qrcode.constants import ERROR_CORRECT_H
import sympy as sp


class PistaQR:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = self.convertir_a_fracciones(respuesta_correcta)

    def convertir_a_fracciones(self, respuesta):
        try:
            estructura = eval(respuesta, {"__builtins__": None}, {})
        except Exception:
            raise ValueError("Formato de respuesta inválido. Usa paréntesis o corchetes correctamente.")

        def convertir_elemento(elem):
            return sp.Rational(elem)

        def procesar(estructura):
            if isinstance(estructura, (list, tuple)):
                return tuple(procesar(e) for e in estructura)
            else:
                return convertir_elemento(estructura)

        return procesar(estructura)

    def generar_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_H,  # Corrección Reed-Solomon nivel H (30%)
            box_size=10,
            border=4,
        )
        qr.add_data(self.enunciado)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")

    def verificar_respuesta(self, respuesta):
        try:
            respuesta_jugador = self.convertir_a_fracciones(respuesta)
        except Exception:
            return False
        return respuesta_jugador == self.respuesta_correcta


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
                "(3,1,2)"
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
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f4f8")
        self.frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        self.frame.pack(pady=30, padx=30, fill="both", expand=True)
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

            tk.Label(self.frame, text=f"Pista {self.jugador.pistas_resueltas + 1}",
                     font=("Helvetica", 16, "bold"), bg="white", fg="#2a4d69").pack(pady=10)

            tk.Label(self.frame, text="Escanea el código QR para leer el enunciado",
                     font=("Helvetica", 13), bg="white").pack()
            tk.Label(self.frame, image=qr_imagen_tk, bg="white").pack(pady=10)
            self.frame.image = qr_imagen_tk

            tk.Label(self.frame, text="✍ Ingresa tu respuesta:",
                     font=("Helvetica", 12), bg="white").pack(pady=5)
            self.respuesta_entry = tk.Entry(self.frame, font=("Helvetica", 12), width=40, justify="center")
            self.respuesta_entry.pack(pady=10, ipady=5)

            btn = tk.Button(self.frame, text="Verificar respuesta", font=("Helvetica", 11, "bold"),
                            bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised",
                            command=self.verificar_respuesta)
            btn.pack(pady=15)

        else:
            self.clear_frame()
            tk.Label(self.frame, text="🎉 ¡Felicidades, resolviste todas las pistas! 🎉",
                     font=("Helvetica", 16, "bold"), fg="#2e7d32", bg="white").pack(pady=60)

    def verificar_respuesta(self):
        respuesta = self.respuesta_entry.get()
        if self.pista_actual.verificar_respuesta(respuesta):
            messagebox.showinfo("✅ Correcto", "¡Muy bien! Vamos a la siguiente pista.")
            self.jugador.pistas_resueltas += 1
            self.mostrar_pista()
        else:
            messagebox.showerror("❌ Incorrecto", "Respuesta incorrecta. Intenta de nuevo.")

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    juego = JuegoEscapeQR()

    def iniciar_juego():
        nombre = nombre_entry.get()
        if nombre:
            juego.iniciar_juego(nombre)
            start_frame.destroy()

    start_frame = tk.Frame(juego.root, bg="#f0f4f8")
    start_frame.pack(pady=80)

    tk.Label(start_frame, text="🎮 Juego Escape QR", font=("Helvetica", 20, "bold"),
             bg="#f0f4f8", fg="#2a4d69").pack(pady=10)
    tk.Label(start_frame, text="Ingresa tu nombre para comenzar:",
             font=("Helvetica", 13), bg="#f0f4f8").pack(pady=5)
    nombre_entry = tk.Entry(start_frame, font=("Helvetica", 12), width=30, justify="center")
    nombre_entry.pack(pady=10, ipady=5)

    tk.Button(start_frame, text="🚀 Iniciar Juego", font=("Helvetica", 12, "bold"),
              bg="#2196F3", fg="white", padx=10, pady=5, relief="raised", command=iniciar_juego).pack(pady=20)

    juego.root.mainloop()