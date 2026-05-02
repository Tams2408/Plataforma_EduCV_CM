% ==================================================
% AgriCV - Base de Conhecimento em Prolog
% Sistema de Recomendação Agrícola para Cabo Verde
% ==================================================

% -------------------------------
% Ilhas de Cabo Verde
% -------------------------------

ilha(santiago).
ilha(fogo).
ilha(santo_antao).
ilha(sao_vicente).
ilha(sao_nicolau).
ilha(sal).
ilha(boa_vista).
ilha(maio).
ilha(brava).
ilha(santa_luzia).

% -------------------------------
% Tipos de agricultura
% -------------------------------

tipo_agricultura(sequeiro).
tipo_agricultura(regadio).

% -------------------------------
% Meses e épocas agrícolas
% -------------------------------

epoca_mes(janeiro, seca).
epoca_mes(fevereiro, seca).
epoca_mes(marco, seca).
epoca_mes(abril, seca).
epoca_mes(maio, seca).
epoca_mes(junho, seca).

epoca_mes(julho, chuvosa).
epoca_mes(agosto, chuvosa).
epoca_mes(setembro, chuvosa).
epoca_mes(outubro, chuvosa).

epoca_mes(novembro, seca).
epoca_mes(dezembro, seca).

% -------------------------------
% Clima predominante por ilha
% -------------------------------

clima(santiago, tropical_seco).
clima(fogo, montanhoso).
clima(santo_antao, montanhoso).
clima(sao_vicente, seco).
clima(sao_nicolau, montanhoso).
clima(sal, arido).
clima(boa_vista, arido).
clima(maio, seco).
clima(brava, humido_montanhoso).
clima(santa_luzia, arido).

% -------------------------------
% Culturas por ilha, tipo e época
% cultura(Ilha, Cultura, TipoAgricultura, Epoca).
% -------------------------------

% Santiago
cultura(santiago, milho, sequeiro, chuvosa).
cultura(santiago, feijao, sequeiro, chuvosa).
cultura(santiago, abobora, sequeiro, chuvosa).
cultura(santiago, banana, regadio, seca).
cultura(santiago, coco, regadio, seca).
cultura(santiago, cana_de_acucar, regadio, seca).
cultura(santiago, tomate, regadio, seca).
cultura(santiago, alface, regadio, seca).

% Fogo
cultura(fogo, milho, sequeiro, chuvosa).
cultura(fogo, feijao, sequeiro, chuvosa).
cultura(fogo, uva, regadio, seca).
cultura(fogo, cafe, regadio, seca).
cultura(fogo, maca, regadio, seca).
cultura(fogo, hortalicas, regadio, seca).

% Santo Antao
cultura(santo_antao, milho, sequeiro, chuvosa).
cultura(santo_antao, feijao, sequeiro, chuvosa).
cultura(santo_antao, banana, regadio, seca).
cultura(santo_antao, cana_de_acucar, regadio, seca).
cultura(santo_antao, inhame, regadio, seca).
cultura(santo_antao, batata_doce, regadio, seca).
cultura(santo_antao, hortalicas, regadio, seca).

% Sao Nicolau
cultura(sao_nicolau, milho, sequeiro, chuvosa).
cultura(sao_nicolau, feijao, sequeiro, chuvosa).
cultura(sao_nicolau, batata_doce, regadio, seca).
cultura(sao_nicolau, hortalicas, regadio, seca).

% Sao Vicente
cultura(sao_vicente, hortalicas, regadio, seca).
cultura(sao_vicente, tomate, regadio, seca).
cultura(sao_vicente, alface, regadio, seca).

% Sal
cultura(sal, hortalicas, regadio, seca).
cultura(sal, tomate, regadio, seca).

% Boa Vista
cultura(boa_vista, milho, sequeiro, chuvosa).
cultura(boa_vista, feijao, sequeiro, chuvosa).
cultura(boa_vista, hortalicas, regadio, seca).

% Maio
cultura(maio, milho, sequeiro, chuvosa).
cultura(maio, feijao, sequeiro, chuvosa).
cultura(maio, abobora, sequeiro, chuvosa).
cultura(maio, hortalicas, regadio, seca).

% Brava
cultura(brava, milho, sequeiro, chuvosa).
cultura(brava, feijao, sequeiro, chuvosa).
cultura(brava, cafe, regadio, seca).
cultura(brava, banana, regadio, seca).
cultura(brava, frutas, regadio, seca).

% Santa Luzia
cultura(santa_luzia, sem_recomendacao_agricola, sequeiro, seca).

% -------------------------------
% Regra principal
% -------------------------------

recomendar(Ilha, TipoAgricultura, Mes, Cultura) :-
    ilha(Ilha),
    tipo_agricultura(TipoAgricultura),
    epoca_mes(Mes, Epoca),
    cultura(Ilha, Cultura, TipoAgricultura, Epoca).

% -------------------------------
% Regra para identificar a época
% -------------------------------

identificar_epoca(Mes, Epoca) :-
    epoca_mes(Mes, Epoca).

% -------------------------------
% Regra para identificar o clima
% -------------------------------

identificar_clima(Ilha, Clima) :-
    clima(Ilha, Clima).