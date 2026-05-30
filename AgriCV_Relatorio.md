# AgriCV — Sistema de Recomendação Agrícola Inteligente para Cabo Verde

**Departamento de Ciências da Saúde, Ambiente e Tecnologias**  
**Engenharia Informática | UC: Programação em Lógica**  
**Relatório Final**

---

| Discentes | Docente |
|-----------|---------|
| David Santos — nº 7588 | Valério Santos |
| Natalino Semedo — nº 6423 | |
| Tamiris Évora — nº 8034 | |

**Linguagens:** Python 3 + SWI-Prolog  
**ODS 2 — Fome Zero e Agricultura Sustentável**

---

## 1. Introdução

O objetivo do presente relatório é descrever o processo de desenvolvimento de um sistema inteligente de recomendação agrícola adaptado à realidade de Cabo Verde, denominado AgriCV. O projeto aplica conceitos de lógica formal e programação declarativa na resolução de um problema real, estando alinhado com o ODS 2 — Fome Zero e Agricultura Sustentável.

Cabo Verde apresenta desafios significativos no setor agrícola, nomeadamente:

- Clima árido e irregularidade das chuvas.
- Predominância de agricultura de sequeiro e regadio.
- Diferenças climáticas entre as 9 ilhas habitadas.
- Necessidade de melhor aproveitamento dos recursos hídricos disponíveis.
- Falta de ferramentas digitais de apoio à decisão agrícola local.

Neste contexto, o AgriCV surge como uma ferramenta de apoio à decisão agrícola, ajudando agricultores a saber o que plantar, quando plantar e como gerir os recursos da sua ilha.

---

## 2. Objetivos do Projeto

### 2.1 Objetivo Geral

Desenvolver um sistema baseado em lógica que recomende culturas agrícolas adequadas a cada ilha de Cabo Verde, contribuindo para a sustentabilidade e segurança alimentar do país.

### 2.2 Objetivos Específicos

- Aplicar conceitos de programação em lógica.
- Utilizar Prolog como linguagem declarativa para modelação do conhecimento agrícola.
- Integrar Prolog com Python para criar uma interface acessível ao utilizador.
- Considerar variáveis reais do contexto cabo-verdiano: ilhas, climas, épocas e culturas.
- Contribuir para o ODS 2 — Fome Zero e Agricultura Sustentável.

---

## 3. Enquadramento com o ODS 2

O sistema AgriCV contribui diretamente para o ODS 2 ao:

- Apoiar decisões agrícolas mais eficientes e informadas.
- Reduzir o risco de plantar culturas inadequadas para a época ou ilha.
- Promover o uso racional dos recursos hídricos através de dicas de rega.
- Incentivar práticas agrícolas sustentáveis adaptadas ao clima local.
- Aumentar a produtividade agrícola de forma inteligente e acessível.

---

## 4. Enquadramento Teórico

O sistema baseia-se em três pilares fundamentais da programação em lógica:

- **Factos** — informação declarada sobre as ilhas, culturas, climas e épocas.  
  Exemplo: `cultura(santiago, milho, sequeiro, chuvosa).`

- **Regras** — relações lógicas entre factos que permitem inferir nova informação.  
  Exemplo: `recomendar(Ilha, Tipo, Mes, Cultura) :- ilha(Ilha), cultura(Ilha, Cultura, Tipo, Epoca).`

- **Consultas** — perguntas feitas ao sistema para obter recomendações.  
  Exemplo: `recomendar(santiago, sequeiro, agosto, Cultura).`

O motor de inferência do Prolog percorre automaticamente os factos e aplica as regras para encontrar todas as respostas válidas, sem necessidade de programar explicitamente cada caso.

---

## 5. Descrição do Sistema

O AgriCV é um sistema que recomenda culturas agrícolas com base em três dados fornecidos pelo utilizador: a ilha onde se encontra, o tipo de agricultura que pratica (sequeiro ou regadio), e o mês do ano.

### 5.1 Fluxo de Execução

```
Utilizador → Interface Python → Consulta Prolog → Inferência Lógica → Resultado
```

1. O utilizador insere o seu nome e é registado no sistema.
2. O utilizador escolhe a ilha, o tipo de agricultura e o mês.
3. O Python envia os dados ao Prolog através da biblioteca pyswip.
4. O Prolog identifica a época (seca ou chuvosa) com base no mês.
5. O Prolog aplica as regras da base de conhecimento.
6. O sistema devolve a lista de culturas recomendadas com dicas de rega.
7. A consulta é guardada automaticamente no ficheiro `historico.txt`.

