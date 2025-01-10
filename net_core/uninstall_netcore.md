# .NET Core

## Listar versiones instaladas
```
dotnet --list-sdks     
dotnet --list-runtimes
```
## Remover versiones anteriores
```
version="1.0.1"
sudo rm -rf /usr/local/share/dotnet/sdk/$version
sudo rm -rf /usr/local/share/dotnet/shared/Microsoft.NETCore.App/$version
sudo rm -rf /usr/local/share/dotnet/shared/Microsoft.AspNetCore.All/$version
sudo rm -rf /usr/local/share/dotnet/shared/Microsoft.AspNetCore.App/$version
sudo rm -rf /usr/local/share/dotnet/host/fxr/$version
```

Referencia> https://docs.microsoft.com/en-us/dotnet/core/install/remove-runtime-sdk-versions?pivots=os-macos

