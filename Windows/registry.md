# Registry

## Structure

| Folder/Key            | Descripción                       | Abrevia |
|:-------------------------------|:-------------------------|:-----------------
| HKEY_CURRENT_USER     | confguración del usuario actual   | HKCU
| HKEY_USERS            | los perfiles de todos los usuarios activos cargados | HKU 
| HKEY_LOCAL_MACHINE    | configuración de la computadora   | HKLM
| HKEY_CLASSES_ROOT     | sub key de hklm\Software          | HKCR
| HKEY_CURRENT_CONFIG   | configuración de hardware         | 

## Accessing Registry hives offline:

Se guardan en `C:\Windows\System32\Config`

| Folder    | Key  
|:----------|:------------------------
| DEFAULT   | HKEY_USERS\DEFAULT
| SAM       | HKEY_LOCAL_MACHINE\SAM
| SECURITY  | HKEY_LOCAL_MACHINE\Security
| SOFTWARE  | HKEY_LOCAL_MACHINE\Software
| SYSTEM    | HKEY_LOCAL_MACHINE\System

Otras en `C:\Users\<username>`

NTUSER.DAT - HKEY_CURRENT_USER 
USRCLASS.DAT - HKEY_CURRENT_USER\Software\CLASSES

The USRCLASS.DAT hive is located in the directory `C:\Users\<username>\AppData\Local\Microsoft\Windows`

The NTUSER.DAT hive is located in the directory C:\Users\<username>\.

Apart from these files, there is another very important hive called the AmCache hive. This hive is located in `C:\Windows\AppCompat\Programs\Amcache.hve`. Windows creates this hive to save information on programs that were recently run on the system

## Transaction Logs and Backups:

Los cambios a las keys del registro se guardan en los registros de transacción y respaldo:

C:\Windows\System32\Config
C:\Windows\System32\Config\RegBack