### 5.2 Tecnologias Utilizadas

- **Python 3** — interface, validação e processamento.
- **SWI-Prolog** — motor de inferência lógica e base de conhecimento.
- **PySwip** — biblioteca que liga Python ao SWI-Prolog.
- **Tkinter** — interface gráfica (versão `main_gui.py`).

### 5.3 Estrutura do Projeto

| Ficheiro | Função |
|----------|--------|
| `conhecimento.pl` | Base de conhecimento em Prolog com factos e regras agrícolas. |
| `main.py` | Interface de terminal — versão principal do sistema. |
| `main_gui.py` | Interface gráfica desenvolvida em Tkinter. |
| `consultas.py` | Funções partilhadas de consulta ao Prolog. |
| `README.md` | Documentação com instruções de instalação e uso. |
| `historico.txt` | Ficheiro gerado automaticamente com o histórico de consultas. |

---

## 6. Base de Conhecimento em Prolog

A base de conhecimento é o núcleo do sistema. Está organizada em quatro tipos de factos e três regras principais.

### 6.1 Factos

- **Ilhas** — as 9 ilhas habitadas de Cabo Verde.
- **Épocas** — cada mês é classificado como seca ou chuvosa (julho a outubro).
- **Climas** — cada ilha tem um clima predominante registado.
- **Culturas** — cada cultura está associada a uma ilha, tipo de agricultura e época.

### 6.2 Regras

```prolog
recomendar(Ilha, TipoAgricultura, Mes, Cultura) :-
    ilha(Ilha),
    tipo_agricultura(TipoAgricultura),
    epoca_mes(Mes, Epoca),
    cultura(Ilha, Cultura, TipoAgricultura, Epoca).

identificar_epoca(Mes, Epoca) :- epoca_mes(Mes, Epoca).

identificar_clima(Ilha, Clima) :- clima(Ilha, Clima).
```

### 6.3 Exemplo de Funcionamento

```
Entrada:       Santiago | Sequeiro | Agosto
Processamento: Agosto → Época Chuvosa
Saída:         Milho, Feijão, Abóbora, Mandioca
```

---

## 7. Agricultura em Cabo Verde por Ilha

Cada ilha de Cabo Verde tem condições climáticas e agrícolas muito diferentes. Esta secção descreve a realidade agrícola de cada ilha e explica como o sistema foi adaptado.

---

### 🌿 Santiago — A maior ilha, maior diversidade agrícola

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Sequeiro nas zonas altas do interior e regadio nos vales com acesso a poços e nascentes. |
| **Produtos principais** | Milho, feijão, mandioca, abóbora, batata-doce, cana-de-açúcar, banana, coco, tomate, alface, pimentos, cenoura, couve. |
| **Clima** | Tropical semiárido. Interior mais húmido, litoral mais quente e seco. Época chuvosa de julho a outubro. |
| **Dificuldades** | Erosão do solo, irregularidade das chuvas, pragas como a lagarta do milho. |
| **No sistema** | 13 culturas registadas — a ilha mais representada. |
| **Dica de rega** | Aproveitar poços e nascentes para regadio nos meses secos. |

---

### 🌋 Fogo — Solo vulcânico único, ilha do café e da uva

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Misto. Sequeiro nas zonas baixas e regadio na Chã das Caldeiras. |
| **Produtos principais** | Café, uva, maçã, pêssego, figo, milho, feijão, feijão-congo, hortícolas. |
| **Clima** | Montanhoso. Altitude do vulcão cria microclimas distintos. Chã das Caldeiras mais fria e húmida. |
| **Dificuldades** | Risco de erupções vulcânicas — última em 2014. Transporte caro para exportar. |
| **No sistema** | 9 culturas registadas, incluindo café, uva, maçã, pêssego e figo. |
| **Dica de rega** | Solo vulcânico retém bem a humidade — menos rega necessária. |

---

