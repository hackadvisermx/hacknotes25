
# Task 24  [Day 18] Eradication A Gift That Keeps on Giving

## Learning Objectives  

In this task, we will:

- Identify the CPU and memory usage of processes in Linux.
- Kill unwanted processes in Linux.
- Find ways a process can persist beyond termination.
- Remove persistent processes permanently.

### Identifying the Process

Linux gives us various options for monitoring a system's performance. Using these, we can identify the resource usage of processes. One option is the `top` command. This command shows us a list of processes in real time with their usage. It's a dynamic list, meaning it changes with the resource usage of each process.

```
top

top - 23:32:21 up 1 min,  0 users,  load average: 3.31, 1.21, 0.44
Tasks: 197 total,   2 running, 193 sleeping,   0 stopped,   2 zombie
%Cpu(s): 34.5 us,  3.4 sy,  0.0 ni, 51.7 id,  0.0 wa,  0.0 hi,  0.0 si, 10.3 st
MiB Mem :   3933.8 total,   2515.0 free,    618.7 used,    800.0 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   3051.6 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                    
    659 root      20   0    2488   1436   1344 R  94.4   0.0   1:22.85 a                          
      1 root      20   0  102696  11840   8400 S   0.0   0.3   0:04.52 systemd                    
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd                   
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                     
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                 
      5 root      20   0       0      0      0 I   0.0   0.0   0:00.02 kworker/0:0-memcg_kmem_ca+ 
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-kblockd       
      7 root      20   0       0      0      0 I   0.0   0.0   0:00.07 kworker/0:1-events         
      8 root      20   0       0      0      0 I   0.0   0.0   0:00.02 kworker/u30:0-events_unbo+ 
      9 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq               
     10 root      20   0       0      0      0 S   0.0   0.0   0:00.05 ksoftirqd/0                
     11 root      20   0       0      0      0 I   0.0   0.0   0:00.22 rcu_sched                  
     12 root      rt   0       0      0      0 S   0.0   0.0   0:00.00 migration/0                
     13 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/0                    
     14 root      20   0       0      0      0 S   0.0   0.0   0:00.01 cpuhp/1                    
     15 root      rt   0       0      0      0 S   0.0   0.0   0:00.33 migration/1                
     16 root      20   0       0      0      0 S   0.0   0.0   0:00.13 ksoftirqd/1                
     17 root      20   0       0      0      0 I   0.0   0.0   0:00.00 kworker/1:0-events         
     18 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/1:0H-kblockd       
     19 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kdevtmpfs                  
     20 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns                      
     21 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_tasks_kthre            
     22 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kauditd                    

```

### Killing the Culprit
- the process still there !!!
- 
```
sudo kill 659
top
```

### Checking the Cronjobs

Our first hint of what happened with the process will be in the cronjobs. Cronjobs are tasks that we ask the computer to perform on our behalf at a fixed interval. Often, that's where we can find traces of auto-starting processes.

```
crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
@reboot sudo runuser -l ubuntu -c 'vncserver :1 -depth 24 -geometry 1900x1200'
@reboot sudo python3 -m websockify 80 localhost:5901 -D

```

- as root
```
ubuntu@tryhackme:~$ sudo su
root@tryhackme:/home/ubuntu# crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
root@tryhackme:/home/ubuntu# 

```

### Check for Running Services

Maybe we should check for running services that might bring the process back. But the process name is quite generic and doesn't give a good hint. We might be clutching at straws here, but let's see what services are running on the system.

