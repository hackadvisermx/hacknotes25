# Configurar el repo


## Como hacerle para tener 2 pinches repositorios en una puta computadora

- Crear una llave ssh para cada cuenta
```
ssh-keygen -t rsa -C "hackadviser@gmail.com" -f ~/.ssh/hackadvisermx
ssh-keygen -t rsa -C "castr@uaz.edu.mx" -f ~/.ssh/castruaz
```

- Borrar y listar llaves cacheadas
```
ssh-add -D
ssh-add -l
```

- Agregar llaves al agente
```
ssh-add ~/.ssh/hackadvisermx
ssh-add ~/.ssh/castruaz
```


- Crear archivo de configuracion ~/.ssh/config
```
Host hackadvisermx
  Hostname github.com
  IdentityFile ~/.ssh/hackadvisermx
  IdentitiesOnly yes

Host castruaz
  Hostname github.com
  IdentityFile ~/.ssh/castruaz
  IdentitiesOnly yes
```

- Ir a cada repo por separado y agregar la llave SSH que corresponda


- Verificar que las llaves ssh funcionan
```
ssh -vT git@hackadvisermx
ssh -vT git@castruaz
```

- borrar todas las configuraciones globales
git config --unset-all   
	git config --global --unset-all   
❯ git config --global --unset-all user.name
❯ git config --global --unset-all user.emai

- Ir a la carpeta de cada repo y configurar de manera separada user y mail

```
cd hkn
git config user.name "hackadvisermx"
git config user.email "hackadviser@gmail.com"
git config --list

cd pro
git config user.name "castruaz"
git config user.email "castr@uaz.edu.mx"
git config --list
```

- Al agregar el remote origin, espcificar la url tipo ssh de acuerdo al archivo config
 
```
git remote add origin https://github.com/hackadvisermx/hacknotes21.git
git remote set-url origin git@github.com:hackadvisermx/hacknotes21.git
git branch -M main
git push -u origin main
```
- ver la configuraion
git remote -v

- push un repositorio existente (ssh)
```
git remote add origin https://github.com/castruaz/sisinfogeoej21.git
git remote set-url origin git@github.com:castruaz/sisinfogeoej21.git
git branch -M main
git push -u origin main
```




## Referencias
- [Dos cuentas git ssh](https://gist.github.com/jexchan/2351996)