### 🌿 Santo Antão — A ilha mais verde, maior produtora agrícola

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Principalmente regadio nos vales profundos usando as levadas históricas. |
| **Produtos principais** | Banana, cana-de-açúcar, inhame, batata-doce, hortícolas, café, milho, feijão, couve, cenoura. |
| **Clima** | Húmido montanhoso. Vales do norte muito férteis com neblina frequente. |
| **Dificuldades** | Terreno muito acidentado. Manutenção cara das levadas. Transporte difícil. |
| **No sistema** | 10 culturas registadas — a mais diversificada do sistema. |
| **Dica de rega** | Usar as levadas para irrigação por gravidade — sistema tradicional eficiente. |

---

### 🏙 São Vicente — Cidade e cultura, agricultura limitada

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Quase exclusivamente regadio em pequena escala. Produção em estufas. |
| **Produtos principais** | Tomate, alface, pimentos, couve, cenoura, hortícolas em geral. |
| **Clima** | Seco e árido, muito influenciado pelo vento e pelo Harmatão (vento quente do Sahara). |
| **Dificuldades** | Falta de água. Solo pobre. Vento forte danifica culturas ao ar livre. |
| **No sistema** | 6 culturas de regadio. Representa bem a realidade da ilha. |
| **Dica de rega** | Produzir em estufa para proteger do vento e reduzir evaporação. |

---

### 🐟 Sal — Turismo e deserto, agricultura mínima

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Produção em estufas de pequena escala para hotéis e restaurantes. |
| **Produtos principais** | Tomate e hortícolas em ambiente controlado. |
| **Clima** | Árido. Poucas chuvas, temperatura alta, muito vento, ilha plana. |
| **Dificuldades** | Sem água doce. Toda a rega depende de dessalinização — muito cara. |
| **No sistema** | 2 culturas. Representação honesta da realidade árida. |
| **Dica de rega** | Rega gota-a-gota poupa até 50% da água — essencial nesta ilha. |

---

### 🏖 Boa Vista — Dunas e turismo, quase sem agricultura

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Muito limitada. Apenas hortícolas de regadio em pequena escala. |
| **Produtos principais** | Hortícolas produzidas em zonas protegidas. |
| **Clima** | Árido. Temperatura alta, ventos fortes, chuvas escassas. Muitas dunas. |
| **Dificuldades** | Avanço das dunas sobre os terrenos. Solo sem matéria orgânica. |
| **No sistema** | 1 cultura. Milho e feijão foram removidos por serem inadequados ao clima árido. |
| **Dica de rega** | Cisternas para recolher água da chuva e mulching para reter humidade. |

---

### 🌾 Maio — Planície e tradição agrícola

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Predominantemente sequeiro na planície central. Algum regadio. |
| **Produtos principais** | Milho, feijão, abóbora, amendoim, batata-doce, hortícolas. |
| **Clima** | Seco com chuvas irregulares. Época chuvosa mais curta do que nas ilhas do norte. |
| **Dificuldades** | Irregularidade das chuvas. Falta de mercado para escoar a produção. |
| **No sistema** | 6 culturas — amendoim e batata-doce adicionados na atualização. |
| **Dica de rega** | Cobrir o solo para reter a humidade nos meses secos. |

---

### ☕ Brava — A ilha das flores, clima húmido

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Misto, com destaque para regadio nos vales. Boa humidade graças à altitude. |
| **Produtos principais** | Café, banana, frutas tropicais, milho, feijão, inhame, batata-doce, hortícolas. |
| **Clima** | Húmido montanhoso. Verde durante grande parte do ano. |
| **Dificuldades** | A ilha mais isolada do arquipélago. Ligação marítima irregular. Transporte caro. |
| **No sistema** | 8 culturas — inhame, batata-doce e hortícolas adicionados na atualização. |
| **Dica de rega** | Aproveitar a humidade natural das zonas altas — menos rega artificial necessária. |

---

### 🏔 São Nicolau — Tradição agrícola e cultural

| Campo | Detalhe |
|-------|---------|
| **Tipo de agricultura** | Misto. Zonas altas com mais humidade permitem mais diversidade. |
| **Produtos principais** | Milho, feijão, batata-doce, hortícolas, banana, cana-de-açúcar. |
| **Clima** | Húmido montanhoso nas zonas altas, seco no litoral. |
| **Dificuldades** | Envelhecimento da população agrícola. Emigração dos jovens. |
| **No sistema** | 6 culturas — banana e cana-de-açúcar adicionados na atualização. |
| **Dica de rega** | Regar cedo de manhã para reduzir evaporação durante o calor do dia. |

