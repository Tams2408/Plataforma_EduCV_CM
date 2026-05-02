import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog


def consultar_recomendacao():
    ilha_nome = ilha_var.get()
    tipo_nome = tipo_var.get()
    mes_nome = mes_var.get()

    if not ilha_nome or not tipo_nome or not mes_nome:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

    ilha = ilhas[ilha_nome]
    tipo = tipos[tipo_nome]
    mes = meses[mes_nome]

    resultado_texto.delete("1.0", tk.END)

    try:
        consulta_epoca = f"identificar_epoca({mes}, Epoca)"
        epocas = list(prolog.query(consulta_epoca))

        if not epocas:
            messagebox.showerror("Erro", "Mês inválido.")
            return

        epoca = str(epocas[0]["Epoca"]).replace("_", " ").title()

        consulta_clima = f"identificar_clima({ilha}, Clima)"
        climas = list(prolog.query(consulta_clima))

        clima = "Não definido"
        if climas:
            clima = str(climas[0]["Clima"]).replace("_", " ").title()

        consulta = f"recomendar({ilha}, {tipo}, {mes}, Cultura)"
        resultados = list(prolog.query(consulta))

        texto = "RESULTADO DA RECOMENDAÇÃO\n"
        texto += "============================\n\n"
        texto += f"Ilha: {ilha_nome}\n"
        texto += f"Tipo de agricultura: {tipo_nome}\n"
        texto += f"Mês: {mes_nome}\n"
        texto += f"Época identificada: {epoca}\n"
        texto += f"Clima predominante: {clima}\n\n"

        if resultados:
            texto += "Culturas recomendadas:\n"
            for resultado in resultados:
                cultura = str(resultado["Cultura"]).replace("_", " ").title()
                texto += f"- {cultura}\n"
        else:
            texto += "Não foram encontradas culturas recomendadas para estes dados.\n"

        resultado_texto.insert(tk.END, texto)

    except Exception as erro:
        messagebox.showerror("Erro", f"Ocorreu um erro na consulta:\n{erro}")


def limpar_campos():
    ilha_var.set("")
    tipo_var.set("")
    mes_var.set("")
    resultado_texto.delete("1.0", tk.END)


# -------------------------------
# Ligação ao Prolog
# -------------------------------

prolog = Prolog()
prolog.consult("conhecimento.pl")


# -------------------------------
# Dados para a interface
# -------------------------------

ilhas = {
    "Santiago": "santiago",
    "Fogo": "fogo",
    "Santo Antão": "santo_antao",
    "São Vicente": "sao_vicente",
    "São Nicolau": "sao_nicolau",
    "Sal": "sal",
    "Boa Vista": "boa_vista",
    "Maio": "maio",
    "Brava": "brava",
    "Santa Luzia": "santa_luzia"
}

tipos = {
    "Sequeiro": "sequeiro",
    "Regadio": "regadio"
}

meses = {
    "Janeiro": "janeiro",
    "Fevereiro": "fevereiro",
    "Março": "marco",
    "Abril": "abril",
    "Maio": "maio",
    "Junho": "junho",
    "Julho": "julho",
    "Agosto": "agosto",
    "Setembro": "setembro",
    "Outubro": "outubro",
    "Novembro": "novembro",
    "Dezembro": "dezembro"
}


# -------------------------------
# Janela principal
# -------------------------------

janela = tk.Tk()
janela.title("AgriCV - Sistema de Recomendação Agrícola")
janela.geometry("700x550")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="AgriCV",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=10)

subtitulo = tk.Label(
    janela,
    text="Sistema de Recomendação Agrícola para Cabo Verde",
    font=("Arial", 12)
)
subtitulo.pack(pady=5)

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=20)

ilha_var = tk.StringVar()
tipo_var = tk.StringVar()
mes_var = tk.StringVar()

tk.Label(frame_formulario, text="Ilha:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
combo_ilha = ttk.Combobox(frame_formulario, textvariable=ilha_var, values=list(ilhas.keys()), state="readonly", width=30)
combo_ilha.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Tipo de agricultura:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
combo_tipo = ttk.Combobox(frame_formulario, textvariable=tipo_var, values=list(tipos.keys()), state="readonly", width=30)
combo_tipo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Mês:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
combo_mes = ttk.Combobox(frame_formulario, textvariable=mes_var, values=list(meses.keys()), state="readonly", width=30)
combo_mes.grid(row=2, column=1, padx=10, pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_consultar = tk.Button(
    frame_botoes,
    text="Consultar Recomendação",
    command=consultar_recomendacao,
    width=25,
    bg="#2e7d32",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_consultar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_campos,
    width=15,
    bg="#757575",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_limpar.grid(row=0, column=1, padx=10)

resultado_texto = tk.Text(janela, width=75, height=15, font=("Arial", 10))
resultado_texto.pack(pady=20)

rodape = tk.Label(
    janela,
    text="Python + SWI-Prolog | Projeto AgriCV",
    font=("Arial", 9)
)
rodape.pack(pady=5)

janela.mainloop()