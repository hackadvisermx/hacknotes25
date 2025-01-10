# Autenticacion en Windows

Es el proceso de verificar la identidad de una persona (o un objeto o servicio), cuando se autentifica a una persona, el objetivo es verificar que no es un impostor.

## Autenticación Local
La autenticación local se lleva a cabo usando LSA (Local Security Authority). LSA es un subsistema protegido que realizan un seguimiento de las polítcas de seguridad y las cuentas que hay en el sistema. También mantiene la información acerca de los aspectos de la seguridad local de la computadora.

## Autenticación de Directorio Activo
Hay dos tipos:
- On-Premise Active Directory (AD)
- Azure Active Directory (ADD)

### On Premise Active Directory (AD)

Tiene el registro de todos los usuarios, pcs y servidores y autentica usuarios (los registra en la red). Una vez autenticados, el directorio activo también gobierna que es lo que lo usuarios pueden hacer y lo que no pueden hacer, permite hacer o dar autorización.

La autenticación se hace usando alguno de los siguientes protocolos:
- NTLM
- LDAP / LDAPS
- KERBEROS

|Protocolo       |Descripción
|:--------------|:-------------------
| NTLM / NTLM2  | usa una secuencia de mensajes reto-respuesta entre el cliente y el servidor, no provee protección de la integridad o confidencialidad de datos
| LDAP / LDAPS  | los usuarios / pcs se comunican via API con el controlador de dominio y envian sus credenciales para ser validadas y obtener acceso, LDAPS envia las credenciales encriptadas
| KERBEROS      | usa criptografía de llave simetrica y requiere la autorización de una tercera-parte para verificar la identidad del usuario

### Autenticación en Azure Active Directory (ADD)
Es una autenticación segura en línea la cual puede contner usuarios y grupos, los usuarios tienen un nombre de usuario y contraseña que es usada para ingresar a la aplicación que usa ADD para autenticación.

Azure Active Directory utiliza los siguientes métodos:
- SAML (Security Assertion Markup Languaje)
- OAUTH 2.0
- OpenID Connect

|Método         |Descripción
|:--------------|:-------------------
| SAML          | es un estandar SSO (single sign-on) define un conjunto de reglas/protocolos que permite a los usuarios
| OAUTH 2.0     |
| OpenID Connect|