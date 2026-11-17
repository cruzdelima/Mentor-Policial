# -*- coding: utf-8 -*-
"""Dados da planilha Taticum — ciclo básico."""

CAREERS = [
    # sigla, nome exibido, esfera, escolaridade, banca, discursiva, observação, matérias-marca
    ("PF",  "PF — Polícia Federal",                 "Federal",   "Superior",                 "Cebraspe (2021 e 2025)", "Sim", "Agente: Contabilidade no Bloco III; Estatística e RLM no Bloco I. Escrivão soma Arquivologia (fora do ciclo básico).", "Contabilidade · Estatística · Informática"),
    ("PRF", "PRF — Polícia Rodoviária Federal",      "Federal",   "Superior",                 "Cebraspe (2021)",        "Sim", "Legislação de Trânsito ocupou um bloco inteiro (30 itens) no último edital.", "Trânsito · Física · Ética"),
    ("PPF", "PPF — Polícia Penal Federal",           "Federal",   "Superior (Lei 14.875/24)", "Cebraspe (2020)",        "Sim", "Último edital em 2020; novo concurso solicitado. Execução Penal é a matéria-marca.", "Execução Penal · Direitos Humanos"),
    ("PC",  "PC — Polícia Civil (agente/escrivão/investigador)", "Estadual", "Superior (maioria dos estados)", "Varia por estado", "Sim", "Penal, Processual Penal e Leis Especiais pesam; Criminologia e Medicina Legal em parte dos estados.", "Penal · Processo Penal · Leis especiais"),
    ("PM",  "PM — Polícia Militar (soldado)",        "Estadual",  "Médio ou superior (varia)", "Varia por estado",       "Sim", "Soldado: Matemática e conhecimentos gerais pesam; História/Geografia do estado vêm com o edital. Oficial (CFO): nível superior (vários estados exigem Direito); Constitucional, Administrativo e Penal Militar pesam.", "Matemática · Conhecimentos gerais"),
    ("BM",  "BM — Bombeiro Militar (soldado)",       "Estadual",  "Médio ou superior (varia)", "Varia por estado",       "Sim", "Soldado: Física e ciências da natureza pesam; Direito em noções. Oficial (CFO): nível superior; Matemática, Física, Química e legislação militar do estado pesam.", "Física · Matemática"),
    ("PP",  "PP — Polícia Penal Estadual",           "Estadual",  "Médio ou superior (varia)", "Varia por estado",       "Sim", "Execução Penal (LEP) é a matéria-marca.", "Execução Penal (LEP)"),
    ("GCM", "GCM — Guarda Civil Municipal",          "Municipal", "Médio (maioria)",          "Varia por município",    "Não", "Lei 13.022/14 (Estatuto Geral das Guardas) + legislação municipal.", "Lei 13.022/14 · legislação municipal"),
]
CODES = [c[0] for c in CAREERS]

# sigla, nome, cor (tom claro p/ faixa), cor forte, pesos por carreira (ordem CODES)
SUBJECTS = [
    ("LP",   "Língua Portuguesa",                 "EAF1FB", "1F4E79", [3,3,3,3,3,3,3,3]),
    ("RLM",  "Raciocínio Lógico e Matemática",    "EEF5E9", "38761D", [2,2,2,2,3,3,2,3]),
    ("INFO", "Informática",                       "E8F4F8", "0B6E8A", [3,2,2,2,2,2,2,2]),
    ("DC",   "Direito Constitucional",            "FDF3E1", "B45F06", [2,2,2,2,2,1,2,2]),
    ("DA",   "Direito Administrativo",            "FBEFEA", "A0412D", [2,2,2,2,1,1,2,1]),
    ("DP",   "Direito Penal",                     "F9EAEA", "990000", [2,2,2,3,2,1,2,2]),
    ("DPP",  "Direito Processual Penal",          "F3ECF7", "674EA7", [2,2,2,3,1,0,2,1]),
    ("LPE",  "Legislação Penal Especial",         "FCEFF5", "A64D79", [2,2,2,3,2,1,2,2]),
    ("DH",   "Direitos Humanos",                  "EAF6F4", "13756A", [1,1,2,1,2,1,2,2]),
    ("EST",  "Estatística",                       "EEF0FA", "3C4FA0", [2,0,0,0,0,0,0,0]),
    ("CONT", "Contabilidade",                     "F1F6E6", "5B7F1A", [3,0,0,0,0,0,0,0]),
    ("TRAN", "Legislação de Trânsito",            "FFF6DD", "B7860B", [0,3,0,0,0,0,0,1]),
    ("FIS",  "Física",                            "EDF2F7", "45607A", [0,2,0,0,0,2,0,0]),
    ("LEP",  "Execução Penal",                    "F4EFEA", "7A5230", [0,0,3,0,0,0,3,0]),
    ("INST", "Legislação Institucional",          "EFEFF3", "4A4A68", [0,0,1,1,2,2,1,2]),
    ("GER",  "Conhecimentos Gerais e Ética",      "F2F2EC", "6B6B3A", [0,1,1,0,2,2,1,2]),
    ("CRIM", "Criminologia e Medicina Legal",     "F6ECEC", "7F2F2F", [0,0,0,1,0,0,0,0]),
]

