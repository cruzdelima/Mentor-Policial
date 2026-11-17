# -- coding: utf-8 --
"""Informática · Vírus e outros códigos maliciosos — MATERIAL APROFUNDADO (estudo inicial)."""
from common import *

MATERIAL = {
    "id": "info-malware-02",
    "version": "0.1.0",
    "status": "Em revisão pelo autor",
    "subjectId": "INFO",
    "topicIds": ["INFO-12"],
    "kind": "aprofundado",
    "title": "Vírus e outros códigos maliciosos",
    "subtitle": "Informática · Segurança da informação",
    "minutes": 150,
    "folder": "informatica_virus_aprofundado",
    "pdf": "informatica_virus_aprofundado.pdf",
    "outName": "Informatica_Virus_APROFUNDADO.pdf",
    "header": "Informática · Vírus e outros códigos maliciosos",
    "coverKicker": "Informática  ·  Segurança da informação",
    "coverTitle": ["Vírus e outros", "códigos maliciosos"],
    "coverSub": ["Teoria completa para o primeiro estudo: malware, ataques, golpes e proteção,", "com 20 questões no estilo Cebraspe e gabarito comentado."],
    "coverItems": [("01", "Fundamentos", "ameaça, vulnerabilidade, risco, ataque e incidente"),
                   ("02", "Malware", "vírus, worm, bot, trojan, spyware, backdoor, rootkit, ransomware"),
                   ("03", "Ataques e golpes", "engenharia social, phishing, pharming, DoS, spoofing, sniffing"),
                   ("04", "Proteção", "antimalware, firewall, backup, atualizações e boas práticas"),
                   ("05", "Questões", "20 itens certo/errado + gabarito comentado")],
    "coverTopic": "Tópico do edital: Malwares, ataques e golpes (Informática)",
    "coverBase": "Base: Cartilha de Segurança para Internet (CERT.br) e literatura de segurança (Stallings).",
}