---

## 8. Erros Identificados e Corrigidos

Durante o desenvolvimento e revisão do projeto foram identificados e corrigidos oito erros. Todos foram resolvidos e aplicados no código final.

---

### ❌ Erro 1 — Santa Luzia incluída como ilha agrícola

**O Erro:** Santa Luzia estava na lista de ilhas com o facto `cultura(santa_luzia, sem_recomendacao_agricola, sequeiro, seca).`

**Porque é um problema:** Santa Luzia é a única ilha desabitada de Cabo Verde. `sem_recomendacao_agricola` aparecia como se fosse o nome de uma cultura, criando confusão ao utilizador.

**A Solução:** Removidas as três linhas referentes a Santa Luzia do ficheiro `conhecimento.pl`.

```prolog
% REMOVIDO:
ilha(santa_luzia).
cultura(santa_luzia, sem_recomendacao_agricola, sequeiro, seca).
clima(santa_luzia, arido).
```

---

### ❌ Erro 2 — Mês 'março' com acento não era reconhecido

**O Erro:** O utilizador digitava `março` mas o Prolog só conhecia `marco`. A função `normalizar_texto()` não resolvia acentos.

**Porque é um problema:** O utilizador recebia "Mês inválido" sem perceber porquê. Escrever "março" é natural e correto em português.

**A Solução:** Criado um menu numerado de meses. O utilizador escolhe 1 a 12 e o Python converte automaticamente para o átomo Prolog correto, sem problemas de acentos.

```python
# ANTES: texto livre com erros de acentuação
mes = input("Digite o mês: ")

# DEPOIS: menu com números sem possibilidade de erro
mostrar_menu_meses()
opcao_mes = input("Escolha o mês: ")
mes = converter_mes(opcao_mes)  # '3' -> 'marco'
```

---

### ❌ Erro 3 — Programa terminava após cada consulta

**O Erro:** Depois de apresentar o resultado, o `main.py` terminava automaticamente.

**Porque é um problema:** O agricultor tinha de reiniciar o programa para cada nova consulta, o que é inconveniente.

**A Solução:** Adicionado ciclo `while True` com pergunta de nova consulta. Os erros de validação usam `continue` em vez de `return`.

```python
while True:
    # ... perguntas e resultados ...
    resposta = input("Deseja fazer nova consulta? (s/n): ")
    if resposta.lower() not in ("s", "sim"):
        print("Obrigado por usar o AgriCV!")
        break
```

---

### ❌ Erro 4 — Código duplicado em main.py e main_gui.py

**O Erro:** A lógica de consulta ao Prolog estava repetida nos dois ficheiros Python.

**Porque é um problema:** Qualquer correção tinha de ser feita em dois sítios, arriscando inconsistências e erros difíceis de detetar.

**A Solução:** Criado o ficheiro `consultas.py` com a função `obter_recomendacao()` partilhada por ambos os ficheiros.

```python
# consultas.py — lógica partilhada
def obter_recomendacao(prolog, ilha, tipo, mes):
    epocas = list(prolog.query(f"identificar_epoca({mes}, Epoca)"))
    if not epocas:
        return None, None, []
    epoca = str(epocas[0]["Epoca"])
    climas = list(prolog.query(f"identificar_clima({ilha}, Clima)"))
    clima = str(climas[0]["Clima"]) if climas else "nao_definido"
    resultados = list(prolog.query(f"recomendar({ilha},{tipo},{mes},Cultura)"))
    return epoca, clima, resultados
```

---

### ❌ Erro 5 — Boa Vista com culturas inadequadas ao clima árido

**O Erro:** A Boa Vista tinha milho e feijão registados, mas a ilha é praticamente árida.

**Porque é um problema:** Recomendar culturas que não crescem bem na ilha induz o agricultor em erro e passa uma imagem incorreta da realidade agrícola da Boa Vista.

**A Solução:** Removidas as linhas de milho e feijão. Ficou apenas hortícolas de regadio, que é o único tipo de produção viável.

```prolog
% REMOVIDO — culturas inadequadas:
cultura(boa_vista, milho, sequeiro, chuvosa).
cultura(boa_vista, feijao, sequeiro, chuvosa).

% MANTIDO — única produção viável:
cultura(boa_vista, hortalicas, regadio, seca).
```

---

### ❌ Erro 6 — README sem instruções de instalação

