
# Event-Viewing

#### Description

One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:

1. They installed software using an installer they downloaded online
2. They ran the installed software but it seemed to do nothing
3. Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.

See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!Download the Windows Log file [here](https://challenge-files.picoctf.net/c_verbal_sleep/123d9b79cadb6b44ab6ae912f25bf9cc18498e8addee851e7d349416c7ffc1e1/Windows_Logs.evtx)

# Solucion

- Event ID 1033 -  Windows Installer installed the product (1/3)
```
cGljb0NURntFdjNudF92aTN3djNyXw==

```

- Event id 4657 -  A registry value was modified....
```
MXNfYV9wcjN0dHlfdXMzZnVsXw==
1s_a_pr3tty_us3ful_
```

- Event ID 1074 - A user initiates a shutdown or restart (3/3) 
```
dDAwbF84MWJhM2ZlOX0=

t00l_81ba3fe9}

```

```powershell

Get-WinEvent -Path .\Windows_Logs.evtx | ? Message -like "*=" | select TimeCreated, Id, ProviderName, Message | Format-List

Get-WinEvent -Path .\Windows_Logs.evtx | ? Message -match  "[A-Za-z0-9+/]{20,}={2}" | select TimeCreated, Id, ProviderName, Message | Format-List
```


```
picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}

```

## Solucion 2

- Usando un parser para .evtx archivos 

```

- Desacargar
https://github.com/omerbenamram/evtx
https://github.com/omerbenamram/evtx/releases/tag/v0.9.0


- modificar permisos y crear liga
chmod +x evtx_dump-v0.9.0-aarch64-unknown-linux-gnu 
ln -s /home/kali/Downloads/evtx_dump-v0.9.0-aarch64-unknown-linux-gnu /usr/local/bin/evtx

sudo evtx Windows_Logs.evtx > event.xml           
                                                                                                                                                                                
strings event.xml | grep ==            
    <Data>Totally_Legit_Software,1.3.3.7,0,0,cGljb0NURntFdjNudF92aTN3djNyXw==,(NULL),</Data>
    <Data Name="ObjectValueName">Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==)</Data>
                                                                                                                                                                                
echo cGljb0NURntFdjNudF92aTN3djNyXw== | base64 -d
picoCTF{Ev3nt_vi3wv3r_                                                                                                                                                                                
echo MXNfYV9wcjN0dHlfdXMzZnVsXw== | base64 -d    
1s_a_pr3tty_us3ful_           


 cat event.xml | grep -E "[0-9A-Za-z+/]{19,}=" | grep -v "Notification"
    <Data>Totally_Legit_Software,1.3.3.7,0,0,cGljb0NURntFdjNudF92aTN3djNyXw==,(NULL),</Data>
    <Data Name="ObjectValueName">Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==)</Data>
    <Data Name="param6">dDAwbF84MWJhM2ZlOX0=</Data>
    <Data Name="param6">dDAwbF84MWJhM2ZlOX0=</Data>

echo dDAwbF84MWJhM2ZlOX0= | base64 -d
t00l_81ba3fe9} 

picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}


```

## Forma 3

```

```