THEORY = [
    exam("Como estudar este material",
         "Este é o material do **primeiro contato** com o assunto: leia com calma, grife as definições e resolva as 20 questões ao final. "
         "Para as revisões (24 horas, 7 dias e 30 dias), use o **PDF de resumo** do mesmo assunto. "
         "A banca segue as definições da **Cartilha de Segurança para Internet (CERT.br)**; os termos extras vêm da literatura técnica e estão sinalizados."),

    h2("1. Onde o assunto se encaixa"),
    p("Segurança da informação é a proteção da informação contra acessos, alterações e indisponibilidades indevidas. Os três pilares clássicos são "
      "**confidencialidade** (só acessa quem está autorizado), **integridade** (a informação não é alterada indevidamente) e **disponibilidade** "
      "(a informação está acessível quando necessária). A eles costumam se somar **autenticidade** (garantia da origem) e **não repúdio** "
      "(o autor não pode negar o que fez)."),
    p("Os códigos maliciosos são um dos principais meios de violar esses pilares: um spyware quebra a confidencialidade, um vírus que corrompe arquivos "
      "quebra a integridade, um ransomware ou um ataque de negação de serviço quebra a disponibilidade."),
    tb(["Termo", "Significado", "Exemplo"], [0.2, 0.45, 0.35], [
        ("Vulnerabilidade", "Fraqueza que pode ser explorada.", "Sistema sem atualização; senha fraca."),
        ("Ameaça", "Causa potencial de um incidente indesejado.", "Um worm circulando na internet."),
        ("Risco", "Probabilidade de a ameaça explorar a vulnerabilidade, combinada com o impacto.", "Chance de o worm infectar o servidor desatualizado."),
        ("Ataque", "Ação deliberada para explorar uma vulnerabilidade.", "Envio do worm contra a rede."),
        ("Incidente", "Evento adverso, confirmado ou sob suspeita, relacionado à segurança.", "Servidor infectado e fora do ar."),
    ]),

    h2("2. Código malicioso (malware)"),
    p("**Código malicioso**, ou **malware** (de malicious software), é todo programa desenvolvido especificamente para executar ações danosas e "
      "atividades maliciosas em um equipamento. No uso popular, “vírus” virou sinônimo de qualquer praga digital; **para a banca, vírus é só um dos tipos**."),
    h3("Como o malware chega ao equipamento"),
    bl("**Exploração de vulnerabilidades** existentes em programas e sistemas desatualizados.",
       "**Autoexecução de mídias removíveis** infectadas, como pen drives.",
       "**Acesso a páginas maliciosas** com navegadores vulneráveis.",
       "**Execução de arquivos infectados**: anexos de e-mail, downloads, arquivos recebidos por mensagens ou compartilhados em rede.",
       "**Ação direta de atacantes** que, após invadir o equipamento, instalam os códigos.",
       "**Aplicativos falsos**, sobretudo de fora das lojas oficiais.",
       "**Outro malware** já presente, que baixa ou instala novos códigos."),
    p("Uma vez instalado, o código malicioso passa a ter acesso aos dados armazenados e pode executar ações **em nome do usuário, com as permissões "
      "do usuário**. Por isso a recomendação de não usar a conta de administrador no dia a dia."),
    h3("Motivações"),
    p("Obtenção de **vantagens financeiras**, coleta de **informações confidenciais**, desejo de autopromoção e vandalismo. Os equipamentos infectados "
      "também viram **intermediários** para a prática de golpes, a realização de ataques e a disseminação de spam."),
    h3("Três perguntas para classificar qualquer malware"),
    tb(["Pergunta", "O que observar", "Quem se destaca"], [0.26, 0.4, 0.34], [
        ("Como se propaga?", "Depende de hospedeiro e de execução, ou se espalha sozinho?", "Vírus (hospedeiro) × worm e bot (sozinhos)"),
        ("Como se esconde?", "Disfarça-se de programa útil? Oculta arquivos e processos?", "Cavalo de troia e rootkit"),
        ("O que faz (carga)?", "Espiona, abre acesso, sequestra dados, exibe propaganda?", "Spyware, backdoor, ransomware, adware"),
    ]),
    nt("Na prática, as pragas atuais misturam características (um ransomware que se espalha como worm, um trojan que instala um backdoor). "
       "A banca cobra a característica que define cada categoria."),

    h2("3. Vírus"),
    p("**Vírus** é um programa ou parte de um programa de computador, normalmente malicioso, que se propaga **inserindo cópias de si mesmo e se "
      "tornando parte de outros programas e arquivos**."),
    key("Ponto-chave",
        "Para se tornar ativo e continuar o processo de infecção, o vírus **depende da execução do programa ou do arquivo hospedeiro**. "
        "Vírus não age sozinho: precisa de um hospedeiro e de alguém (ou algo) que o execute."),
    h3("Anatomia de um vírus"),
    bl("**Mecanismo de infecção** (vetor): como o vírus se replica e se espalha.",
       "**Gatilho** (trigger): evento ou condição que ativa a carga — uma data, um número de execuções, a abertura de um arquivo. "
       "Quando o disparo depende de data ou evento, fala-se em **bomba lógica** (ou bomba-relógio).",
       "**Carga útil** (payload): o que o vírus faz além de se espalhar — apagar arquivos, exibir mensagens, roubar dados."),
    h3("Ciclo de vida (Stallings)"),
    tb(["Fase", "O que acontece"], [0.25, 0.75], [
        ("1. Dormência", "O vírus está inativo, à espera de um evento. Nem todo vírus passa por essa fase."),
        ("2. Propagação", "Insere cópias de si mesmo em outros programas ou áreas do disco."),
        ("3. Ativação (disparo)", "O gatilho é acionado."),
        ("4. Execução", "A carga é executada: do inofensivo (uma mensagem) ao destrutivo (perda de dados)."),
    ]),
    h3("Tipos de vírus"),
    tb(["Tipo", "Como age", "Fonte"], [0.24, 0.6, 0.16], [
        ("Propagado por e-mail", "Recebido como anexo; induz o usuário a executá-lo. Ao agir, infecta arquivos e envia cópias para os contatos da vítima.", "Cartilha"),
        ("De script", "Escrito em linguagem de script (VBScript, JavaScript); recebido ao acessar página web ou em e-mail em HTML. Pode ser executado automaticamente, conforme a configuração do navegador e do leitor de e-mails.", "Cartilha"),
        ("De macro", "Tipo específico de vírus de script, escrito em linguagem de macro; infecta arquivos de aplicativos que usam essa linguagem (ex.: os do Microsoft Office).", "Cartilha"),
        ("De telefone celular", "Propaga-se de celular para celular por Bluetooth ou MMS. A infecção ocorre quando o usuário permite o recebimento e executa o arquivo.", "Cartilha"),
        ("De arquivo (parasita)", "Anexa-se a arquivos executáveis e se replica quando o programa infectado roda.", "Literatura"),
        ("De boot", "Infecta o setor de inicialização do disco; é carregado antes do sistema operacional.", "Literatura"),
        ("Criptografado", "Parte do código fica cifrada para dificultar a detecção por assinatura.", "Literatura"),
        ("Polimórfico (mutante)", "Muda a própria assinatura a cada infecção, mantendo a função.", "Literatura"),
        ("Metamórfico", "Reescreve-se por completo a cada infecção; pode mudar até o comportamento.", "Literatura"),
        ("Stealth (furtivo)", "Projetado para se esconder do antivírus (por exemplo, devolvendo a ele a versão “limpa” do arquivo).", "Literatura"),
        ("Time bomb", "Programado para agir em data ou momento específicos.", "Literatura"),
    ]),
    trap("Pegadinha: macro",
         "Vírus de macro **não infecta programas executáveis**, e sim **documentos** (textos, planilhas, apresentações). Para a Cartilha, "
         "ele é um **tipo de vírus de script**. Desabilitar a execução automática de macros é a principal prevenção."),

    h2("4. Worm"),
    p("**Worm** (verme) é um programa capaz de **se propagar automaticamente pelas redes**, enviando cópias de si mesmo de equipamento para equipamento."),
    bl("**Não se propaga por meio da inclusão de cópias em outros programas ou arquivos**: propaga-se pela **execução direta de suas cópias** "
       "ou pela **exploração automática de vulnerabilidades** em programas instalados.",
       "**Não precisa de hospedeiro** nem de ação do usuário para se espalhar.",
       "É notadamente responsável por **consumir muitos recursos**: o grande número de cópias afeta o desempenho de redes e a utilização dos equipamentos."),
    h3("Processo de propagação e infecção"),
    tb(["Etapa", "Descrição"], [0.3, 0.7], [
        ("1. Identificação dos alvos", "Varre a rede, usa listas de endereços ou informações do equipamento infectado."),
        ("2. Envio das cópias", "Como parte da exploração de vulnerabilidades, anexado a e-mails, por mensagens instantâneas, em pastas compartilhadas."),
        ("3. Ativação das cópias", "Imediata (pela exploração da vulnerabilidade), pela execução por um usuário ou por uma ação específica dele (como inserir uma mídia)."),
        ("4. Reinício do processo", "O equipamento que era alvo passa a ser também origem de novos ataques."),
    ]),
    trap("Pegadinha: vírus × worm",
         "Guarde o par: **vírus = hospedeiro + execução**; **worm = autônomo + rede + vulnerabilidade**. A banca troca as características "
         "dos dois de todas as formas possíveis."),
    nt("Casos históricos para fixar: o worm de Morris (1988) derrubou boa parte da internet da época; o Stuxnet (2010) atacou sistemas industriais; "
       "o WannaCry (2017) foi um ransomware que se espalhava como worm, explorando uma falha do Windows."),

    h2("5. Bot e botnet"),
    p("**Bot** é um programa que dispõe de **mecanismos de comunicação com o invasor**, permitindo que seja **controlado remotamente**. "
      "O processo de infecção e propagação é **similar ao do worm**: propaga-se automaticamente, explorando vulnerabilidades."),
    bl("A comunicação entre o invasor e o bot pode ocorrer por canais de IRC, servidores web e redes P2P, entre outros. "
       "O ponto central de comando é chamado de **comando e controle (C&C)**.",
       "O equipamento infectado é chamado de **zumbi** (zombie computer), pois pode ser controlado remotamente sem o conhecimento do dono. "
       "Quando o bot o transforma em servidor de e-mails para envio de spam, fala-se em **spam zombie**.",
       "**Botnet** é a rede formada por centenas ou milhares de zumbis, que potencializa as ações danosas dos bots."),
    p("Ações típicas de uma botnet: **ataques de negação de serviço distribuídos (DDoS)**, propagação de códigos maliciosos, coleta de informações, "
      "envio de spam e camuflagem da identidade do atacante (com o uso de proxies instalados nos zumbis). O atacante pode inclusive alugar a botnet a terceiros."),

    h2("6. Cavalo de troia (trojan)"),
    p("**Cavalo de troia** é um programa que, além de executar as funções para as quais foi aparentemente projetado, **também executa outras funções, "
      "normalmente maliciosas, e sem o conhecimento do usuário**. Exemplos: cartões virtuais animados, álbuns de fotos, jogos e protetores de tela."),
    bl("**Precisa ser explicitamente executado** para ser instalado.",
       "**Não se replica** e **não se propaga** sozinho.",
       "Também pode ser instalado por atacantes que, após invadir o equipamento, alteram programas existentes para que executem ações maliciosas."),
    tb(["Tipo de trojan", "O que faz"], [0.27, 0.73], [
        ("Downloader", "Instala outros códigos maliciosos, obtidos de sites na internet."),
        ("Dropper", "Instala outros códigos maliciosos, embutidos no próprio código do trojan."),
        ("Backdoor", "Inclui backdoors, possibilitando o acesso remoto do atacante."),
        ("DoS", "Instala ferramentas de negação de serviço e as utiliza para desferir ataques."),
        ("Destrutivo", "Altera ou apaga arquivos e diretórios, formata o disco e pode deixar o equipamento fora de operação."),
        ("Clicker", "Redireciona a navegação para sites específicos, para aumentar acessos ou apresentar propagandas."),
        ("Proxy", "Instala um servidor proxy, usado para navegação anônima e envio de spam."),
        ("Spy", "Instala spywares e os utiliza para coletar informações sensíveis, como senhas e números de cartão."),
        ("Banker (bancos)", "Coleta dados bancários por meio de spywares ativados quando sites de internet banking são acessados."),
        ("RAT", "Remote Access Trojan: combina trojan e backdoor; dá ao atacante acesso remoto e interativo ao equipamento."),
    ]),

    h2("7. Spyware"),
    p("**Spyware** é um programa projetado para **monitorar as atividades de um sistema e enviar as informações coletadas para terceiros**. "
      "Pode ser usado de forma **legítima** (instalado pelo dono, ou com o consentimento dele, para verificar o uso do equipamento) ou "
      "**maliciosa** (compromete a privacidade do usuário e a segurança do equipamento)."),
    tb(["Tipo", "O que captura", "Detalhe que a banca cobra"], [0.2, 0.4, 0.4], [
        ("Keylogger", "As teclas digitadas no teclado.", "Em muitos casos, a ativação depende de uma ação do usuário, como o acesso a um site de banco."),
        ("Screenlogger", "A posição do cursor e a tela apresentada (ou a região em volta do clique) no momento em que o mouse é clicado.", "Usado para capturar as teclas digitadas em **teclados virtuais**."),
        ("Adware", "Projetado especificamente para apresentar propagandas.", "Legítimo quando incorporado a programas gratuitos como patrocínio; malicioso quando direciona anúncios monitorando a navegação sem o usuário saber."),
        ("Stalkerware", "Tudo o que o dono do dispositivo faz (mensagens, localização, chamadas).", "Instalado por alguém próximo, sem consentimento, para vigiar a vítima."),
    ]),

    h2("8. Backdoor"),
    p("**Backdoor** é um programa que **permite o retorno de um invasor a um equipamento comprometido**, por meio da inclusão de serviços criados "
      "ou modificados para esse fim. Pode ser incluído pela ação de outros códigos maliciosos ou por atacantes que exploram vulnerabilidades."),
    bl("Depois de incluído, garante o acesso futuro **sem que seja preciso repetir os métodos da invasão** e, em geral, sem ser notado.",
       "Programas de **administração remota** (como BackOrifice, NetBus, SubSeven, VNC e Radmin), se mal configurados ou usados sem consentimento, "
       "também podem ser classificados como backdoors.",
       "Há backdoors incluídos pelos próprios fabricantes, sob a alegação de necessidades administrativas; ainda assim, são uma séria ameaça à segurança."),

    h2("9. Rootkit"),
    p("**Rootkit** é um **conjunto de programas e técnicas** que permite **esconder e assegurar a presença** de um invasor ou de outro código "
      "malicioso em um equipamento comprometido. Pode ser usado para:"),
    bl("remover evidências em **arquivos de log**;",
       "instalar outros códigos maliciosos, como **backdoors**, para assegurar o acesso futuro;",
       "**esconder atividades e informações**, como arquivos, diretórios, processos, chaves de registro e conexões de rede;",
       "**mapear vulnerabilidades** em outros equipamentos, por meio de varreduras de rede;",
       "**capturar informações** da rede, pela interceptação de tráfego."),
    trap("Pegadinha do nome",
         "O nome vem de **root** (o superusuário em sistemas Unix) + **kit**. Mas o termo **não indica que os programas são usados para obter** "
         "acesso privilegiado, e sim para **mantê-lo**."),
    nt("Na literatura, fala-se em rootkit de modo usuário, de modo kernel (age no núcleo do sistema, mais difícil de detectar) e bootkit "
       "(infecta a inicialização). A remoção costuma exigir ferramentas específicas ou a reinstalação do sistema."),

    h2("10. Ransomware"),
    p("**Ransomware** é um código malicioso que **torna inacessíveis os dados armazenados em um equipamento**, geralmente usando **criptografia**, "
      "e que **exige pagamento de resgate** (ransom) para restabelecer o acesso. O pagamento costuma ser exigido em criptomoedas."),
    bl("**Ransomware locker**: impede o acesso ao **equipamento** infectado.",
       "**Ransomware crypto**: impede o acesso aos **dados** armazenados, geralmente por criptografia.",
       "Além do equipamento, costuma buscar outros dispositivos conectados, locais ou em rede, e cifrá-los também.",
       "Variantes recentes praticam a **dupla extorsão**: além de cifrar, copiam os dados e ameaçam divulgá-los.",
       "Propaga-se por e-mails com o código em anexo ou com links, e pela **exploração de vulnerabilidades** em sistemas sem atualização."),
    key("Prevenção",
        "Manter sistema e programas **atualizados**, usar antimalware, ter cautela com links e anexos e, principalmente, fazer **backups regulares**. "
        "O backup deve ficar **desconectado** do equipamento (se estiver acessível, pode ser cifrado junto). "
        "**O pagamento do resgate não garante** o restabelecimento do acesso."),

    h2("11. Outros termos que aparecem em prova"),
    tb(["Termo", "Significado"], [0.25, 0.75], [
        ("Exploit", "Programa ou técnica que explora uma vulnerabilidade específica."),
        ("Dia zero (zero-day)", "Vulnerabilidade desconhecida do fabricante ou ainda sem correção; o ataque ocorre antes de existir defesa."),
        ("Bomba lógica", "Código inserido em um programa legítimo, programado para disparar quando certa condição ocorrer."),
        ("Hijacker", "Altera a página inicial e o mecanismo de busca do navegador e redireciona a navegação."),
        ("Scareware", "Simula alertas de infecção para assustar o usuário e levá-lo a instalar um falso antivírus ou a pagar por ele."),
        ("Cryptojacking", "Uso não autorizado do equipamento da vítima para minerar criptomoedas."),
        ("Malware sem arquivo (fileless)", "Atua na memória e usa ferramentas legítimas do sistema, sem gravar arquivo em disco, o que dificulta a detecção por assinatura."),
        ("APT", "Ameaça persistente avançada: ataque direcionado, sofisticado e de longa duração, em geral contra organizações."),
    ]),

    h2("12. Ataques e golpes ligados ao tema"),
    p("O edital reúne malwares, ataques e golpes. Os golpes exploram a **engenharia social**: técnica em que uma pessoa procura persuadir outra a "
      "executar determinadas ações, abusando da ingenuidade ou da confiança dela. **Não são códigos maliciosos**, mas costumam ser a porta de entrada deles."),
    tb(["Golpe", "Como funciona"], [0.25, 0.75], [
        ("Phishing", "O golpista tenta obter dados pessoais e financeiros combinando meios técnicos e engenharia social: mensagens que se passam por instituição conhecida e levam a páginas falsas ou a arquivos maliciosos."),
        ("Spear phishing", "Phishing direcionado a uma pessoa ou organização específica, com mensagem personalizada. Contra altos executivos: whaling."),
        ("Smishing e vishing", "Phishing por SMS (ou mensagens) e por voz (ligações telefônicas), respectivamente."),
        ("Pharming", "Tipo específico de phishing que redireciona a navegação para sites falsos por meio de **alterações no serviço de DNS**. O usuário digita o endereço correto e cai na página falsa."),
        ("Hoax (boato)", "Mensagem de conteúdo alarmante ou falso, geralmente atribuída a uma instituição importante, que pede para ser repassada."),
        ("Furto de identidade", "Uma pessoa se passa por outra para obter vantagens indevidas."),
    ]),
    tb(["Ataque", "Como funciona"], [0.25, 0.75], [
        ("Varredura (scan)", "Buscas minuciosas na rede para identificar equipamentos ativos, serviços e vulnerabilidades."),
        ("Falsificação (spoofing)", "Alteração de campos para aparentar outra origem: de e-mail (cabeçalho), de IP, de DNS."),
        ("Interceptação (sniffing)", "Inspeção dos dados trafegados na rede por programas chamados sniffers. Pode ser legítima (administração) ou maliciosa."),
        ("Força bruta", "Adivinhar, por tentativa e erro, um nome de usuário e senha."),
        ("Desfiguração (defacement)", "Alteração do conteúdo de uma página web."),
        ("Negação de serviço (DoS)", "Um atacante usa um equipamento para tirar de operação um serviço, um computador ou uma rede. O objetivo é **exaurir recursos e causar indisponibilidade**, não invadir nem coletar dados."),
        ("DDoS", "Negação de serviço **distribuída**: o ataque parte de um conjunto de equipamentos, em geral uma botnet."),
        ("Homem no meio (MITM)", "O atacante se posiciona entre as duas partes da comunicação, podendo ler e alterar as mensagens."),
    ]),

    h2("13. Prevenção e ferramentas"),
    h3("Antimalware (antivírus)"),
    p("Ferramentas antimalware procuram **detectar e, então, anular ou remover** os códigos maliciosos. Antivírus, antispyware, antirootkit e "
      "antitrojan são exemplos. Apesar do nome, os antivírus atuais atuam sobre vários tipos de códigos, não só sobre vírus."),
    tb(["Método de detecção", "Como funciona", "Limite"], [0.24, 0.46, 0.3], [
        ("Assinatura", "Compara os arquivos com uma lista de padrões (assinaturas) de códigos conhecidos.", "Não detecta o que ainda não foi catalogado; exige atualização constante."),
        ("Heurística", "Analisa estruturas, instruções e características do código para apontar o que é suspeito, mesmo sem assinatura.", "Pode gerar **falsos positivos**."),
        ("Comportamento", "Observa o que o programa faz quando executado (por exemplo, cifrar muitos arquivos em sequência).", "A ação maliciosa pode já ter começado."),
    ]),
    bl("**Quarentena**: área em que o arquivo suspeito fica isolado, sem poder ser executado, até que se decida removê-lo ou restaurá-lo.",
       "Mantenha **apenas um** antimalware com proteção em tempo real ativa: dois ao mesmo tempo podem entrar em conflito.",
       "Configure a verificação automática de anexos, downloads e mídias removíveis e mantenha o arquivo de assinaturas atualizado."),
    h3("Firewall pessoal"),
    p("Protege o equipamento contra **acessos não autorizados vindos da rede**. Pode bloquear tentativas de invasão e de exploração de vulnerabilidades, "
      "registrar essas tentativas em logs, evitar que um malware já instalado se propague ou se comunique com o invasor e bloquear o envio de dados coletados. "
      "**Não substitui o antimalware**: o firewall analisa conexões, não o conteúdo dos arquivos."),
    h3("Boas práticas"),
    bl("Manter sistema operacional e programas **atualizados**, removendo versões antigas e programas sem uso.",
       "Usar a conta de **administrador** apenas quando necessário.",
       "Desconfiar de links e anexos, mesmo vindos de conhecidos (o remetente pode ter sido falsificado ou a conta, invadida).",
       "Baixar aplicativos apenas de **fontes confiáveis** e lojas oficiais.",
       "Desabilitar a **autoexecução** de mídias removíveis e de macros.",
       "Fazer **backups** regulares, mantidos fora do equipamento.",
       "Usar **verificação em duas etapas** e senhas diferentes para cada serviço."),

    h2("14. Resumo comparativo"),
    tb(["Código", "Como é obtido", "Propagação", "Ação típica"], [0.16, 0.3, 0.24, 0.3], [
        ("Vírus", "Arquivo infectado executado; e-mail; mídia removível", "Insere cópias em arquivos", "Altera ou remove arquivos"),
        ("Worm", "Rede; exploração de vulnerabilidade", "Envia cópias de si pela rede", "Consome recursos; instala outros códigos"),
        ("Bot", "Rede; exploração de vulnerabilidade", "Como o worm", "Controle remoto; DDoS; spam"),
        ("Trojan", "Executado pelo usuário, enganado pelo disfarce", "Não se propaga", "Instala outros códigos; furta dados"),
        ("Spyware", "Por outro malware ou pelo usuário", "Não se propaga", "Monitora e envia informações"),
        ("Backdoor", "Por outro malware ou pelo invasor", "Não se propaga", "Possibilita o retorno do invasor"),
        ("Rootkit", "Por outro malware ou pelo invasor", "Não se propaga", "Esconde e mantém o invasor"),
        ("Ransomware", "Anexos, links, vulnerabilidades", "Depende da variante", "Cifra dados e exige resgate"),
    ]),
    exam("Como o Cebraspe cobra",
         "(1) Troca de características entre **vírus e worm**. (2) Trojan que “se replica”. (3) Rootkit para “obter” acesso. "
         "(4) Firewall “remove vírus” ou antivírus “bloqueia portas”. (5) Phishing e pharming tratados como malware. "
         "(6) Palavras absolutas — sempre, somente, exclusivamente, garante — quase sempre tornam o item errado em segurança da informação."),
]

