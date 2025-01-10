# Task 10 - Atomic Red Team - Day 4: I’m all atomic inside!


## Learning Objectives

- Learn how to identify malicious techniques using the MITRE ATT&CK framework.
- Learn about how to use Atomic Red Team tests to conduct attack simulations.
- Understand how to create alerting and detection rules from the attack tests.
## Detection Gaps

While it might be the utopian dream of every blue teamer, we will rarely be able to detect every attack or step in an attack kill chain. This is a reality that all blue teamers face: there are gaps in their detection. But worry not! These gaps do not have to be the size of black holes; there are things we can do to help make these gaps smaller.

Detection gaps are usually for one of two main reasons:

- **Security is a cat-and-mouse game.** As we detect more, the threat actors and red teamers will find new sneaky ways to thwart our detection. We then need to study these novel techniques and update our signature and alert rules to detect these new techniques.
- **The line between anomalous and expected behaviour is often very fine and sometimes even has significant overlap.** For example, let's say we are a company based in the US. We expect to see almost all of our logins come from IP addresses in the US. One day, we get a login event from an IP in the EU, which would be an anomaly. However, it could also be our CEO travelling for business. This is an example where normal and malicious behaviour intertwine, making it hard to create accurate detection rules that would not have too much noise.

Blue teams constantly refine and improve their detection rules to close the gaps they experience due to the two reasons mentioned above. Let's take a look at how this can be done!

## Cyber Attacks and the Kill Chain

Before diving into creating new detection rules, we first have to discuss some key topics. The first topic to discuss is the Cyber Kill chain. All cyber attacks follow a fairly standard process, which is explained quite well by the Unified Cyber Kill chain:

As a blue teamer, it would be our dream to prevent all attacks at the start of the kill chain. So even just when threat actors start their reconnaissance, we already stop them dead in their tracks. But, as discussed before, this is not possible. The goal then shifts slightly. If we are unable to fully detect and prevent a threat actor at any one phase in the kill chain, the goal becomes to perform detections across the entire kill chain in such a way that even if there are detection gaps in a single phase, the gap is covered in a later phase. The goal is, therefore, to ensure we can detect the threat actor before the very last phase of goal execution.

## MITRE ATT&CK