```
root@tryhackme:/home/ubuntu# systemctl list-unit-files | grep enabled
proc-sys-fs-binfmt_misc.automount              static          enabled      
-.mount                                        generated       enabled      
dev-hugepages.mount                            static          enabled      
dev-mqueue.mount                               static          enabled      
proc-sys-fs-binfmt_misc.mount                  disabled        enabled      
snap-amazon\x2dssm\x2dagent-5163.mount         enabled         enabled      
snap-amazon\x2dssm\x2dagent-7628.mount         enabled         enabled      
snap-core-16202.mount                          enabled         enabled      
snap-core18-2790.mount                         enabled         enabled      
snap-core18-2796.mount                         enabled         enabled      
snap-core20-1361.mount                         enabled         enabled      
snap-core20-2015.mount                         enabled         enabled      
snap-lxd-22526.mount                           enabled         enabled      
snap-lxd-24061.mount                           enabled         enabled      
sys-fs-fuse-connections.mount                  static          enabled      
sys-kernel-config.mount                        static          enabled      
sys-kernel-debug.mount                         static          enabled      
sys-kernel-tracing.mount                       static          enabled      
acpid.path                                     enabled         enabled      
apport-autoreport.path                         enabled         enabled      
cups.path                                      enabled         enabled      
systemd-ask-password-console.path              static          enabled      
systemd-ask-password-plymouth.path             static          enabled      
systemd-ask-password-wall.path                 static          enabled      
session-1.scope                                transient       enabled      
session-c1.scope                               transient       enabled      
a-unkillable.service                           enabled         enabled      
accounts-daemon.service                        enabled         enabled      
acpid.service                                  disabled        enabled      
alsa-restore.service                           static          enabled      
alsa-state.service                             static          enabled      
alsa-utils.service                             masked          enabled      
anacron.service                                enabled         enabled      
apparmor.service                               enabled         enabled
```

```
root@tryhackme:/home/ubuntu# systemctl list-unit-files | grep enabled | grep kill
a-unkillable.service                           enabled         enabled      
systemd-rfkill.service                         static          enabled      
systemd-rfkill.socket                          static          enabled      
root@tryhackme:/home/ubuntu# 

```

- service status
```
systemctl status a-unkillable.service 
● a-unkillable.service - Unkillable exe
     Loaded: loaded (/etc/systemd/system/a-unkillable.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2023-12-18 23:30:48 UTC; 12min ago
   Main PID: 563 (sudo)
      Tasks: 5 (limit: 4710)
     Memory: 3.6M
     CGroup: /system.slice/a-unkillable.service
             ├─ 563 /usr/bin/sudo /etc/systemd/system/a service
             ├─ 635 /etc/systemd/system/a service
             └─1801 unkillable proc

Dec 18 23:30:48 tryhackme systemd[1]: Started Unkillable exe.
Dec 18 23:30:49 tryhackme sudo[563]:     root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/etc/sy>
Dec 18 23:30:49 tryhackme sudo[563]: pam_unix(sudo:session): session opened for user root by (uid>
Dec 18 23:30:49 tryhackme sudo[663]: Merry Christmas
Dec 18 23:33:41 tryhackme sudo[1805]: Merry Christmas

```

- disable process
```
systemctl disable a-unkillable.service 
Removed /etc/systemd/system/multi-user.target.wants/a-unkillable.service.

root@tryhackme:/home/ubuntu# systemctl disable a-unkillable.service 
Removed /etc/systemd/system/multi-user.target.wants/a-unkillable.service.
root@tryhackme:/home/ubuntu# 
root@tryhackme:/home/ubuntu# rm -rf /etc/systemd/system/a
root@tryhackme:/home/ubuntu# rm -rf /etc/systemd/system/a-unkillable.service 

systemctl daemon-reload
systemctl status a-unkillable.service 
Unit a-unkillable.service could not be found.

```



## Answer the questions below

What is the name of the service that respawns the process after killing it?

a-unkillable.service

What is the path from where the process and service were running?  

/etc/systemd/system/a 
 

The malware prints a taunting message. When is the message shown? Choose from the options below.

1. Randomly

2. After a set interval

3. On process termination

4. None of the above

4

 Task 24  [Day 18] Eradication A Gift That Keeps on Giving

I completed Task 24  [Day 18] Eradication A Gift That Keeps on Giving!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023