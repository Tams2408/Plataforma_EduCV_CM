from pyswip import Prolog


def normalizar_texto(texto):
    return texto.lower().strip().replace(" ", "_")


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
    print("10 - Santa Luzia")


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
        "10": "santa_luzia"
    }

    return ilhas.get(opcao)


def mostrar_menu_agricultura():
    print("\nTipos de agricultura:")
    print("1 - Sequeiro")
    print("2 - Regadio")


def converter_tipo(opcao):
    tipos = {
        "1": "sequeiro",
        "2": "regadio"
    }

    return tipos.get(opcao)


def main():
    prolog = Prolog()
    prolog.consult("conhecimento.pl")

    print("==========================================")
    print("        AgriCV - Sistema Agrícola CV")
    print(" Recomendação de Culturas em Cabo Verde")
    print("==========================================")

    mostrar_menu_ilhas()
    opcao_ilha = input("\nEscolha a ilha: ")
    ilha = converter_ilha(opcao_ilha)

    if ilha is None:
        print("\nIlha inválida.")
        return

    mostrar_menu_agricultura()
    opcao_tipo = input("\nEscolha o tipo de agricultura: ")
    tipo = converter_tipo(opcao_tipo)

    if tipo is None:
        print("\nTipo de agricultura inválido.")
        return

    mes = input("\nDigite o mês: ")
    mes = normalizar_texto(mes)

    consulta_epoca = f"identificar_epoca({mes}, Epoca)"
    epocas = list(prolog.query(consulta_epoca))

    if not epocas:
        print("\nMês inválido.")
        return

    epoca = epocas[0]["Epoca"]

    consulta_clima = f"identificar_clima({ilha}, Clima)"
    climas = list(prolog.query(consulta_clima))

    clima = climas[0]["Clima"] if climas else "nao_definido"

    consulta = f"recomendar({ilha}, {tipo}, {mes}, Cultura)"
    resultados = list(prolog.query(consulta))

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

    print("\n==========================================")
    print("Consulta concluída.")
    print("==========================================")


if __name__ == "__main__":
    main()