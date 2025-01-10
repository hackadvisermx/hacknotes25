# WSL

wsl --set-default-version 1


wsl -l -v
  NAME          STATE           VERSION
* kali-linux    Stopped         1

wsl -l

wsl --unregister kali-linux

 Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 


Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 


 [wsl1 vs wsl2](https://www.softzone.es/windows-10/como-se-hace/subsistema-windows-linux/)


Instalar

 Windows Terminal


Interoperabilidad

https://docs.microsoft.com/es-mx/windows/wsl/interop