# Windows Sessions

## Interactive

Un inicio de sesión interactivo o local es iniciada por un usuario que se autentica en un sistema local o de dominio ingresando sus credenciales. Se puede iniciar un inicio de sesión interactivo,  iniciando sesión directamente en el sistema, solicitando una sesión de inicio de sesión secundaria utilizando el comando **runas** a través de la línea de comando, o mediante una conexión de escritorio remoto. 


## No-interactive

Las cuentas no interactivas en Windows se diferencian de las cuentas de usuario estándar porque no requieren credenciales de inicio de sesión. Hay 3 tipos de cuentas no interactivas:  

| Cuenta | Nobre | Descripcion
|:-------|:------------|:-----------------|
| Local System Account | NT AUTHORITY\SYSTEM | la de mayores privilegios
| Local Service Account | NT AUTHORITY\LocalService | prvilegos como usuario local
| Network Service Account |  NT AUTHORITY\NetworkService | igual que la anteriror para para el domino