**O Erro:** O README continha apenas o nome do projeto e dos autores.

**Porque é um problema:** Qualquer pessoa que descarregue o projeto não sabe como instalar nem executar o sistema.

**A Solução:** README atualizado com instruções completas de instalação e uso.

```markdown
## Instalação
1. Instalar Python 3
2. Instalar SWI-Prolog
3. pip install pyswip

## Como executar
python main.py       # versão terminal
python main_gui.py   # versão gráfica
```

---

### ❌ Erro 7 — str() em falta nas comparações de dicas de rega

**O Erro:** As dicas de rega por cultura comparavam o átomo Prolog diretamente com string Python sem converter com `str()`.

**Porque é um problema:** O pyswip devolve os átomos Prolog como objetos `Term`, não como strings Python. Sem o `str()`, a comparação é sempre `False` — as dicas de rega nunca aparecem no programa real com o Prolog instalado.

**A Solução:** Adicionado `str()` em todas as comparações das dicas de rega por cultura.

```python
# ANTES — comparação incorreta:
if cultura["Cultura"] == "milho":

# DEPOIS — comparação correta:
if str(cultura["Cultura"]) == "milho":
    print("- Milho: rega a cada 3 dias")
```

---

### ❌ Erro 8 — Programa crashava sem mensagem clara se o Prolog falhasse

**O Erro:** Se o SWI-Prolog não estivesse instalado ou o `conhecimento.pl` não existisse, o programa terminava com uma mensagem técnica que o utilizador não percebe.

**Porque é um problema:** Um utilizador sem conhecimentos técnicos não consegue perceber o que correu mal nem como resolver o problema.

**A Solução:** Adicionado `try/except` no carregamento do Prolog com mensagem clara e instruções.

```python
try:
    prolog = Prolog()
    prolog.consult("conhecimento.pl")
except Exception as e:
    print("Erro ao carregar o sistema.")
    print("Verifique se o SWI-Prolog está instalado.")
    return
```

---

## 9. Melhorias Implementadas

Para além das correções de erros, foram implementadas seis melhorias que tornam o sistema mais útil para a realidade agrícola de Cabo Verde.

---

### 💧 Melhoria 1 — Aviso de Época Seca

Quando o utilizador escolhe sequeiro num mês de época seca, o sistema apresenta um aviso. Em Cabo Verde, as culturas de sequeiro dependem completamente da chuva — plantar em época seca pode resultar em perda total da colheita.

**Como foi implementado:** Adicionado um bloco `if` após obter a época: se `epoca == 'seca'` e `tipo == 'sequeiro'`, o sistema imprime o aviso e usa `continue` para voltar ao menu.

---

### 🌊 Melhoria 2 — Informação sobre Água por Cultura

Após apresentar as culturas recomendadas, o sistema mostra a necessidade de água de cada uma. Foram cobertas 20 culturas diferentes. Esta informação é essencial em Cabo Verde onde a água é escassa.

**Como foi implementado:** Adicionado um loop após os resultados que usa `str()` para converter o átomo Prolog e comparar com o nome de cada cultura, apresentando a informação de rega correspondente.

---

### 📋 Melhoria 3 — Ver Todas as Culturas de uma Ilha

O menu principal foi expandido com a opção 2, que permite ao utilizador ver todas as culturas registadas para uma ilha sem filtrar por tipo ou época.

**Como foi implementado:** Adicionada a opção `2` no menu. Quando selecionada, consulta o Prolog com `cultura(Ilha, Cultura, _, _)` e apresenta a lista sem duplicados.

---

### ☀ Melhoria 4 — Aviso de Risco de Seca por Ilha

Quando o utilizador seleciona uma ilha com risco elevado de seca (Sal, Boa Vista, Maio), o sistema apresenta um aviso. A Brava foi retirada desta lista porque tem clima húmido montanhoso, incompatível com a classificação de risco de seca.

**Como foi implementado:** Adicionada a lista `ilhas_risco = ["sal", "boa_vista", "maio"]` e um bloco `if` que verifica se a ilha está nessa lista.

---

### 👤 Melhoria 5 — Registo do Agricultor e Histórico

O sistema pede o nome do utilizador no início e guarda cada consulta realizada num ficheiro `historico.txt` com modo append — sem apagar consultas anteriores.