QUIZ = quiz([
    ("C", "Código malicioso (malware) é o gênero que abrange programas desenvolvidos para executar ações danosas em equipamentos, sendo o vírus uma de suas espécies.",
     "Malware é o termo genérico; vírus, worm, bot, trojan, spyware, backdoor, rootkit e ransomware são tipos."),
    ("E", "Um vírus de computador é capaz de se propagar automaticamente pela rede, explorando vulnerabilidades, sem necessidade de que o arquivo infectado seja executado.",
     "Essa é a descrição do worm. O vírus insere cópias de si em outros arquivos e depende da execução do hospedeiro."),
    ("C", "No ciclo de vida de um vírus, a fase de dormência corresponde ao período em que ele permanece inativo, aguardando um evento que o ative.",
     "É a primeira fase do modelo clássico (dormência, propagação, ativação e execução). Nem todo vírus passa por ela."),
    ("E", "O vírus de macro infecta exclusivamente arquivos executáveis do sistema operacional, razão pela qual não pode ser transmitido por documentos de texto.",
     "É o contrário: o vírus de macro infecta documentos de aplicativos que usam linguagem de macro, como textos e planilhas."),
    ("C", "Um vírus polimórfico altera sua assinatura a cada infecção, o que dificulta a detecção por antivírus baseados exclusivamente em assinaturas.",
     "A mudança de assinatura é exatamente o que define o vírus polimórfico (mutante)."),
    ("C", "Os worms são notadamente responsáveis por consumir muitos recursos, em razão da grande quantidade de cópias de si mesmos que costumam propagar.",
     "É a ação típica do worm segundo a Cartilha: degrada o desempenho de redes e equipamentos."),
    ("E", "O bot diferencia-se do worm por não ser capaz de se propagar automaticamente, dependendo sempre de que o usuário o instale.",
     "O bot propaga-se de modo similar ao worm. A diferença está nos mecanismos de comunicação com o invasor, que permitem o controle remoto."),
    ("E", "O trojan do tipo dropper obtém da internet os códigos maliciosos que instala, ao passo que o downloader os traz embutidos em seu próprio código.",
     "Os conceitos estão invertidos: o downloader baixa da internet; o dropper traz os códigos embutidos."),
    ("C", "Adware é um tipo de spyware projetado para apresentar propagandas, podendo ser usado de forma legítima ou maliciosa.",
     "É legítimo quando incorporado a programas como patrocínio; malicioso quando as propagandas são direcionadas com base no monitoramento da navegação, sem o usuário saber."),
    ("E", "O ransomware do tipo locker cifra os arquivos do usuário, enquanto o do tipo crypto apenas impede o acesso ao equipamento.",
     "Invertido: o locker impede o acesso ao equipamento; o crypto impede o acesso aos dados, em geral por criptografia."),

    ("C", "Um backdoor permite o retorno de um invasor a um equipamento comprometido, por meio da inclusão de serviços criados ou modificados para esse fim.",
     "É a definição de backdoor: garante o acesso futuro sem que seja preciso repetir os métodos usados na invasão."),
    ("E", "Rootkits são programas utilizados para obter acesso privilegiado a um computador e, por isso, sua atuação cessa após a invasão.",
     "O rootkit serve para esconder e assegurar a presença do invasor, isto é, para manter o acesso, e não para obtê-lo."),
    ("E", "O cavalo de troia é um programa que se propaga inserindo cópias de si mesmo em outros arquivos, como jogos e protetores de tela.",
     "O trojan não se propaga nem se replica: ele se apresenta como um programa útil (jogo, protetor de tela) e executa funções maliciosas ocultas."),
    ("C", "Screenloggers são capazes de armazenar a posição do cursor e a tela apresentada no monitor nos momentos em que o mouse é clicado.",
     "Por isso são usados para capturar o que se digita em teclados virtuais."),
    ("C", "Em um ataque de negação de serviço distribuído (DDoS), um conjunto de equipamentos é utilizado de forma coordenada para tirar de operação um serviço, um computador ou uma rede.",
     "O DDoS costuma partir de botnets. O objetivo é a indisponibilidade, e não a invasão ou a coleta de dados."),
    ("E", "O pharming consiste no envio de mensagens eletrônicas com arquivos anexos que, quando executados, cifram os dados do usuário.",
     "Pharming é o redirecionamento da navegação para sites falsos por meio de alterações no serviço de DNS. Cifrar dados é ação do ransomware."),
    ("C", "A detecção heurística permite que o antimalware identifique códigos maliciosos ainda não catalogados, com base em características e comportamentos suspeitos, embora possa gerar falsos positivos.",
     "A heurística complementa a detecção por assinatura justamente para as pragas novas, ao custo de eventuais alarmes falsos."),
    ("E", "A instalação de um firewall pessoal dispensa o uso de antimalware, pois o firewall analisa o conteúdo dos arquivos armazenados e remove os códigos maliciosos encontrados.",
     "O firewall controla conexões de rede; não examina nem desinfeta arquivos. As duas ferramentas são complementares."),
    ("E", "O pagamento do resgate exigido por um ransomware garante o restabelecimento do acesso aos dados, sendo essa a medida de proteção recomendada.",
     "Não há garantia alguma de devolução. A proteção recomendada é manter backups atualizados e desconectados, além de sistemas atualizados."),
    ("C", "Phishing é um tipo de golpe por meio do qual se tenta obter dados pessoais e financeiros de um usuário pela utilização combinada de meios técnicos e engenharia social.",
     "É a definição da Cartilha. Phishing é golpe, não código malicioso, embora possa levar à instalação de um."),
], 20)

SOURCES = [
    "CERT.br — Cartilha de Segurança para Internet: capítulos “Códigos maliciosos (malware)”, “Golpes na Internet”, “Ataques na Internet” e “Mecanismos de segurança”; fascículo “Códigos maliciosos”. cartilha.cert.br",
    "STALLINGS, W. Criptografia e segurança de redes — capítulos sobre software malicioso (ciclo de vida e classificação dos vírus).",
    "Os 20 itens foram escritos para o Taticum. O Bloco B segue o padrão de cobrança da banca, mas não reproduz questões de provas.",
]
