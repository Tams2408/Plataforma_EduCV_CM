from pyswip import Prolog
from consultas import obter_recomendacao

def mostrar_menu_ilhas():
    print("\nIlhas disponíveis:")
    print("1 - Santiago")
    print("2 - Fogo")
    print("3 - Santo Antão")
    print("4 - São Vicente")
    print("5 - São Nicolau")
    print("6 - Sal")
    print("7 - Boa Vista")
    print("8 - Maio")
    print("9 - Brava")


def converter_ilha(opcao):
    ilhas = {
        "1": "santiago",
        "2": "fogo",
        "3": "santo_antao",
        "4": "sao_vicente",
        "5": "sao_nicolau",
        "6": "sal",
        "7": "boa_vista",
        "8": "maio",
        "9": "brava",
    }

    return ilhas.get(opcao)


def mostrar_menu_meses():
    print("\nMeses do ano:")
    print("1  - Janeiro    2  - Fevereiro  3  - Março")
    print("4  - Abril      5  - Maio       6  - Junho")
    print("7  - Julho      8  - Agosto     9  - Setembro")
    print("10 - Outubro    11 - Novembro   12 - Dezembro")


def converter_mes(opcao):
    meses = {
        "1":  "janeiro",
        "2":  "fevereiro",
        "3":  "marco",
        "4":  "abril",
        "5":  "maio",
        "6":  "junho",
        "7":  "julho",
        "8":  "agosto",
        "9":  "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }
    return meses.get(opcao)



def mostrar_menu_agricultura():
    print("\nTipos de agricultura:")
    print("1 - Sequeiro")
    print("2 - Regadio")


def converter_tipo(opcao):
    tipos = {"1": "sequeiro", "2": "regadio"}

    return tipos.get(opcao)


def main():
    try:
        prolog = Prolog()
        prolog.consult("conhecimento.pl")
    except Exception as e:
        print("Erro ao carregar o sistema.")
        print(f"Detalhe: {e}")
        print("Verifique se o SWI-Prolog está instalado e se o ficheiro conhecimento.pl existe.")
        return

    #Registo do Agricultor
    nome_usuario = input("Digite seu nome: ")
    print(f"\nBem-vindo ao AgriCV, {nome_usuario}!")

    #loop para que o usuário possa fazer várias consultas sem precisar reiniciar o programa
    while True :
        
        print("\nO que deseja fazer?")
        print("1 - Obter recomendação")
        print("2 - Ver todas as culturas de uma ilha")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("\nObrigado por usar o AgriCV!")
            break
        elif opcao == "2":
            mostrar_menu_ilhas()
            opcao_ilha = input("\nEscolha a ilha: ")
            ilha = converter_ilha(opcao_ilha)
            if ilha is None:
                print("\nIlha inválida.")
                continue
            resultados_todos = list(prolog.query(f"cultura({ilha}, Cultura, _, _)"))
            culturas_vistas = []
            print(f"\nTodas as culturas de {ilha.replace('_', ' ').title()}:")
            for r in resultados_todos:
                cultura = str(r["Cultura"]).replace("_", " ").title()
                if cultura not in culturas_vistas:
                    culturas_vistas.append(cultura)
                    print(f"- {cultura}")
            continue
        elif opcao == "1":
            mostrar_menu_ilhas()
            opcao_ilha = input("\nEscolha a ilha: ")
            ilha = converter_ilha(opcao_ilha)

            if ilha is None:
                print("\nIlha inválida.")
                continue

            mostrar_menu_agricultura()
            opcao_tipo = input("\nEscolha o tipo de agricultura: ")
            tipo = converter_tipo(opcao_tipo)

            if tipo is None:
                print("\nTipo de agricultura inválido.")
                continue

            mostrar_menu_meses()
            opcao_mes = input("\nEscolha o mês: ")
            mes = converter_mes(opcao_mes)

            if mes is None:
                print("\nMês inválido.")
                continue

            
            epoca, clima, resultados = obter_recomendacao(prolog, ilha, tipo, mes)
            

            if epoca is None:
                print("\nMês inválido.")
                continue
            
            ilhas_risco = ["sal", "boa_vista", "maio"]

            if ilha in ilhas_risco:
                print("Aviso: Esta ilha está em risco de seca.")
                print("Considere culturas resistentes à falta de água.")

            if epoca == "seca" and tipo == "sequeiro":
                print("Aviso: Epoca seca.")
                print("Sequeiro pode ter resultados limitados. Considere escolher outro tipo de agricultura ou mês.")
                continue

            print("\n==========================================")
            print("Resultado da Recomendação")
            print("==========================================")
            print(f"Ilha: {ilha.replace('_', ' ').title()}")
            print(f"Tipo de agricultura: {tipo.title()}")
            print(f"Mês: {mes.title()}")
            print(f"Época identificada: {str(epoca).title()}")
            print(f"Clima predominante: {str(clima).replace('_', ' ').title()}")

            if resultados:
                print("\nCulturas recomendadas:")
                for resultado in resultados:
                    cultura = str(resultado["Cultura"]).replace("_", " ").title()
                    print(f"- {cultura}")
            else:
                print("\nNão foram encontradas culturas recomendadas para estes dados.")
                print("Pode ser necessário escolher outro mês, ilha ou tipo de agricultura.")

            # Dicas de rega por cultura
            for cultura in resultados:
                if str(cultura["Cultura"]) == "milho":
                    print("- Milho: rega a cada 3 dias")
                elif str(cultura["Cultura"]) == "feijao":
                    print("- Feijão: tolera períodos sem chuva")
                elif str(cultura["Cultura"]) == "alface":
                    print("- Alface: rega diária necessária")
                elif str(cultura["Cultura"]) == "tomate":
                    print("- Tomate: rega 2x por semana")
                elif str(cultura["Cultura"]) == "banana":
                    print("- Banana: solo húmido permanente")
                elif str(cultura["Cultura"]) == "cana_de_acucar":
                    print("- Cana-de-açúcar: rega frequente necessária")
                elif str(cultura["Cultura"]) == "batata_doce":
                    print("- Batata-doce: rega moderada")
                elif str(cultura["Cultura"]) == "hortalicas":
                    print("- Hortícolas: rega regular 2x por semana")
                elif str(cultura["Cultura"]) == "abobora":
                    print("- Abóbora: rega moderada, tolera alguma seca")
                elif str(cultura["Cultura"]) == "mandioca":
                    print("- Mandioca: muito resistente à seca")
                elif str(cultura["Cultura"]) == "coco":
                    print("- Coco: rega abundante, solo sempre húmido")
                elif str(cultura["Cultura"]) == "cafe":
                    print("- Café: rega regular, evitar excesso")
                elif str(cultura["Cultura"]) == "uva":
                    print("- Uva: rega moderada, solo bem drenado")
                elif str(cultura["Cultura"]) == "maca":
                    print("- Maçã: rega regular nas fases de crescimento")
                elif str(cultura["Cultura"]) == "inhame":
                    print("- Inhame: solo húmido, rega frequente")
                elif str(cultura["Cultura"]) == "pimentos":
                    print("- Pimentos: rega regular 2x por semana")
                elif str(cultura["Cultura"]) == "cenoura":
                    print("- Cenoura: solo húmido, rega moderada")
                elif str(cultura["Cultura"]) == "couve":
                    print("- Couve: rega regular, não tolera seca")
                elif str(cultura["Cultura"]) == "amendoim":
                    print("- Amendoim: tolera períodos secos")
                elif str(cultura["Cultura"]) == "feijao_congo":
                    print("- Feijão-congo: muito resistente à seca")
            
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
                print(f"\n{dicas_rega[ilha]}")

            print("\n==========================================")
            print("Consulta concluída.")
            print("==========================================")

            # guardar no ficheiro
            with open("historico.txt", mode="at", encoding="utf-8") as f:
                f.write(nome_usuario + " | Ilha: " + ilha + " | Tipo: " + tipo + " | Mês: " + mes + " | Época: " + epoca + " | Clima: " + clima + "\n")

            print("Consulta guardada, " + nome_usuario + "!")


            resposta = input("\nDeseja fazer nova consulta? (s/n): ")
            if resposta.lower() not in ("s", "sim"):
                print("\nObrigado por usar o AgriCV!")
                break

        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
        

if __name__ == "__main__":
    main()
