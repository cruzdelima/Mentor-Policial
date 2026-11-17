; Instalador do Taticum (Inno Setup). Compilado no GitHub Actions.
; Instala só para o usuário atual: não pede senha de administrador.
#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
AppId={{6B0E5C1E-3D0B-4E1B-9A55-7F2C6D1A9E21}
AppName=Taticum
AppVersion={#AppVersion}
AppVerName=Taticum {#AppVersion}
AppPublisher=Taticum
DefaultDirName={autopf}\Taticum
DefaultGroupName=Taticum
DisableProgramGroupPage=yes
DisableDirPage=yes
DisableReadyPage=yes
DisableWelcomePage=yes
DisableFinishedPage=no
PrivilegesRequired=lowest
OutputDir=..\dist
OutputBaseFilename=Taticum-Setup
SetupIconFile=runner\resources\app_icon.ico
UninstallDisplayIcon={app}\Taticum.exe
UninstallDisplayName=Taticum
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
CloseApplications=yes

[Languages]
Name: "ptbr"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[InstallDelete]
; Limpeza da versão com o nome antigo (Mentor Policial)
Type: files; Name: "{app}\MentorPolicial.exe"
Type: files; Name: "{autodesktop}\Mentor Policial.lnk"
Type: files; Name: "{group}\Mentor Policial.lnk"
Type: dirifempty; Name: "{group}"

[Files]
Source: "..\build\windows\x64\runner\Release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Taticum"; Filename: "{app}\Taticum.exe"
Name: "{autodesktop}\Taticum"; Filename: "{app}\Taticum.exe"

[Run]
Filename: "{app}\Taticum.exe"; Description: "Abrir o Taticum"; Flags: nowait postinstall skipifsilent

[Code]
// Fecha o Taticum (e a versão antiga, Mentor Policial) antes de copiar os arquivos.
// Sem isso, instalar por cima com o app aberto dá "Acesso negado" no flutter_windows.dll.
function PrepareToInstall(var NeedsRestart: Boolean): String;
var
  Code: Integer;
begin
  Exec(ExpandConstant('{sys}\taskkill.exe'), '/F /T /IM Taticum.exe', '', SW_HIDE, ewWaitUntilTerminated, Code);
  Exec(ExpandConstant('{sys}\taskkill.exe'), '/F /T /IM MentorPolicial.exe', '', SW_HIDE, ewWaitUntilTerminated, Code);
  Sleep(1000);
  Result := '';
end;
