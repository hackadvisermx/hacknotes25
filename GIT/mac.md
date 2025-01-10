# Manejo de credenciales en macos

- Borrar credenciasles
```
git config --local credential.helper ""
git credential-osxkeychain erase
host=github.com 
protocol=https 
<Enter>
```

git config --global credentials.helper osxkeychain
