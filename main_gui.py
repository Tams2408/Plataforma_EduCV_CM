import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from pyswip import Prolog
from consultas import obter_recomendacao


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
        epoca, clima, resultados = obter_recomendacao(prolog, ilha, tipo, mes)

        if epoca is None:
            messagebox.showerror("Erro", "Mês inválido.")
            return

        # Aviso de ilha em risco de seca
        ilhas_risco = ["sal", "boa_vista", "maio"]
        if ilha in ilhas_risco:
            messagebox.showwarning(
                "Aviso de Seca",
                "Esta ilha está em risco elevado de seca.\nConsidere culturas resistentes à falta de água."
            )

        # Aviso de época seca com sequeiro
        if epoca == "seca" and tipo == "sequeiro":
            messagebox.showwarning(
                "Aviso de Época Seca",
                "Época seca identificada.\nSequeiro pode ter resultados limitados.\nConsidere escolher outro tipo de agricultura ou mês."
            )
            return

        epoca_fmt = epoca.replace("_", " ").title()
        clima_fmt = clima.replace("_", " ").title()

        texto = "RESULTADO DA RECOMENDAÇÃO\n"
        texto += "============================\n\n"
        texto += f"Ilha: {ilha_nome}\n"
        texto += f"Tipo de agricultura: {tipo_nome}\n"
        texto += f"Mês: {mes_nome}\n"
        texto += f"Época identificada: {epoca_fmt}\n"
        texto += f"Clima predominante: {clima_fmt}\n\n"

        if resultados:
            texto += "Culturas recomendadas:\n"
            for resultado in resultados:
                cultura = str(resultado["Cultura"]).replace("_", " ").title()
                texto += f"- {cultura}\n"
        else:
            texto += "Não foram encontradas culturas recomendadas para estes dados.\n"

        # Dicas de rega por cultura
        dicas_cultura = {
            "milho":        "- Milho: rega a cada 3 dias",
            "feijao":       "- Feijão: tolera períodos sem chuva",
            "alface":       "- Alface: rega diária necessária",
            "tomate":       "- Tomate: rega 2x por semana",
            "banana":       "- Banana: solo húmido permanente",
            "cana_de_acucar": "- Cana-de-açúcar: rega frequente necessária",
            "batata_doce":  "- Batata-doce: rega moderada",
            "hortalicas":   "- Hortícolas: rega regular 2x por semana",
            "abobora":      "- Abóbora: rega moderada, tolera alguma seca",
            "mandioca":     "- Mandioca: muito resistente à seca",
            "coco":         "- Coco: rega abundante, solo sempre húmido",
            "cafe":         "- Café: rega regular, evitar excesso",
            "uva":          "- Uva: rega moderada, solo bem drenado",
            "maca":         "- Maçã: rega regular nas fases de crescimento",
            "inhame":       "- Inhame: solo húmido, rega frequente",
            "pimentos":     "- Pimentos: rega regular 2x por semana",
            "cenoura":      "- Cenoura: solo húmido, rega moderada",
            "couve":        "- Couve: rega regular, não tolera seca",
            "amendoim":     "- Amendoim: tolera períodos secos",
            "feijao_congo": "- Feijão-congo: muito resistente à seca",
            "pessego":      "- Pêssego: rega regular, solo bem drenado",
            "figo":         "- Figo: tolera seca moderada",
            "frutas":       "- Frutas: rega moderada conforme a variedade",
        }

        texto += "\nNecessidade de água:\n"
        for resultado in resultados:
            nome_cultura = str(resultado["Cultura"])
            if nome_cultura in dicas_cultura:
                texto += dicas_cultura[nome_cultura] + "\n"

        # Dicas de rega por ilha
        dicas_rega = {
            "santo_antao": "Dica de rega: Use as levadas para irrigação por gravidade.",
            "santiago":    "Dica de rega: Aproveite poços e nascentes para regadio.",
            "sal":         "Dica de rega: Rega gota-a-gota poupa até 50% da água.",
            "boa_vista":   "Dica de rega: Use cisternas para guardar água da chuva.",
            "fogo":        "Dica de rega: Solo vulcânico retém bem a humidade.",
            "maio":        "Dica de rega: Cubra o solo para reter a humidade.",
            "brava":       "Dica de rega: Aproveite a humidade natural das zonas altas.",
            "sao_nicolau": "Dica de rega: Regue cedo de manhã para reduzir evaporação.",
            "sao_vicente": "Dica de rega: Produza em estufa para proteger do vento.",
        }

        if ilha in dicas_rega:
            texto += f"\n{dicas_rega[ilha]}\n"

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