NEON = {"LP":"7FB2FF","RLM":"6EE7A8","INFO":"5EEAD4","DC":"FBBF77","DA":"F9A58A","DP":"FB8C8C","DPP":"C4B5FD","LPE":"F9A8D4",
        "DH":"67D8C8","EST":"A5B4FC","CONT":"BEF264","TRAN":"FDE047","FIS":"93C5FD","LEP":"E0BE94","INST":"CBD5E1","GER":"E5E7A0","CRIM":"FCA5A5"}

# (sigla, assunto, tamanho, só para)
T = []
def add(sig, items):
    for it in items:
        name, size = it[0], it[1]
        scope = it[2] if len(it) > 2 else ""
        T.append((sig, name, size, scope))

add("LP", [
    ("Ortografia oficial", "P"),
    ("Acentuação gráfica", "P"),
    ("Classes de palavras: substantivo, adjetivo, artigo e numeral", "M"),
    ("Pronomes: emprego e colocação pronominal", "M"),
    ("Compreensão e interpretação de textos", "G"),
    ("Verbos: flexão, tempos, modos e vozes", "M"),
    ("Advérbio, preposição e conjunção", "M"),
    ("Análise sintática: termos da oração", "G"),
    ("Orações coordenadas", "M"),
    ("Orações subordinadas", "G"),
    ("Concordância nominal e verbal", "G"),
    ("Regência nominal e verbal", "M"),
    ("Crase", "M"),
    ("Pontuação", "M"),
    ("Tipologia e gêneros textuais", "P"),
    ("Coesão e coerência textual", "M"),
    ("Reescrita de frases e parágrafos", "G"),
    ("Estrutura e formação de palavras", "P"),
    ("Semântica e significação das palavras", "P"),
    ("Redação oficial (Manual da Presidência)", "M"),
])
add("RLM", [
    ("Proposições e conectivos lógicos", "M"),
    ("Tabela-verdade, tautologia e contradição", "M"),
    ("Equivalências lógicas e Leis de De Morgan", "M"),
    ("Negação de proposições", "P"),
    ("Lógica de argumentação", "M"),
    ("Quantificadores e diagramas lógicos", "M"),
    ("Conjuntos e operações", "P"),
    ("Razão, proporção, regra de três e porcentagem", "M"),
    ("Problemas aritméticos e equações", "M"),
    ("Sequências e progressões", "P"),
    ("Princípios de contagem e análise combinatória", "G"),
    ("Probabilidade", "G"),
    ("Funções: afim, quadrática, exponencial e logarítmica", "M", "PRF PM BM"),
    ("Geometria plana e espacial", "M", "PM BM GCM PP"),
])
add("INFO", [
    ("Hardware e software: conceitos básicos", "P"),
    ("Windows: arquivos, pastas e atalhos", "M"),
    ("Linux: conceitos e comandos básicos", "M"),
    ("Editores de texto (Word/Writer)", "M"),
    ("Planilhas (Excel/Calc)", "G"),
    ("Internet, intranet e extranet", "P"),
    ("Navegadores, ferramentas de busca e correio eletrônico", "M"),
    ("Redes de computadores: conceitos, topologias e equipamentos", "G"),
    ("Protocolos e modelos TCP/IP e OSI", "M"),
    ("Computação em nuvem", "M"),
    ("Segurança da informação: princípios e conceitos", "P"),
    ("Malwares, ataques e golpes", "M"),
    ("Firewall, antivírus, backup e mecanismos de segurança", "M"),
    ("Criptografia, assinatura e certificado digital", "M"),
    ("Banco de dados: conceitos e modelo relacional", "M", "PF"),
    ("SQL básico", "M", "PF"),
    ("Big Data, mineração de dados e BI", "M", "PF"),
    ("Inteligência artificial e machine learning (noções)", "M", "PF"),
    ("Programação: Python e R (noções)", "M", "PF"),
    ("Teoria geral de sistemas e análise de informação", "P", "PF"),
])
add("DC", [
    ("Princípios fundamentais (arts. 1º a 4º)", "P"),
    ("Direitos e deveres individuais e coletivos (art. 5º)", "G"),
    ("Remédios constitucionais", "M"),
    ("Direitos sociais (arts. 6º a 11)", "P"),
    ("Nacionalidade (arts. 12 e 13)", "P"),
    ("Direitos políticos e partidos (arts. 14 a 17)", "M"),
    ("Organização político-administrativa do Estado (arts. 18 a 33)", "M"),
    ("Administração Pública e servidores (arts. 37 a 41)", "G"),
    ("Poder Legislativo e processo legislativo", "M", "PF PRF PPF PC"),
    ("Poder Executivo", "M", "PF PRF PPF PC"),
    ("Poder Judiciário e funções essenciais à Justiça", "M", "PF PRF PPF PC PP"),
    ("Defesa do Estado: estados de defesa e de sítio, Forças Armadas", "P"),
    ("Segurança Pública (art. 144)", "M"),
])
add("DA", [
    ("Estado, governo e Administração Pública", "P"),
    ("Princípios da Administração Pública", "M"),
    ("Organização administrativa: Administração direta e indireta", "M"),
    ("Agentes públicos: conceito, cargos e regime jurídico", "M"),
    ("Lei 8.112/90 (servidores públicos federais)", "G", "PF PRF PPF"),
    ("Poderes administrativos e poder de polícia", "M"),
    ("Atos administrativos", "G"),
    ("Serviços públicos", "P"),
    ("Controle da Administração Pública", "M"),
    ("Responsabilidade civil do Estado", "M"),
    ("Improbidade administrativa (Lei 8.429/92)", "M"),
    ("Processo administrativo (Lei 9.784/99)", "M", "PF PRF PPF PC"),
    ("Licitações e contratos (Lei 14.133/21)", "G", "PF PRF PPF PC PP"),
    ("Bens públicos", "P"),
])
add("DP", [
    ("Princípios do Direito Penal", "P"),
    ("Aplicação da lei penal no tempo e no espaço", "M"),
    ("Teoria do crime: fato típico", "G"),
    ("Ilicitude e excludentes", "M"),
    ("Culpabilidade e imputabilidade", "M"),
    ("Iter criminis: tentativa, desistência e arrependimento", "M"),
    ("Concurso de pessoas", "M"),
    ("Penas: espécies e aplicação", "M"),
    ("Extinção da punibilidade", "P"),
    ("Crimes contra a pessoa", "G"),
    ("Crimes contra o patrimônio", "G"),
    ("Crimes contra a dignidade sexual", "M"),
    ("Crimes contra a fé pública", "M", "PF PRF PPF PC PP"),
    ("Crimes contra a Administração Pública", "G"),
])
add("DPP", [
    ("Princípios e aplicação da lei processual penal", "P"),
    ("Inquérito policial", "G"),
    ("Ação penal", "M"),
    ("Provas", "G"),
    ("Busca e apreensão", "P"),
    ("Prisão em flagrante", "M"),
    ("Prisão preventiva e temporária", "M"),
    ("Medidas cautelares, liberdade provisória e fiança", "M"),
    ("Juiz das garantias e acordo de não persecução penal", "P"),
    ("Jurisdição e competência", "M", "PF PRF PPF PC PP"),
])
add("LPE", [
    ("Lei de Drogas (Lei 11.343/06)", "M"),
    ("Estatuto do Desarmamento (Lei 10.826/03)", "M"),
    ("Crimes hediondos (Lei 8.072/90)", "P"),
    ("Tortura (Lei 9.455/97)", "P"),
    ("Abuso de autoridade (Lei 13.869/19)", "M"),
    ("Organizações criminosas (Lei 12.850/13)", "M"),
    ("Violência doméstica: Lei Maria da Penha (Lei 11.340/06)", "M"),
    ("Interceptação telefônica (Lei 9.296/96)", "P", "PF PRF PPF PC PP"),
    ("Juizados Especiais Criminais (Lei 9.099/95)", "P"),
    ("ECA: ato infracional", "M", "PC PM GCM PP"),
    ("Estatuto da Pessoa Idosa: crimes", "P", "PC PM GCM"),
    ("Crimes ambientais (Lei 9.605/98)", "M", "PF PRF PC PM GCM"),
    ("Lavagem de dinheiro (Lei 9.613/98)", "M", "PF PC"),
    ("Crimes cibernéticos e identificação criminal (Leis 12.737/12 e 12.037/09)", "P", "PF PC"),
    ("Lei de Migração (Lei 13.445/17)", "M", "PF"),
    ("Estatuto da Segurança Privada (Lei 14.967/24)", "P", "PF"),
    ("Controle de produtos químicos (Lei 10.357/01)", "P", "PF"),
])
add("DH", [
    ("Teoria geral dos direitos humanos", "M"),
    ("Direitos humanos na Constituição de 1988", "P"),
    ("Declaração Universal dos Direitos Humanos", "P"),
    ("Convenção Americana (Pacto de San José da Costa Rica)", "M"),
    ("Sistemas global e interamericano de proteção", "M"),
    ("Convenção contra a Tortura", "P"),
    ("Convenções contra a discriminação racial e contra a mulher", "P"),
    ("Uso da força: Lei 13.060/14 e princípios da ONU", "P"),
    ("Refugiados, genocídio e desaparecimento forçado (convenções)", "M", "PF"),
    ("Programa Nacional de Direitos Humanos (PNDH-3)", "P", "PPF PC PM GCM PP"),
])
add("EST", [
    ("Conceitos básicos: população, amostra e variáveis", "P"),
    ("Apresentação de dados: tabelas e gráficos", "P"),
    ("Medidas de posição", "M"),
    ("Medidas de dispersão", "M"),
    ("Assimetria e curtose", "P"),
    ("Probabilidade e distribuições", "G"),
    ("Correlação e regressão linear", "M"),
    ("Amostragem e inferência (noções)", "M"),
])
add("CONT", [
    ("Conceitos, objeto e finalidade", "P"),
    ("Patrimônio e equação patrimonial", "M"),
    ("Atos e fatos contábeis", "M"),
    ("Contas e plano de contas", "M"),
    ("Escrituração e livros contábeis", "M"),
    ("Regimes de caixa e de competência", "P"),
    ("Balancete de verificação", "P"),
    ("Balanço patrimonial", "G"),
    ("Demonstração do resultado do exercício (DRE)", "G"),
    ("Estoques", "M"),
    ("Ativo imobilizado e intangível", "M"),
    ("Estrutura conceitual (CPC 00)", "M"),
    ("Contabilidade pública: NBC TSP (noções)", "M"),
])
add("TRAN", [
    ("Sistema Nacional de Trânsito e disposições preliminares", "M"),
    ("Normas gerais de circulação e conduta", "G"),
    ("Pedestres e condutores de veículos não motorizados", "P", "PRF"),
    ("Sinalização de trânsito", "M"),
    ("Veículos: classificação, registro e licenciamento", "M", "PRF"),
    ("Habilitação", "M", "PRF"),
    ("Infrações de trânsito", "G"),
    ("Penalidades e medidas administrativas", "M"),
    ("Processo administrativo de trânsito", "P", "PRF"),
    ("Crimes de trânsito", "M"),
    ("Resoluções do CONTRAN (principais)", "M", "PRF"),
])
add("FIS", [
    ("Cinemática escalar e vetorial", "G"),
    ("Movimento circular", "M", "PRF"),
    ("Leis de Newton e aplicações", "G"),
    ("Trabalho, potência e energia", "M"),
    ("Quantidade de movimento, impulso e colisões", "M"),
    ("Hidrostática", "M", "BM"),
    ("Termologia e calorimetria", "M", "BM"),
    ("Eletricidade básica", "M", "BM"),
])
add("LEP", [
    ("LEP: objeto, aplicação e classificação", "P"),
    ("Assistência ao preso e ao egresso", "P"),
    ("Trabalho do preso", "M"),
    ("Deveres, direitos e disciplina (faltas e sanções)", "G"),
    ("Regime disciplinar diferenciado (RDD)", "P"),
    ("Órgãos da execução penal", "M"),
    ("Estabelecimentos penais", "M"),
    ("Regimes, progressão e regressão", "G"),
    ("Saídas, remição e livramento condicional", "M"),
    ("Sistema Penitenciário Federal (Lei 11.671/08)", "M", "PPF"),
    ("Regras de Mandela (ONU)", "P"),
])
add("INST", [
    ("Sistema Único de Segurança Pública (Lei 13.675/18)", "M"),
    ("Lei Orgânica Nacional das PMs e CBMs (Lei 14.751/23)", "M", "PM BM"),
    ("Lei Orgânica Nacional das Polícias Civis (Lei 14.735/23)", "M", "PC"),
    ("Estatuto Geral das Guardas Municipais (Lei 13.022/14)", "M", "GCM"),
    ("Polícia Penal Federal (Lei 14.875/24, cap. XII)", "P", "PPF"),
    ("Estatuto ou lei orgânica da sua corporação", "G", "PC PM BM PP GCM"),
    ("Direito Penal Militar (noções)", "M", "PM BM"),
    ("Proteção e defesa civil (Lei 12.608/12)", "P", "BM"),
])
add("GER", [
    ("Ética e moral; ética no serviço público", "M", "PRF PPF PP"),
    ("Geopolítica brasileira", "M", "PRF"),
    ("Língua estrangeira: inglês ou espanhol (interpretação)", "G", "PRF"),
    ("História do estado/município", "M", "PM BM GCM"),
    ("Geografia do estado/município", "M", "PM BM GCM"),
    ("Atualidades: segurança pública, política e economia", "M", "PPF PM BM GCM PP"),
    ("Primeiros socorros (noções)", "P", "BM GCM"),
])
add("CRIM", [
    ("Criminologia: conceito, objeto e métodos", "M"),
    ("Escolas e teorias criminológicas", "G"),
    ("Vitimologia e prevenção do delito", "P"),
    ("Medicina legal: perícias e documentos médico-legais", "P"),
    ("Traumatologia forense", "G"),
    ("Tanatologia", "M"),
    ("Identidade e identificação", "P"),
])
TOPICS = T

