class Menu:

    @staticmethod
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

    @staticmethod
    def mostrar_menu_meses():
        print("\nMeses do ano:")
        print("1  - Janeiro    2  - Fevereiro  3  - Março")
        print("4  - Abril      5  - Maio       6  - Junho")
        print("7  - Julho      8  - Agosto     9  - Setembro")
        print("10 - Outubro    11 - Novembro   12 - Dezembro")

    @staticmethod
    def mostrar_menu_agricultura():
        print("\nTipos de agricultura:")
        print("1 - Sequeiro")
        print("2 - Regadio")

class Conversor:

    @staticmethod
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
            "9": "brava"
        }
        return ilhas.get(opcao)
    
    @staticmethod
    def converter_mes(opcao):
        meses = {
            "1": "janeiro",
            "2": "fevereiro",
            "3": "marco",
            "4": "abril",
            "5": "maio",
            "6": "junho",
            "7": "julho",
            "8": "agosto",
            "9": "setembro",
            "10": "outubro",
            "11": "novembro",
            "12": "dezembro"
        }
        return meses.get(opcao)
    
    @staticmethod
    def converter_tipo(opcao):
        tipos = {
            "1": "sequeiro",
            "2": "regadio"
        }
        return tipos.get(opcao)

class Historico:

    @staticmethod
    def guardar(nome, ilha, tipo, mes, epoca, clima):
        with open("historico.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{nome} | Ilha: {ilha} | Tipo: {tipo} | "
                f"Mês: {mes} | Época: {epoca} | Clima: {clima}\n"
            )


class Dicas:

    @staticmethod
    def mostrar_dica_rega(ilha):

        dicas_rega = {
            "santo_antao": "Use as levadas para irrigação por gravidade.",
            "santiago": "Aproveite poços e nascentes para regadio.",
            "sal": "Rega gota-a-gota poupa até 50% da água.",
            "boa_vista": "Use cisternas para guardar água da chuva.",
            "fogo": "Solo vulcânico retém bem a humidade.",
            "maio": "Cubra o solo para reter a humidade.",
            "brava": "Aproveite a humidade natural das zonas altas.",
            "sao_nicolau": "Regue cedo de manhã para reduzir evaporação.",
            "sao_vicente": "Produza em estufa para proteger do vento."
        }

        if ilha in dicas_rega:
            print("\nDica de rega:")
            print(dicas_rega[ilha])

class DicasCultura:

    Dicas = {
        "milho": "Milho: rega a cada 3 dias",
        "feijao": "Feijão: tolera períodos sem chuva",
        "alface": "Alface: rega diária necessária",
        "tomate": "Tomate: rega 2x por semana",
        "banana": "Banana: solo húmido permanente",
        "cana_de_acucar": "Cana-de-açúcar: rega frequente necessária",
        "batata_doce": "Batata-doce: rega moderada",
        "hortalicas": "Hortícolas: rega regular 2x por semana",
        "abobora": "Abóbora: rega moderada, tolera alguma seca",
        "mandioca": "Mandioca: muito resistente à seca",
        "coco": "Coco: rega abundante, solo sempre húmido",
        "cafe": "Café: rega regular, evitar excesso",
        "uva": "Uva: rega moderada, solo bem drenado",
        "maca": "Maçã: rega regular nas fases de crescimento",
        "inhame": "Inhame: solo húmido, rega frequente",
        "pimentos": "Pimentos: rega regular 2x por semana",
        "cenoura": "Cenoura: solo húmido, rega moderada",
        "couve": "Couve: rega regular, não tolera seca",
        "amendoim": "Amendoim: tolera períodos secos",
        "feijao_congo": "Feijão-congo: muito resistente à seca"
}

@staticmethod
def mostrar_dicas(resultados):
        print("\nDicas de rega:")
        
        for resultado in resultados:
            cultura = str(resultado["Cultura"])

            if cultura in DicasCultura.Dicas:
                print("- " + DicasCultura.Dicas[cultura])