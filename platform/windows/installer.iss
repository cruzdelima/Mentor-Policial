; Instalador do Mentor Policial (Inno Setup). Compilado no GitHub Actions.
; Instala só para o usuário atual: não pede senha de administrador.
#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
AppId={{6B0E5C1E-3D0B-4E1B-9A55-7F2C6D1A9E21}
AppName=Mentor Policial
AppVersion={#AppVersion}
AppVerName=Mentor Policial {#AppVersion}
AppPublisher=Mentor Policial
DefaultDirName={autopf}\Mentor Policial
DefaultGroupName=Mentor Policial
DisableProgramGroupPage=yes
DisableDirPage=yes
DisableReadyPage=yes
PrivilegesRequired=lowest
OutputDir=..\dist
OutputBaseFilename=MentorPolicial-Setup
SetupIconFile=runner\resources\app_icon.ico
UninstallDisplayIcon={app}\MentorPolicial.exe
UninstallDisplayName=Mentor Policial
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
CloseApplications=yes

[Languages]
Name: "ptbr"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na Área de Trabalho"; GroupDescription: "Atalhos:"

[Files]
Source: "..\build\windows\x64\runner\Release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Mentor Policial"; Filename: "{app}\MentorPolicial.exe"
Name: "{autodesktop}\Mentor Policial"; Filename: "{app}\MentorPolicial.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MentorPolicial.exe"; Description: "Abrir o Mentor Policial"; Flags: nowait postinstall skipifsilent
