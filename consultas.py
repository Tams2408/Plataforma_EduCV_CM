def obter_recomendacao(prolog, ilha, tipo, mes):
    
    # Identificar a época do ano
    epocas = list(prolog.query(f"identificar_epoca({mes}, Epoca)"))
    if not epocas:
        return None, None, []
    epoca = str(epocas[0]["Epoca"])

    # Identificar o clima da ilha
    climas = list(prolog.query(f"identificar_clima({ilha}, Clima)"))
    clima = str(climas[0]["Clima"]) if climas else "nao_definido"

    # Obter culturas recomendadas
    resultados = list(prolog.query(f"recomendar({ilha}, {tipo}, {mes}, Cultura)"))

    return epoca, clima, resultados