A popular framework for understanding the different techniques and tactics that threat actors perform through the kill chain is the [MITRE ATT&CK framework](https://attack.mitre.org/). The framework is a collection of tactics, techniques, and procedures that have been seen to be implemented by real threat actors. The framework provides a [navigator tool](https://mitre-attack.github.io/attack-navigator/) where these TTPs can be investigated:

However, the framework primarily discusses these TTPs in a theoretical manner. Even if we know we have a gap for a specific TTP, we don't really know how to test the gap or close it down. This is where the Atomics come in!

## Atomic Red

The Atomic Red Team library is a collection of red team test cases that are mapped to the MITRE ATT&CK framework. The library consists of simple test cases that can be executed by any blue team to test for detection gaps and help close them down. The library also supports automation, where the techniques can be automatically executed. However, it is also possible to execute them manually.

## Dropping the Atomic

McSkidy has a vague idea of what happened to the "compromised machine." It seems someone tried to use the Atomic Red Team to emulate an attack on one of our systems without permission. The perpetrator also did not clean up the test artefacts. Let's have a look at what happened.

## Running an Atomic

McSkidy suspects that the supposed attacker used the MITRE ATT&CK technique [T1566.001 Spearphishing](https://attack.mitre.org/techniques/T1566/001/) with an attachment. Let's recreate the attack emulation performed by the supposed attacker and then look for the artefacts created.

Open up a PowerShell prompt as administrator and follow along with us. Let's start by having a quick peek at the help page. Enter the command `Get-Help Invoke-Atomictest`. You should see the output below:

```
PS C:\Users\Administrator> Get-Help Invoke-Atomictest
```

| Parameter           | Explanation                                                                                                                              | Example use                                                                           |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `-Atomic Technique` | This defines what technique you want to emulate. You can use the complete technique name or the "TXXXX" value. This flag can be omitted. | `Invoke-AtomicTest -AtomicTechnique T1566.001`                                        |
| `-ShowDetails`      | Shows the details of each test included in the Atomic.                                                                                   | `Invoke-AtomicTest T1566.001 -ShowDetails`                                            |
| `-ShowDetailsBrief` | Shows the title of each test included in the Atomic.                                                                                     | `Invoke-AtomicTest T1566.001 -ShowDetailsBrief`                                       |
| `-CheckPrereqs`     | Provides a check if all necessary components are present for testing                                                                     | `Invoke-AtomicTest T1566.001 -CheckPrereqs`                                           |
| `-TestNames`        | Sets the tests you want to execute using the complete Atomic Test Name.                                                                  | `Invoke-AtomicTest T1566.001 -TestNames "Download Macro-Enabled Phishing Attachment"` |
| `-TestGuids`        | Sets the tests you want to execute using the unique test identifier.                                                                     | `Invoke-AtomicTest T1566.001 -TestGuids 114ccff9-ae6d-4547-9ead-4cd69f687306`         |
| `-TestNumbers`      | Sets the tests you want to execute using the test number. The scope is limited to the Atomic Technique.                                  | `Invoke-AtomicTest T1566.001 -TestNumbers 2,3   `                                     |
| `-Cleanup`          | Run the cleanup commands that were configured to revert your machine state to normal.                                                    | `Invoke-AtomicTest T1566.001 -TestNumbers 2 -Cleanup`                                 |
**Our First Command**  

We can build our first command now that we know which parameters are available. We would like to know more about what exactly happens when we test the Technique T1566.001. To get this information, we must include the name of the technique we want information about and then add the flag `-ShowDetails` to our command. Let's have a look at the command we constructed: `Invoke-AtomicTest T1566.001 -ShowDetails`. This command displays the details of all tests included in the T1566.001 Atomic.

```
PS C:\Users\Administrator> Invoke-AtomicTest T1566.001 -ShowDetails
```

The output above is clearly split up into multiple parts, each matching a test. Let's examine what type of information is provided in a test. We will use the test we want to run as an example.

| Key                | Value                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Technique          | Phishing: Spearphishing Attachment T1566.001                                                                                                                                                                                                    | The full name of the MITRE ATT&CK technique that will be tested                                                                                                                                                          |
| Atomic Test Name   | Download Macro-Enabled Phishing Attachment                                                                                                                                                                                                      | A descriptive name of the type of test that will be executed                                                                                                                                                             |
| Atomic Test Number | 1                                                                                                                                                                                                                                               | A number is assigned to the test; we can use this in the command to specify which test we want to run.                                                                                                                   |
| Atomic Test GUID   | 114ccff9-ae6d-4547-9ead-4cd69f687306                                                                                                                                                                                                            | A unique ID is assigned to this test; we can use this in the command to specify which test we want to run.                                                                                                               |
| Description        | This atomic test downloads a macro-enabled document from the Atomic Red Team GitHub repository, simulating an end-user clicking a phishing link to download the file. The file "PhishingAttachment.xlsm" is downloaded to the %temp% directory. | Provides a detailed explanation of what the test will do.                                                                                                                                                                |
| Attack commands    | **Executor:** powershell<br><br>**ElevationRequired:** False<br><br>**Command:** $url = ‘http://localhost/PhishingAttachment.xlsm’ Invoke-WebRequest -Uri $url -OutFile $env:TEMP.xlsm                                                          | This provides an overview of all the commands run during the test, including the executor of those commands and the required privileges. It also helps us determine where to look for artefacts in Windows Event Viewer. |
| Cleanup commands   | Command: Remove-Item $env:TEMP.xlsm -ErrorAction Ignore                                                                                                                                                                                         | An overview of the commands executed to revert the machine back to its original state.                                                                                                                                   |
| Dependencies       | There are no dependencies required.                                                                                                                                                                                                             | An overview of all required resources that must be present on the testing machine in order to execute the test                                                                                                           |

**Phishing: Spearphishing Attachment T1566.001 Emulated**

Let's continue and run the first test of T1566.001. Before running the emulation, we should ensure that all required resources are in place to conduct it successfully. To verify this, we can add the flag `-Checkprereq` to our command. The command should look something like this: `Invoke-AtomicTest T1566.001 -TestNumbers 1 -CheckPrereq`.

This command will use the data included in the "dependencies" part of the test details to verify if all required resources are present. Looking at the test 1 dependencies of the T1566.001 Atomic, no additional resources are required. Run the same command for test 2, and it will state that Microsoft Word needs to be installed, as shown below:

```
Invoke-AtomicTest T1566.001 -TestNumbers 2 -CheckPrereq
```

Now that we have verified the dependencies, let us continue with the emulation. Execute the following command to start the emulation: `Invoke-AtomicTest T1566.001 -TestNumbers 1` and you should get the following output:

```
Invoke-AtomicTest T1566.001 -TestNumbers 1
```
Based on the output, we can determine that the test was successfully executed. We can now analyse the logs in theWindows Event Viewer to find Indicators of Attack and Compromise.

## Detecting the Atomic

Now that we have executed the T1566.001 Atomic, we can look for log entries that point us to this emulated attack. For this purpose, we will use the Windows Event Logs. This machine comes with [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) installed. System Monitor (Sysmon) provides us with detailed information about process creation, network connections, and changes to file creation time.

To make it easier for us to pick up the events created for this emulation, we will first start with cleaning up files from the previous test by running the command `Invoke-AtomicTest T1566.001 -TestNumbers 1 -cleanup`.

```
Invoke-AtomicTest T1566.001 -TestNumbers 1 -cleanup
```

ow, we will clear the Sysmon event log:

- Open up Event Viewer by clicking the icon in the taskbar, or searching for it in the Start Menu.
- Navigate to `Applications and Services => Microsoft => Windows => Sysmon => Operational` on the left-hand side of the screen.
- Right-click `Operational` on the left-hand side of the screen and click **Clear Log**. Click **Clear** when the popup shows.

Now that we have cleaned up the files and the sysmon logs, let us run the emulation again by issuing the command `Invoke-AtomicTest T1566.001 -TestNumbers 1`.

```
Invoke-AtomicTest T1566.001 -TestNumbers 1
```

Next, go to the Event Viewer and right-click on the **Operational** log on the left-hand side of the screen and then click on **Refresh**. There should be new events related to the emulated attack. Now sort the table on the Date and Time column to order the events chronologically (oldest first). The first two events of the list are tests that Atomic executes for every emulation. We are interested in 2 events that detail the attack:

- First, a process was created for PowerShell to execute the following command: `"powershell.exe" & {$url = 'http://localhost/PhishingAttachment.xlsm' Invoke-WebRequest -Uri $url -OutFile $env:TEMP\PhishingAttachment.xlsm}`.
- Then, a file was created with the name PhishingAttachment.xlsm.

Click on each event to see the details. When you select an event, you should see a detailed overview of all the data collected for that event. Click on the **Details** tab to show all the **EventData** in a readable format. Let us take a look at the details of these events below. The data highlighted is valuable for incident response and creating alerting rules.

## Answer the questions below

### What was the flag found in the .txt file that is found in the same directory as the PhishingAttachment.xslm artefact?

C:\Users\Administrator\AppData\Local\temp

THM{GlitchTestingForSpearphishing}

### What ATT&CK technique ID would be our point of interest?
https://attack.mitre.org/techniques/T1059/
T1059

###  What ATT&CK subtechnique ID focuses on the Windows Command Shell?

https://attack.mitre.org/techniques/T1059/003/

T1059.003

### What is the name of the Atomic Test to be simulated?

```
Invoke-AtomicTest T1059.003 -ShowDetails
```

Simulate BlackByte Ransomware Print Bombing

### What is the name of the file used in the test?

```
Invoke-AtomicTest T1059.003 -TestNumbers 4
```

Wareville_Ransomware.txt

### What is the flag found from this Atomic Test?
- En el pdf que se crea esta la flag
=THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}