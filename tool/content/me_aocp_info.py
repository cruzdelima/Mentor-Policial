# -*- coding: utf-8 -*-
"""Informática · Bloco B das versões Instituto AOCP (múltipla escolha, 5 alternativas). Questões inéditas."""

ME = {}

ME['info_virus_aprof'] = [
    ('C', "O tipo de código malicioso que se propaga inserindo cópias de si mesmo em outros programas ou arquivos e que depende da execução do "
          "programa ou arquivo hospedeiro para se tornar ativo é o",
     ["worm.", "spyware.", "vírus.", "bot.", "rootkit."],
     "O vírus precisa de um hospedeiro e da ação do usuário. O worm se propaga sozinho pela rede."),
    ('A', "O programa capaz de se propagar automaticamente pelas redes, enviando cópias de si mesmo de computador para computador, explorando "
          "vulnerabilidades e sem precisar de hospedeiro, é o",
     ["worm.", "vírus de macro.", "cavalo de troia.", "adware.", "keylogger."],
     "O worm é autônomo e consome muitos recursos da rede."),
    ('E', "O código malicioso que torna inacessíveis os dados armazenados em um equipamento, geralmente por criptografia, e exige pagamento de "
          "resgate para restabelecer o acesso, é o",
     ["spyware.", "backdoor.", "bot.", "rootkit.", "ransomware."],
     "Ransomware: sequestro de dados mediante resgate, em geral em criptomoeda."),
    ('B', "Assinale a alternativa que apresenta corretamente o conceito de cavalo de troia (trojan).",
     ["Programa que se replica sozinho pela rede.", "Programa que, além de executar as funções para as quais foi aparentemente projetado, executa outras, normalmente maliciosas, sem o conhecimento do usuário.",
      "Conjunto de computadores controlados remotamente.", "Programa que exibe propagandas indesejadas.", "Técnica de envio de e-mails em massa."],
     "O trojan se disfarça de programa útil (jogo, cartão virtual, protetor de tela) para instalar códigos maliciosos."),
    ('D', "O spyware que captura e armazena as teclas digitadas pelo usuário, como senhas bancárias, é denominado",
     ["screenlogger.", "adware.", "botnet.", "keylogger.", "sniffer de rede."],
     "Keylogger registra teclas; screenlogger registra a tela e a posição do cursor nos cliques."),
    ('A', "Um computador infectado que pode ser controlado remotamente pelo invasor, integrando uma rede de máquinas usadas em ataques coordenados, "
          "é chamado de",
     ["zumbi (bot), parte de uma botnet.", "honeypot.", "firewall.", "proxy.", "servidor DNS."],
     "Botnets são usadas, por exemplo, em ataques de negação de serviço distribuídos (DDoS)."),
    ('C', "O conjunto de programas e técnicas que permite esconder e assegurar a presença de um invasor ou de outro código malicioso em um "
          "computador comprometido é o",
     ["adware.", "worm.", "rootkit.", "vírus de boot.", "phishing."],
     "Rootkit: esconde atividades e arquivos maliciosos, dificultando a detecção."),
    ('E', "O golpe em que o criminoso envia mensagem que se passa por instituição conhecida, induzindo a vítima a acessar página falsa e informar "
          "dados pessoais e financeiros, é o",
     ["DDoS.", "ransomware.", "worm.", "backdoor.", "phishing."],
     "Phishing é engenharia social: explora a confiança do usuário, não uma falha técnica."),
    ('B', "Assinale a alternativa que apresenta uma medida adequada de prevenção contra códigos maliciosos.",
     ["Desativar as atualizações do sistema operacional.", "Manter o sistema e os programas atualizados e usar antivírus atualizado.",
      "Abrir anexos de remetentes desconhecidos para verificar o conteúdo.", "Usar a mesma senha em todos os serviços.",
      "Desligar o firewall para melhorar o desempenho."],
     "Atualizações corrigem vulnerabilidades; antivírus detecta e remove códigos conhecidos."),
    ('D', "O programa que permite o retorno de um invasor a um computador comprometido, por meio da inclusão de serviços criados ou modificados "
          "para esse fim, é o",
     ["adware.", "keylogger.", "spam.", "backdoor.", "cookie."],
     "Backdoor = “porta dos fundos”, deixada para acesso futuro."),
]

ME['info_virus_resumo'] = [
    ('B', "O malware que depende de um arquivo hospedeiro para se propagar é o",
     ["worm", "vírus", "bot", "rootkit", "spyware"],
     "O worm não precisa de hospedeiro."),
    ('E', "O ransomware caracteriza-se por",
     ["exibir propagandas", "monitorar teclas", "abrir porta para retorno do invasor", "propagar-se pela rede sozinho",
      "sequestrar dados e exigir resgate"],
     "Bloqueia ou criptografa dados."),
    ('A', "O keylogger é um tipo de",
     ["spyware", "worm", "vírus de boot", "ransomware", "firewall"],
     "Registra teclas digitadas."),
    ('D', "O golpe que usa mensagens falsas para obter dados da vítima é o",
     ["worm", "DDoS", "backdoor", "phishing", "rootkit"],
     "Engenharia social."),
    ('C', "Computadores infectados controlados remotamente formam uma",
     ["intranet", "VPN", "botnet", "DMZ", "LAN"],
     "Rede de bots (zumbis)."),
]