**Como foi implementado:** Adicionado `input` do nome antes do ciclo `while`. No final de cada consulta bem-sucedida, os dados são escritos no `historico.txt`.

---

### 🚿 Melhoria 6 — Dicas de Rega por Ilha

No final de cada consulta, o sistema apresenta uma dica de rega personalizada para a ilha selecionada. Por exemplo: levadas em Santo Antão, rega gota-a-gota no Sal, cisternas na Boa Vista.

**Como foi implementado:** Adicionado um dicionário Python com uma dica por cada uma das 9 ilhas.

---

## 10. Interface do Sistema

### 10.1 Versão Terminal (main.py)

A versão de terminal apresenta menus numerados para todas as escolhas, tornando impossível errar a digitação.

```
==========================================
        AgriCV - Sistema Agrícola CV
 Recomendação de Culturas em Cabo Verde
==========================================
O que deseja fazer?
1 - Obter recomendação
2 - Ver todas as culturas de uma ilha
0 - Sair
```

### 10.2 Versão Gráfica (main_gui.py)

A versão gráfica foi desenvolvida em Tkinter com três menus de seleção (combobox) para ilha, tipo de agricultura e mês. Os resultados aparecem numa área de texto organizada. Existe também um botão Limpar para repor os campos.

---

## 11. Resultados

- Aplicação correta de lógica declarativa em Prolog com factos, regras e consultas.
- Capacidade de inferência automática — o Prolog encontra as culturas sem programação explícita.
- Integração funcional entre Python e Prolog através da biblioteca pyswip.
- Adaptação real ao contexto cabo-verdiano com 9 ilhas, 2 tipos de agricultura e 12 meses.
- Interface acessível em duas versões: terminal e gráfica.
- Oito erros corrigidos e seis melhorias implementadas.

---

## 12. Limitações

- A base de conhecimento não cobre todas as variedades de culturas existentes em Cabo Verde.
- O sistema não considera dados reais de solo, altitude ou quantidade exata de chuva.
- Não existe integração com dados meteorológicos em tempo real.
- A interface gráfica é simples — sem imagens, mapas ou gráficos.
- O histórico de consultas é guardado em texto simples, sem organização avançada.

---

## 13. Melhorias Futuras

- Integração com dados meteorológicos reais do INMG.
- Expansão da base de conhecimento com mais culturas e variedades locais.
- Desenvolvimento de uma versão web ou aplicação móvel.
- Inclusão de informação sobre pragas e doenças comuns em cada ilha.
- Sistema de recomendação de rotação de culturas para melhorar a saúde do solo.
- Interface com mapas das ilhas para visualização geográfica das recomendações.

---

## 14. Conclusão

O AgriCV é uma aplicação prática dos conceitos de Programação em Lógica, demonstrando como sistemas baseados em regras podem resolver problemas reais. O projeto mostra de forma clara a divisão correta de responsabilidades entre Python e Prolog: o Python cuida da interface e da interação, enquanto o Prolog cuida do conhecimento e da inferência.

Durante o desenvolvimento foram identificados e corrigidos oito erros e implementadas seis melhorias que tornam o AgriCV mais útil para a realidade agrícola de Cabo Verde. A base de conhecimento foi expandida com novas culturas, corrigida nas ilhas com dados inadequados, e o clima de Santiago foi ajustado para tropical semiárido. A lista de ilhas em risco de seca foi também corrigida — a Brava foi removida por ter clima húmido montanhoso, incompatível com a classificação de risco de seca.

> O AgriCV é um primeiro passo concreto na digitalização do apoio à agricultura em Cabo Verde. Com as bases estabelecidas neste projeto, é possível continuar a desenvolver o sistema para ter um impacto real na segurança alimentar do país.

---

## 15. Referências Bibliográficas

- INIDA — Instituto Nacional de Investigação e Desenvolvimento Agrário de Cabo Verde. www.inida.cv
- SWI-Prolog — Documentação oficial. www.swi-prolog.org
- PySwip — Biblioteca Python para SWI-Prolog. https://github.com/yuce/pyswip
- Python 3 — Documentação oficial. www.python.org
- Tkinter — Documentação oficial Python. https://docs.python.org/3/library/tkinter.html
- ODS 2 — Fome Zero e Agricultura Sustentável. www.undp.org/sustainable-development-goals
- Ministério do Ambiente e Agricultura de Cabo Verde — Relatórios agrícolas.
