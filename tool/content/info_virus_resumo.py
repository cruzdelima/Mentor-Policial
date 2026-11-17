# -- coding: utf-8 --
"""Conteúdo-teste: Informática · Vírus e outros códigos maliciosos (malware).

Fonte única: gera o JSON do app e o PDF de revisão. Texto original, com base nas
definições da Cartilha de Segurança para Internet (CERT.br), referência das bancas.
Marcação: **negrito** dentro dos textos.
"""

MATERIAL = {
    "id": "info-malware-01",
    "version": "0.1.0",
    "status": "Aprovado pelo autor",
    "subjectId": "INFO",
    "topicIds": ["INFO-12"],
    "kind": "resumo",
    "title": "Vírus e outros códigos maliciosos",
    "subtitle": "Informática · Segurança da informação",
    "minutes": 50,
    "folder": "informatica_virus",
    "pdf": "informatica_virus.pdf",
    "outName": "Informatica_Virus_RESUMO.pdf",
    "header": "Informática · Vírus e outros códigos maliciosos",
    "coverKicker": "Informática  ·  Segurança da informação",
    "coverTitle": ["Vírus e outros", "códigos maliciosos"],
    "coverSub": ["Resumo direto ao ponto, quadro comparativo, mapa mental", "e 10 questões no estilo Cebraspe com gabarito comentado."],
    "coverItems": [("01", "Teoria", "malware, vírus, worm, bot, trojan, spyware, backdoor, rootkit, ransomware"),
                   ("02", "Resumo", "quadro comparativo e “leve para a prova”"),
                   ("03", "Mapa mental", "uma página para revisar em 5 minutos"),
                   ("04", "Questões", "10 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Malwares, ataques e golpes (Informática)",
    "coverBase": "Base: Cartilha de Segurança para Internet (CERT.br), referência das bancas.",
}

THEORY = [
    {"t": "callout", "style": "exam", "title": "O que a banca cobra",
     "text": "As questões de malware seguem quase sempre as definições da **Cartilha de Segurança para Internet (CERT.br)**. "
             "As pegadinhas se repetem: trocar as características de **vírus** e **worm**; dizer que o **cavalo de troia se replica**; "
             "tratar **firewall como antivírus**; chamar **phishing** de vírus; e afirmar que o **rootkit serve para obter** acesso privilegiado."},

    {"t": "h2", "text": "1. Código malicioso (malware)"},
    {"t": "p", "text": "**Código malicioso (malware)** é todo programa desenvolvido para executar ações danosas e atividades maliciosas em um "
                       "equipamento — computador, celular, servidor ou dispositivo conectado. No dia a dia, “vírus” virou sinônimo de qualquer "
                       "malware; **na prova, vírus é apenas um dos tipos**."},
    {"t": "h3", "text": "Como o malware chega ao equipamento"},
    {"t": "bullets", "items": [
        "**Exploração de vulnerabilidades** de sistemas e programas desatualizados.",
        "**Execução de arquivos infectados**: anexos de e-mail, downloads, mídias removíveis (pen drive).",
        "**Links e páginas maliciosas**, inclusive enviados por contas falsas ou invadidas.",
        "**Aplicativos falsos**, sobretudo os obtidos fora das lojas oficiais.",
        "**Ação direta de um atacante** que invadiu o equipamento.",
        "**Outro malware já instalado**, que baixa ou instala novos códigos maliciosos.",
    ]},
    {"t": "h3", "text": "Por que existem"},
    {"t": "p", "text": "A principal motivação é o **ganho financeiro** (golpes, fraudes bancárias, resgates). Também há coleta de informações "
                       "confidenciais, autopromoção e vandalismo. Além do dano direto, o equipamento infectado passa a servir de "
                       "**intermediário** para golpes, ataques e envio de spam."},

    {"t": "h2", "text": "2. Vírus"},
    {"t": "p", "text": "**Vírus** é um programa ou parte de um programa que se propaga **inserindo cópias de si mesmo** em outros programas e "
                       "arquivos, dos quais passa a fazer parte."},
    {"t": "callout", "style": "key", "title": "Ponto-chave",
     "text": "O vírus **depende da execução do programa ou do arquivo hospedeiro** para se tornar ativo e continuar a infecção. "
             "Sem hospedeiro executado, não há infecção. É isso que o separa do worm."},
    {"t": "p", "text": "Depois de instalado, o vírus pode agir logo ou permanecer **dormente**, manifestando-se só em uma data ou após um "
                       "evento (a chamada **bomba lógica** ou bomba-relógio). A propagação clássica ocorre por mídias removíveis, anexos "
                       "e arquivos compartilhados."},
    {"t": "h3", "text": "Tipos de vírus"},
    {"t": "table", "head": ["Tipo", "Como age"], "widths": [0.27, 0.73], "rows": [
        ["Propagado por e-mail", "Chega como anexo. Ao ser executado, infecta o equipamento e envia cópias de si para os contatos da vítima."],
        ["De script", "Escrito em linguagem de script (como JavaScript ou VBScript). Vem em páginas web ou e-mails em HTML e pode ser executado automaticamente, conforme a configuração do navegador ou do leitor de e-mails."],
        ["De macro", "Usa a linguagem de macro de aplicativos como editores de texto, planilhas e apresentações (ex.: pacote Office). Ativa-se quando o documento é aberto com macros habilitadas."],
        ["De telefone celular", "Propaga-se entre celulares por Bluetooth ou mensagens (MMS); ao ser instalado, pode destruir dados, fazer ligações e gastar a bateria."],
        ["De boot", "Infecta o setor de inicialização do disco e é carregado antes do sistema operacional."],
        ["Polimórfico (mutante)", "Altera a própria assinatura a cada infecção para escapar dos antivírus que detectam por assinatura."],
        ["Stealth (furtivo)", "Usa técnicas para se esconder da detecção, por exemplo interceptando as consultas do antivírus."],
    ]},
    {"t": "note", "text": "A Cartilha do CERT.br lista os quatro primeiros tipos; boot, polimórfico e stealth são classificações da literatura que também aparecem em provas."},

    {"t": "h2", "text": "3. Worm"},
    {"t": "p", "text": "**Worm** é um programa que **se propaga sozinho pelas redes**, enviando cópias de si mesmo de equipamento para equipamento."},
    {"t": "bullets", "items": [
        "**Não se insere em outros arquivos** e **não depende de execução**: propaga-se pela execução direta de suas cópias ou pela **exploração automática de vulnerabilidades**.",
        "Efeito típico: **grande consumo de recursos** (rede, processamento, disco), degradando o desempenho de redes e equipamentos.",
        "Ciclo de propagação: identifica alvos, envia cópias, ativa as cópias e reinicia o processo a partir de cada novo equipamento infectado.",
    ]},
    {"t": "callout", "style": "trap", "title": "Pegadinha: vírus × worm",
     "text": "**Vírus**: precisa de hospedeiro e de execução. **Worm**: é autônomo, viaja pela rede e explora falhas. "
             "Se a assertiva disser que o worm “depende da execução do arquivo pelo usuário”, está errada."},

    {"t": "h2", "text": "4. Bot e botnet"},
    {"t": "p", "text": "**Bot** é um programa que, além de se propagar de forma parecida com o worm, tem **mecanismos de comunicação com o invasor** "
                       "(por servidores web, redes P2P ou IRC), o que permite **controlar o equipamento remotamente**. O equipamento infectado "
                       "é chamado de **zumbi**, porque obedece ao atacante sem que o dono perceba."},
    {"t": "p", "text": "**Botnet** é a rede formada por muitos zumbis. Quanto maior, maior o poder de fogo. Usos típicos: **ataques distribuídos de "
                       "negação de serviço (DDoS)**, envio de spam e phishing, propagação de malware, coleta de dados e mineração de criptomoedas."},

    {"t": "h2", "text": "5. Cavalo de troia (trojan)"},
    {"t": "p", "text": "**Cavalo de troia** é um programa que, além de executar as funções para as quais aparentemente foi projetado (um jogo, "
                       "um cartão virtual, um utilitário), **executa outras funções maliciosas sem o conhecimento do usuário**."},
    {"t": "bullets", "items": [
        "Precisa ser **executado explicitamente** para ser instalado — pelo próprio usuário, enganado pelo disfarce, ou por um invasor.",
        "**Não se replica**: não infecta outros arquivos nem envia cópias de si mesmo.",
    ]},
    {"t": "table", "head": ["Tipo de trojan", "O que faz"], "widths": [0.27, 0.73], "rows": [
        ["Downloader", "Baixa da internet e instala outros códigos maliciosos."],
        ["Dropper", "Instala outros códigos maliciosos que já vêm embutidos no próprio trojan."],
        ["Backdoor", "Abre uma porta para o atacante acessar o equipamento remotamente."],
        ["RAT (Remote Access Trojan)", "Dá ao atacante acesso remoto e interativo, como se ele fosse o próprio usuário."],
        ["DoS", "Instala ferramentas de negação de serviço para atacar terceiros."],
        ["Destrutivo", "Apaga arquivos ou formata o disco, deixando o equipamento inoperante."],
        ["Clicker", "Redireciona a navegação para sites específicos, para gerar acessos ou exibir propagandas."],
        ["Proxy", "Transforma o equipamento em servidor proxy, usado para navegação anônima e envio de spam."],
        ["Spy", "Instala spywares para coletar informações e enviá-las ao atacante."],
        ["Banker (bancário)", "Coleta dados bancários; ativado quando a vítima acessa o internet banking."],
    ]},

    {"t": "h2", "text": "6. Spyware"},
    {"t": "p", "text": "**Spyware** é um programa que **monitora as atividades** de um sistema e **envia as informações coletadas a terceiros**. "
                       "Pode ser **legítimo**, quando instalado pelo dono com consentimento de quem é monitorado, ou **malicioso**."},
    {"t": "table", "head": ["Tipo", "O que captura"], "widths": [0.27, 0.73], "rows": [
        ["Keylogger", "As **teclas digitadas** no teclado. Costuma ser ativado quando a vítima acessa um site de banco ou de comércio eletrônico."],
        ["Screenlogger", "A **tela** exibida e a **posição do cursor** no momento do clique (ou a região em volta dele). Foi criado para **burlar os teclados virtuais** dos bancos."],
        ["Adware", "Exibe **propagandas**. Pode ser legítimo (patrocínio de software gratuito) ou malicioso (anúncios direcionados a partir do monitoramento da navegação)."],
        ["Stalkerware", "Espiona o dono do dispositivo sem consentimento e repassa os dados a quem o instalou (comum em perseguição e controle abusivo)."],
    ]},

    {"t": "h2", "text": "7. Backdoor"},
    {"t": "p", "text": "**Backdoor** é um programa que **permite o retorno de um invasor** a um equipamento comprometido, por meio de serviços "
                       "criados ou modificados para esse fim. Costuma ser incluído por outros malwares (trojans, worms, bots) ou pelo próprio "
                       "invasor depois da invasão. Programas legítimos de **administração remota**, se mal configurados ou instalados sem "
                       "consentimento, também podem funcionar como backdoor."},

    {"t": "h2", "text": "8. Rootkit"},
    {"t": "p", "text": "**Rootkit** é um **conjunto de programas e técnicas** que permite **esconder e assegurar a presença** de um invasor ou de "
                       "outro código malicioso em um equipamento comprometido. Com ele, o atacante pode:"},
    {"t": "bullets", "items": [
        "**remover evidências** em arquivos de log;",
        "**instalar outros malwares**, como backdoors, para garantir acesso futuro;",
        "**esconder atividades e informações**: arquivos, processos, chaves de registro, conexões de rede;",
        "mapear vulnerabilidades em outros equipamentos e capturar informações da rede (sniffing).",
    ]},
    {"t": "callout", "style": "trap", "title": "Pegadinha do nome",
     "text": "O nome junta **root** (o administrador em sistemas Unix/Linux) e **kit**, mas o rootkit **não serve para obter** acesso "
             "privilegiado — serve para **mantê-lo** escondido."},

    {"t": "h2", "text": "9. Ransomware"},
    {"t": "p", "text": "**Ransomware** torna **inacessíveis os dados** do equipamento, geralmente por **criptografia**, e **exige o pagamento de "
                       "um resgate** (normalmente em criptomoedas, com prazo) para restabelecer o acesso."},
    {"t": "bullets", "items": [
        "**Ransomware locker**: impede o acesso ao equipamento.",
        "**Ransomware crypto**: impede o acesso aos dados, cifrando-os.",
        "Chega por anexos e links, por exploração de vulnerabilidades (algumas variantes se espalham como worm) e por acessos remotos mal protegidos.",
        "**Melhor defesa: backup** atualizado e guardado **fora do alcance** do equipamento infectado, além de manter tudo atualizado. "
        "**Pagar o resgate não garante** a devolução dos dados.",
    ]},

    {"t": "h2", "text": "10. Outros nomes que caem"},
    {"t": "table", "head": ["Termo", "Significado"], "widths": [0.27, 0.73], "rows": [
        ["Exploit", "Código ou técnica que explora uma vulnerabilidade específica de um programa."],
        ["Dia zero (zero-day)", "Vulnerabilidade explorada antes de existir correção disponível."],
        ["Hijacker", "“Sequestra” o navegador: troca a página inicial e o buscador e redireciona a navegação."],
        ["Scareware", "Assusta o usuário com falsos alertas de infecção para induzi-lo a instalar uma “solução” que é, na verdade, maliciosa."],
        ["Bomba lógica", "Trecho de código que dispara uma ação danosa quando ocorre uma condição (data, evento)."],
    ]},
    {"t": "callout", "style": "trap", "title": "Pegadinha: não são malware, são golpes",
     "text": "**Phishing**: mensagens e páginas falsas para induzir a vítima a fornecer dados. **Pharming**: redirecionamento para um site falso, "
             "por exemplo por envenenamento do DNS, mesmo digitando o endereço correto. **Hoax (boato)**: mensagem alarmante e falsa. "
             "Todos usam **engenharia social**; podem ser porta de entrada para malware, mas não são, em si, códigos maliciosos."},

    {"t": "h2", "text": "11. Proteção: o que cada ferramenta faz"},
    {"t": "table", "head": ["Ferramenta", "Faz", "Não faz"], "widths": [0.22, 0.43, 0.35], "rows": [
        ["Antimalware (“antivírus”)", "Detecta, anula e remove códigos maliciosos (por assinatura, heurística e comportamento); isola arquivos em **quarentena**. Atua sobre vários tipos, não só vírus.", "Não dispensa atualização constante; não impede, sozinho, golpes de engenharia social."],
        ["Firewall pessoal", "Filtra as conexões de rede; bloqueia acessos não autorizados e tentativas de worms e bots de se comunicar ou se propagar.", "Não remove vírus de arquivos já infectados."],
        ["Backup", "Permite recuperar os dados — principal defesa contra ransomware.", "Não impede a infecção."],
        ["Atualizações", "Corrigem as vulnerabilidades exploradas por worms, bots e exploits.", "Não protegem contra o usuário que executa um trojan."],
        ["Autenticação em 2 etapas", "Limita o estrago de senhas capturadas por keyloggers e phishing.", "Não remove o malware."],
    ]},
    {"t": "bullets", "items": [
        "Desconfie de links e anexos, mesmo de conhecidos; na dúvida, confirme por outro meio.",
        "Instale aplicativos só de **lojas oficiais**, conferindo nome e desenvolvedor.",
        "Use a conta de administrador só quando necessário (**privilégio mínimo**).",
        "Desabilite a autoexecução de mídias removíveis.",
        "Se suspeitar de infecção: rode o antimalware, troque as senhas e, se preciso, reinstale o sistema ou restaure as configurações de fábrica.",
    ]},
]

SUMMARY = [
    {"t": "h2", "text": "Quadro comparativo"},
    {"t": "table", "head": ["Código", "Propaga-se sozinho?", "Marca registrada"], "widths": [0.2, 0.36, 0.44], "rows": [
        ["Vírus", "Não: insere cópias em arquivos e depende da execução do hospedeiro", "Infecta outros programas e arquivos"],
        ["Worm", "**Sim**: envia cópias de si pela rede", "Explora vulnerabilidades; consome recursos"],
        ["Bot", "**Sim**: de forma parecida com o worm", "Controle remoto: zumbi e botnet (DDoS, spam)"],
        ["Cavalo de troia", "Não: precisa ser executado", "Disfarce de programa útil"],
        ["Spyware", "Não", "Monitora e envia dados (keylogger, screenlogger)"],
        ["Backdoor", "Não", "Porta de retorno do invasor"],
        ["Rootkit", "Não", "Esconde e mantém o invasor"],
        ["Ransomware", "Depende da variante", "Cifra os dados e exige resgate"],
    ]},
    {"t": "h2", "text": "Leve para a prova"},
    {"t": "bullets", "items": [
        "Malware é o gênero; **vírus é uma espécie**.",
        "Vírus **depende do hospedeiro** executado; worm **não depende** e se espalha sozinho pela rede.",
        "Worm = **consumo de recursos**; bot = **controle remoto** (zumbi); botnet = **DDoS e spam**.",
        "Cavalo de troia **não se replica**: engana o usuário para ser executado.",
        "Keylogger grava **teclas**; screenlogger grava **tela + clique** e derruba o teclado virtual.",
        "Backdoor garante o **retorno** do invasor; rootkit **esconde e mantém** — não serve para obter root.",
        "Ransomware: **criptografa e pede resgate**; defesa número 1 = **backup**.",
        "Firewall **filtra tráfego**; quem remove vírus é o **antimalware**.",
        "Phishing, pharming e hoax são **golpes**, não malware.",
    ]},
    {"t": "mindmap"},
]

MINDMAP = {
    "root": "CÓDIGOS MALICIOSOS",
    "rootSub": "malware",
    "left": [
        {"label": "Vírus", "items": ["Insere cópias em arquivos", "Depende do hospedeiro executado", "E-mail · script · macro · boot"]},
        {"label": "Worm", "items": ["Propaga-se sozinho pela rede", "Explora vulnerabilidades", "Consome recursos"]},
        {"label": "Bot e botnet", "items": ["Controle remoto: zumbi", "DDoS · spam · mineração"]},
        {"label": "Cavalo de troia", "items": ["Disfarce de programa útil", "Não se replica", "Downloader · dropper · RAT"]},
        {"label": "Ransomware", "items": ["Cifra os dados e pede resgate", "Locker × crypto", "Defesa: backup"]},
    ],
    "right": [
        {"label": "Spyware", "items": ["Keylogger: teclas", "Screenlogger: tela + clique", "Adware · stalkerware"]},
        {"label": "Backdoor", "items": ["Porta de retorno do invasor", "Serviços criados ou alterados"]},
        {"label": "Rootkit", "items": ["Esconde e mantém o invasor", "Não serve para obter root"]},
        {"label": "Golpes (não são malware)", "items": ["Phishing · pharming · hoax", "Engenharia social"]},
        {"label": "Proteção", "items": ["Antimalware + firewall", "Atualizações + backup", "2 etapas · privilégio mínimo"]},
    ],
}

QUIZ = {
    "style": "CE",
    "banca": "estilo Cebraspe",
    "instructions": "Julgue os itens a seguir. No estilo Cebraspe, cada erro anula um acerto: na dúvida, deixe em branco.",
    "questions": [
        {"id": "q1", "answer": "C",
         "text": "Diferentemente do worm, o vírus de computador depende da execução do programa ou do arquivo hospedeiro para se tornar ativo e dar continuidade ao processo de infecção.",
         "comment": "**Certo.** É o traço que separa os dois: o vírus se insere em outros arquivos e só age quando o hospedeiro é executado; o worm é autônomo, envia cópias de si mesmo e explora vulnerabilidades sem precisar de hospedeiro."},
        {"id": "q2", "answer": "E",
         "text": "Os worms propagam-se exclusivamente por meio de anexos de e-mail e dependem de que o usuário execute o arquivo recebido para infectar outros computadores da rede.",
         "comment": "**Errado.** O worm não depende de execução pelo usuário: propaga-se sozinho, enviando cópias de si mesmo e explorando vulnerabilidades automaticamente. O e-mail pode ser um dos meios, mas não o único — “exclusivamente” é o alerta. Quem depende de execução é o vírus."},
        {"id": "q3", "answer": "E",
         "text": "O cavalo de troia caracteriza-se por criar cópias de si mesmo e inseri-las em outros arquivos do computador infectado, o que o torna mais perigoso que o vírus.",
         "comment": "**Errado.** O trojan não se replica: disfarça-se de programa útil e, sem o conhecimento do usuário, executa funções maliciosas, como baixar outros malwares (downloader) ou abrir acesso remoto (RAT). Inserir cópias em outros arquivos é característica do vírus."},
        {"id": "q4", "answer": "C",
         "text": "Um screenlogger pode armazenar a posição do cursor e a imagem exibida no monitor no momento em que o mouse é clicado, o que permite contornar a proteção oferecida pelos teclados virtuais usados em sítios de bancos.",
         "comment": "**Certo.** O screenlogger é o spyware feito para burlar o teclado virtual: ao gravar a tela e o ponto do clique, revela a senha “digitada” com o mouse. O keylogger, por sua vez, registra as teclas do teclado físico."},
        {"id": "q5", "answer": "C",
         "text": "Ransomware é um código malicioso que torna inacessíveis os dados armazenados em um equipamento, geralmente por meio de criptografia, e exige pagamento de resgate para restabelecer o acesso; manter cópias de segurança atualizadas é uma das principais medidas para reduzir os danos causados por esse tipo de ataque.",
         "comment": "**Certo.** É a definição e a principal medida de prevenção: com backup recente, guardado fora do alcance do equipamento infectado, a vítima restaura os dados sem negociar com o criminoso. Pagar o resgate não garante a devolução."},
        {"id": "q6", "answer": "E",
         "text": "O rootkit é utilizado principalmente para obter acesso privilegiado de administrador (root) a um computador; após conseguir esse acesso, ele deixa de atuar no sistema.",
         "comment": "**Errado.** O rootkit serve para esconder e assegurar a presença do invasor ou de outro malware: apaga logs, oculta arquivos e processos, instala backdoors. O nome não indica obtenção de acesso privilegiado, e sim a sua manutenção."},
        {"id": "q7", "answer": "E",
         "text": "Um firewall pessoal corretamente configurado é suficiente para remover os vírus que já tenham infectado arquivos armazenados no disco rígido do computador.",
         "comment": "**Errado.** O firewall filtra o tráfego de rede: bloqueia acessos não autorizados e pode impedir que worms e bots se comuniquem ou se propaguem. Detectar e remover vírus de arquivos é papel do antimalware. As ferramentas se complementam; uma não substitui a outra."},
        {"id": "q8", "answer": "C",
         "text": "Vírus de macro infectam arquivos que suportam linguagem de macro, como documentos de editores de texto e planilhas eletrônicas, e podem ser ativados quando o documento infectado é aberto.",
         "comment": "**Certo.** O vírus de macro usa a linguagem de macro do aplicativo (como no pacote Office) e se ativa quando o documento é aberto com macros habilitadas, podendo infectar outros documentos."},
        {"id": "q9", "answer": "E",
         "text": "Phishing é um tipo de vírus que se instala no computador da vítima para capturar as senhas digitadas no acesso a sítios bancários.",
         "comment": "**Errado.** Phishing não é código malicioso: é golpe de engenharia social, em que o criminoso usa mensagens e páginas falsas para induzir a vítima a fornecer seus dados. Capturar o que é digitado é tarefa de spyware do tipo keylogger."},
        {"id": "q10", "answer": "C",
         "text": "Um computador que integra uma botnet pode ser controlado remotamente pelo atacante e utilizado, por exemplo, em ataques distribuídos de negação de serviço (DDoS) e no envio de spam, muitas vezes sem que o seu usuário perceba.",
         "comment": "**Certo.** O bot mantém um canal de comunicação com o invasor, e o equipamento infectado vira um “zumbi”. Somados, os zumbis formam a botnet, usada em DDoS, spam, propagação de malware e até mineração de criptomoedas."},
    ],
}

SOURCES = [
    "CERT.br — Cartilha de Segurança para Internet: fascículo “Códigos maliciosos” e capítulo “Códigos maliciosos (malware)”. cartilha.cert.br",
    "Texto e questões elaborados para o Taticum (itens inéditos no estilo Cebraspe).",
]