try:
    prolog = Prolog()
    prolog.consult("conhecimento.pl")
except Exception as e:
    import sys
    print("Erro ao carregar o sistema.")
    print(f"Detalhe: {e}")
    print("Verifique se o SWI-Prolog está instalado e se o ficheiro conhecimento.pl existe.")
    sys.exit(1)


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
}

tipos = {"Sequeiro": "sequeiro", "Regadio": "regadio"}

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
    "Dezembro": "dezembro",
}


# -------------------------------
# Janela principal
# -------------------------------

janela = tk.Tk()
janela.title("AgriCV - Sistema de Recomendação Agrícola")
janela.state("zoomed")  # tela cheia no Windows

# Pedir nome antes de mostrar a janela
janela.withdraw()  # esconde a janela temporariamente
nome_usuario = simpledialog.askstring(
    "Bem-vindo ao AgriCV",
    "Digite o seu nome:",
    parent=janela
)

# Validar nome
if not nome_usuario or not nome_usuario.strip():
    nome_usuario = "Utilizador"
else:
    nome_usuario = nome_usuario.strip()

janela.deiconify()  # mostra a janela novamente

# Título com boas-vindas
titulo = tk.Label(
    janela,
    text="🌿 AgriCV",
    font=("Arial", 28, "bold"),
    fg="#1B5E20"
)
titulo.pack(pady=10)

boas_vindas = tk.Label(
    janela,
    text=f"Bem-vindo(a), {nome_usuario}!",
    font=("Arial", 14),
    fg="#2E7D32"
)
boas_vindas.pack(pady=2)

subtitulo = tk.Label(
    janela,
    text="Sistema de Recomendação Agrícola para Cabo Verde",
    font=("Arial", 12),
    fg="#555555"
)
subtitulo.pack(pady=5)

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=20)

ilha_var = tk.StringVar()
tipo_var = tk.StringVar()
mes_var = tk.StringVar()

tk.Label(frame_formulario, text="Ilha:", font=("Arial", 11)).grid(
    row=0, column=0, padx=10, pady=10, sticky="e"
)
combo_ilha = ttk.Combobox(
    frame_formulario,
    textvariable=ilha_var,
    values=list(ilhas.keys()),
    state="readonly",
    width=30,
)
combo_ilha.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Tipo de agricultura:", font=("Arial", 11)).grid(
    row=1, column=0, padx=10, pady=10, sticky="e"
)
combo_tipo = ttk.Combobox(
    frame_formulario,
    textvariable=tipo_var,
    values=list(tipos.keys()),
    state="readonly",
    width=30,
)
combo_tipo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_formulario, text="Mês:", font=("Arial", 11)).grid(
    row=2, column=0, padx=10, pady=10, sticky="e"
)
combo_mes = ttk.Combobox(
    frame_formulario,
    textvariable=mes_var,
    values=list(meses.keys()),
    state="readonly",
    width=30,
)
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
    font=("Arial", 11, "bold"),
)
botao_consultar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_campos,
    width=15,
    bg="#757575",
    fg="white",
    font=("Arial", 11, "bold"),
)
botao_limpar.grid(row=0, column=1, padx=10)

resultado_texto = tk.Text(janela, width=90, height=20, font=("Arial", 10))
resultado_texto.pack(pady=20)

rodape = tk.Label(
    janela,
    text="Python + SWI-Prolog | Projeto AgriCV | ODS 2 — Fome Zero",
    font=("Arial", 9),
    fg="#888888"
)
rodape.pack(pady=5)

janela.mainloop()