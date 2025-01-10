
# Task 12 - Sandboxes - Day 6: If I can't find a nice malware to use, I'm not going.

## Learning Objectives

- Analyze malware behaviour using sandbox tools.
- Explore how to use YARA rules to detect malicious patterns.
- Learn about various malware evasion techniques.
- Implement an evasion technique to bypass YARA rule detection.

```
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\ /v ProgramFilesDir
```

A sandbox is an isolated environment where (malicious) code is executed without affecting anything outside the system. Often, multiple tools are installed to monitor, record, and analyze the code's behaviour.

Mayor Malware knows that before his malware executes, it needs to check if it is running on a Sandbox environment. If it is, then it should not continue with its malicious activity.

To do so, he has settled on one technique, which checks if the directory `C:\Program Files` is present by querying the Registry path `HKLM\\Software\\Microsoft\\Windows\\CurrentVersion`. The value can be confirmed by visiting the Registry path within the Registry Editor, as shown below:

To open the Windows Registry Editor, navigate to the Start Menu on the bottom, select Run, enter regedit, and press enter.

This directory is often absent on sandboxes or other virtualized environments, which could indicate that the malware is running in a sandbox.

Here's what it looks like in the C Programming Language:

```c
void registryCheck() {
    const char *registryPath = "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion";
    const char *valueName = "ProgramFilesDir";
    
    // Prepare the command string for reg.exe
    char command[512];
    snprintf(command, sizeof(command), "reg query \"%s\" /v %s", registryPath, valueName);
    // Run the command
    int result = system(command);
    // Check for successful execution
    if (result == 0) {
        printf("Registry query executed successfully.\n");
    } else {
        fprintf(stderr, "Failed to execute registry query.\n");
    }
}
int main() {
    const char *flag = "[REDACTED]";
    registryCheck();
        return 0;

} 
```

## Can YARA Do It?

Mayor Malware knows that McSkidy is a big fan of YARA rules.

YARA is a tool used to identify and classify malware based on patterns in its code. By writing custom rules, analysts can define specific characteristics to look for—such as particular strings, file headers, or behaviours—and YARA will scan files or processes to find matches, making it invaluable for detecting malicious code.

Mayor Malware does not think such a simple tool can detect his malware. But just to be sure, he has to test it out himself.

To do this, he wrote a small script that executes a YARA detection rule every time a new event is added to the System monitor log. This particular YARA rule detects any command that tries to access the registry.  

Let's have a look at the rule:

```javascript
rule SANDBOXDETECTED
{
    meta:
        description = "Detects the sandbox by querying the registry key for Program Path"
        author = "TryHackMe"
        date = "2024-10-08"
        version = "1.1"

    strings:
        
    $cmd= "Software\\Microsoft\\Windows\\CurrentVersion\" /v ProgramFilesDir" nocase

    

    condition:
        $cmd
}
```

Let's understand the contents:

- In the **strings** section, we have defined variables that include the value to look out for: $cmd
- In the **condition** section, we define when the rule will match the scanned file. In this case, if any of the specified strings are present. 

For his testing, Mayor Malware has set up a one-function script that runs the Yara rule and logs a true positive in `C:\Tools\YaraMatches.txt`.

Open up a PowerShell window, navigate to the `C:\Tools` directory, and use the following command to start up the EDR:

```
PS C:\Tools> .\JingleBells.ps1 
No events found in Sysmon log. 
Monitoring Sysmon events... Press Ctrl+C to exit.
```

Now run the malware by navigating to `C:\Tools\Malware`, and double-clicking on `MerryChristmas.exe`.

If our custom script did its job, you should have witnessed a popup by our EDR with a flag included, as shown below. This will be the answer to Question 1 below. You can now exit the custom EDR by pressing `Ctrl+C`.


## Adding More Evasion Techniques

Ah, it seems that Yara can detect the evasion that Mayor Malware has added. No worries. Because we can make our malware even stealthier by introducing obfuscation.


```c
void registryCheck() {
// Encoded PowerShell command to query the registry
    const char *encodedCommand = "RwBlAHQALQBJAHQAZQBtAFAAcgBvAHAAZQByAHQAeQAgAC0AUABhAHQAaAAgACIASABLAEwATQA6AFwAUwBvAGYAdAB3AGEAcgBlAFwATQBpAGMAcgBvAHMAbwBmAHQAXABXAGkAbgBkAG8AdwBzAFwAQwB1AHIAcgBlAG4AdABWAGUAcgBzAGkAbwBuACIAIAAtAE4AYQBtAGUAIABQAHIAbwBnAHIAYQBtAEYAaQBsAGUAcwBEAGkAcgA=";
    // Prepare the PowerShell execution command
    char command[512];
    snprintf(command, sizeof(command), "powershell -EncodedCommand %s", encodedCommand);

    // Run the command
    int result = system(command);

    // Check for successful execution
    if (result == 0) {
        printf("Registry query executed successfully.\n");
    } else {
        fprintf(stderr, "Failed to execute registry query.\n");
    }  
}
```

## Beware of Floss

While obfuscation is helpful, we also need to know that there are tools available that extract obfuscated strings from malware binaries. One such tool is Floss, a powerful tool developed by Mandiant that functions similarly to the Linux strings tool but is optimized for malware analysis, making it ideal for revealing any concealed details.

To try out Floss, open a PowerShell Window and enter the following command:

```
PS C:\Users\Administrator > cd C:\tools\FLOSS\
FLARE-VM 12/06/2024 17:35:55
PS C:\tools\FLOSS >
FLARE-VM 12/06/2024 17:35:57
PS C:\tools\FLOSS > floss.exe C:\Tools\Malware\MerryChristmas.exe |Out-file C:\tools\malstrings.txt
INFO: floss: extracting static strings
finding decoding function features: 100%|██████| 127/127 [00:00<00:00, 406.44 functions/s, skipped 0 library functions]
INFO: floss.stackstrings: extracting stackstrings from 87 functions
extracting stackstrings: 100%|█████████████████████████████████████████████████| 87/87 [00:01<00:00, 54.06 functions/s]
INFO: floss.tightstrings: extracting tightstrings from 14 functions...
INFO: floss.results: F0056514
extracting tightstrings from function 0x140007530: 100%|███████████████████████| 14/14 [00:01<00:00, 13.58 functions/s]
INFO: floss.string_decoder: decoding strings
emulating function 0x140006b60 (call 5/11): 100%|██████████████████████████████| 24/24 [00:33<00:00,  1.39s/ functions]
INFO: floss: finished execution after 57.09 seconds
INFO: floss: rendering results
FLARE-VM 12/06/2024 17:37:23
```




## Answer the questions below
### What is the flag displayed in the popup window after the EDR detects the malware?

THM{GlitchWasHere}

### What is the flag found in the malstrings.txt document after running floss.exe, and opening the file in a text editor?

THM{HiddenClue}

### if you want to more about sandboxes, have a look at the room [FlareVM: Arsenal of Tools](https://tryhackme.com/r/room/flarevmarsenaloftools).