LEI_SECA = [
    "CF/88 — arts. 1º a 4º (princípios fundamentais)",
    "CF/88 — art. 5º, incisos I a XV",
    "CF/88 — art. 5º, incisos XVI a XXXV",
    "CF/88 — art. 5º, incisos XXXVI a LVI",
    "CF/88 — art. 5º, incisos LVII a LXXIX e parágrafos",
    "CF/88 — arts. 6º a 11 (direitos sociais)",
    "CF/88 — arts. 12 e 13 (nacionalidade)",
    "CF/88 — arts. 14 a 17 (direitos políticos e partidos)",
    "CF/88 — arts. 18 e 19 (organização do Estado)",
    "CF/88 — arts. 20 a 24 (bens e competências da União)",
    "CF/88 — arts. 25 a 31 (Estados e Municípios)",
    "CF/88 — art. 37 (Administração Pública)",
    "CF/88 — arts. 38 a 41 (servidores públicos)",
    "CF/88 — arts. 136 a 141 (estados de defesa e de sítio)",
    "CF/88 — arts. 142 a 144 (Forças Armadas e Segurança Pública)",
    "CP — arts. 1º a 12 (aplicação da lei penal)",
    "CP — arts. 13 a 25 (crime e excludentes)",
    "CP — arts. 26 a 31 (imputabilidade e concurso de pessoas)",
    "CP — arts. 121 a 129 (crimes contra a vida e lesões)",
    "CP — arts. 138 a 154-B (honra e liberdade individual)",
    "CP — arts. 155 a 180 (crimes contra o patrimônio)",
    "CP — arts. 312 a 327 (crimes funcionais contra a Adm. Pública)",
    "CP — arts. 328 a 337-A (crimes de particular contra a Adm.)",
    "CP — arts. 338 a 359 (crimes contra a Administração da Justiça)",
    "CPP — arts. 1º a 3º-F (aplicação e juiz das garantias)",
    "CPP — arts. 4º a 23 (inquérito policial)",
    "CPP — arts. 24 a 62 (ação penal)",
    "CPP — arts. 155 a 184 (provas e perícias)",
    "CPP — arts. 240 a 250 (busca e apreensão)",
    "CPP — arts. 282 a 300 (prisão: disposições gerais)",
    "CPP — arts. 301 a 310 (prisão em flagrante)",
    "CPP — arts. 311 a 318-B (preventiva e domiciliar)",
    "CPP — arts. 319 a 350 (cautelares diversas e fiança)",
    "Lei 7.960/89 — prisão temporária",
    "Lei 11.343/06 — arts. 27 a 47 (crimes da Lei de Drogas)",
    "Lei 10.826/03 — arts. 12 a 21 (crimes do Estatuto do Desarmamento)",
    "Lei 8.072/90 — crimes hediondos",
    "Lei 9.455/97 — tortura",
    "Lei 13.869/19 — arts. 1º a 8º (abuso de autoridade)",
    "Lei 13.869/19 — arts. 9º a 38 (crimes de abuso de autoridade)",
    "Lei 12.850/13 — arts. 1º a 7º (conceito e colaboração premiada)",
    "Lei 12.850/13 — arts. 8º a 21 (ação controlada, infiltração e crimes)",
    "Lei 11.340/06 — arts. 1º a 24-A (Maria da Penha)",
    "Lei 9.296/96 — interceptação telefônica",
    "Lei 9.099/95 — arts. 60 a 92 (Juizados Especiais Criminais)",
    "Lei 13.060/14 — instrumentos de menor potencial ofensivo",
    "Lei 13.675/18 — arts. 1º a 10 (SUSP)",
    "Lei 8.429/92 — arts. 1º a 13 (improbidade)",
    "Lei 9.784/99 — arts. 1º a 30 (processo administrativo)",
    "Lei 9.784/99 — arts. 31 a 69",
    "Lei 8.112/90 — arts. 1º a 35 (provimento e vacância)",
    "Lei 8.112/90 — arts. 116 a 142 (deveres, proibições e penalidades)",
    "ECA — arts. 103 a 128 (ato infracional)",
    "Lei 9.605/98 — arts. 2º a 28 (disposições gerais)",
    "Lei 9.613/98 — arts. 1º a 17 (lavagem de dinheiro)",
    "Lei 12.037/09 — identificação criminal",
    "CP — arts. 154-A e 154-B (invasão de dispositivo informático)",
    "Lei 13.445/17 — arts. 1º a 4º e 46 a 62 (Lei de Migração)",
    "DUDH — arts. 1º a 30",
    "Pacto de San José (Decreto 678/92) — arts. 1º a 25",
]

HOURS = [("1h",1.0),("1h30",1.5),("2h",2.0),("2h30",2.5),("3h",3.0),("4h",4.0),("5h",5.0),("6h",6.0),("7h",7.0),("8h",8.0)]
DAYS = [("5 dias",5),("6 dias",6),("7 dias",7)]
NIVEIS = ["Iniciante (sem base)","Intermediário","Avançado"]
TIPOS = ["Teoria","Questões","Revisão","Simulado","Lei seca","Discursiva"]
FONTES = ["PDF / livro","Videoaula","Plataforma de questões","Prova anterior","Simulado","Lei seca","Resumo / mapa","Outro"]
STATUS = ["✔ Cumprida","◐ Parcial","✖ Não cumprida"]

# tempos por nível: (Iniciante, Intermediário, Avançado)
TEORIA = {'P': (90, 60, 40), 'M': (150, 100, 70), 'G': (240, 160, 110)}
MINQ = (4.0, 3.0, 2.0)
PARAMS = dict(qP=15,qM=25,qG=40,rev=0.2,h2=40,h3=100,sim_start=4,sim_every=2,disc_start=3,sim_full_h=5)
