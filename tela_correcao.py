import customtkinter as ctk
from corrigir_provas import *

app = ctk.CTk()

app.title("Correção das Provas")
app.geometry("700x400")


button = ctk.CTkButton(app, text="Corrigir provas", command=iniciar_correcao())

app.mainloop()
