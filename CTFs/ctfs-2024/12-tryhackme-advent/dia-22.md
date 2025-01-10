
# Task 28 - Kubernetes DFIR - Day 22: It's because I'm kubed, isn't it?

## Learning Objectives

- Learn about Kubernetes, what it is and why it is used.
- Learn about DFIR, and the challenges that come with DFIR in an ephemeral environment.
- Learn how DFIR can be done in a Kubernetes environment using log analysis.
## Kubernetes Explained

Back in the day, it was very common for companies/organisations to use a monolithic architecture when building their applications. A monolithic architecture is an application built as a single unit, a single code base, and usually, a single executable deployed as a single component. For many companies, this worked and still does to this day; however, for some companies, this style of architecture was causing problems, especially when it came to scaling. The problem with monolithic applications is that if one single part of the application needs scaling, the whole application has to be scaled with it. It would make far more sense for companies with applications that receive fluctuating levels of demand across their parts to break the application down component by component and run them as their own microservices. That way, if one "microservice" starts to receive an increase in demand, it can be scaled up rather than the entire application.

**The Great Microservice Adoption**

Microservices architecture was adopted by companies like Netflix, which is a perfect example of the hypothetical company discussed above. Their need to scale up services dedicated to streaming when a new title is released (whilst services dedicated to user registration, billing, etc, won't need the same scaling level) made a microservices architecture a no-brainer. As time went by, companies similar to Netflix hopped aboard the Microservices Express, and it became very widely adopted. Now, as for the hosting of these microservices, containers were chosen due to their lightweight nature. Only as you may imagine, an application of this scale can require hundreds, even thousands of containers. Suddenly, a tool was needed to organise and manage these containers.

**Introducing Kubernetes**

Well, you guessed it! That's exactly what Kubernetes was made for. Kubernetes is a container orchestration system. Imagine one of those microservices mentioned earlier is running in a container, and suddenly, there is an increase in traffic, and this one container can no longer handle all requests. The solution to this problem is to have another container spun up for this microservice and balance the traffic between the two. Kubernetes takes care of this solution for you, "orchestrating" those containers when needed.

That makes things a lot easier for everyone involved, and it's because of this (along with the widespread adoption of microservices architecture) that Kubernetes is so ubiquitous in the digital landscape today. This popularity means that it's **highly portable** as no matter what technology stack is being used, it's very likely a Kubernetes integration is available; this, along with the fact it can help make an application **highly available** and **scalable**, makes Kubernetes a no-brainer!

In Kubernetes, containers run in **pods**; these pods run on **nodes**, and a collection of nodes makes up a Kubernetes **cluster**. It is within a cluster that McSkidy and co's investigation will occur today. If you're interested in learning more about Kubernetes, we have a range of rooms on the subject. A good place to start would be the [Intro to Kubernetes](https://tryhackme.com/r/room/introtok8s) room; then, there's plenty more where that came from with the [Kubernetes Hardening](https://tryhackme.com/module/kubernetes-hardening) Module.


## DFIR Basics

Every cyber security professional has stumbled—or will stumble—upon **DFIR** at some point in their career. It is an acronym—in IT, we all _love_ our acronyms—that stands for "**Digital Forensics and Incident Response**." These two investigative branches of cyber security come into play during a cyber security incident. A DFIR expert will likely be called to action as soon as an incident is ascertained and will be expected to perform actions that fall into one or both of the two disciplines:

- **Digital Forensics**, like any other "forensics" discipline, aims to collect and analyse digital evidence of an incident. The artefacts collected from the affected systems are used to trace the chain of attack and uncover all facts that ultimately led to the incident. DFIR experts sometimes use the term "post-mortem" to indicate that their analysis starts _after_ the incident has occurred and is performed on already compromised systems and networks.
- **Incident Response**, while still relying on data analysis to investigate the incident, focuses on "responsive" actions such as threat containment and system recovery. The incident responder will isolate infected machines, use the data collected during the analysis to identify the "hole" in the infrastructure's security and close it, and then recover the affected systems to a clean, previous-to-compromise state.

Picture the incident responder as an emergency first responder whose aim is to contain the damage, extinguish the fire, and find and stabilise all the victims. On the other hand, the digital forensics analyst is the Crime Scene Investigator (CSI) or detective trying to recreate the crime scene and ultimately find evidence to identify and frame the criminal.

Both roles are expected to document all findings thoroughly. The incident responder will present them to explain how the incident happened and what can be learnt from it, ultimately proposing changes to improve the security stance of the entity affected by the incident. The digital forensics analyst will use the findings to demonstrate the attackers' actions and—eventually—testify against them in court.

In the task at hand, we will help McSkidy and the Glitch become digital forensics analysts and retrace the malicious actor's steps. We will especially focus on collecting evidence and artefacts to uncover the perpetrator and present our analysis to Wareville townspeople.



## Excruciatingly Ephemeral

DFIR can be a lot of fun. It's easy to feel like a digital detective, analysing the crime scene and connecting the dots to create a narrative string of events explaining what happened. What if the crime scene vanished into thin air moments after the crime was committed? That is a problem we face regularly when carrying out DFIR in a Kubernetes environment. This is because, as mentioned, Kubernetes workloads run in containers. It is **very** common that a container will have a very short lifespan (either spun up to run a job quickly or to handle increased load, etc, before being spun back down again). In fact, in this year's (2024) [Cloud-Native Security and Usage Report](https://sysdig.com/2024-cloud-native-security-and-usage-report/), Sysdig found that 70% of containers live less than 5 minutes.

So what can we do about it? Well not to worry, it just means we have to expand our digital detectives toolkit. The key to keeping track of the ongoings in your often ephemeral workloads within your Kubernetes environment is increasing **visibility**. There are a few ways we can do this. One way is by enabling Kubernetes audit logging, a function that Kubernetes provides, allowing for requests to the API to be captured at various stages. For example, if a user makes a request to delete a pod, this request can be captured, and while the pod will be deleted (and logs contained within it lost), the request made to delete it will be persisted in the audit logs. What requests/events are captured can be defined with an audit policy. We can use these audit logs to answer questions which help us in a security/DFIR context, such as:

- What happened?
- When did it happen?
- Who initiated it?
- To what did it happen?
- Where was it observed?
- From where was it initiated?
- To where was it going?

Of course, this just scratches the surface in terms of the level of visibility we can achieve in our Kubernetes environment. We can feed these audit logs, as well as events from other security-relevant sources, into runtime security tools which help transform these raw events into actionable data (which can then be visualised using yet more tools; a digital detective should definitely invest in an **extra large** toolkit). If you want to learn more on that subject, check out the [Kubernetes Runtime Security](https://tryhackme.com/r/room/k8sruntimesecurity) room.

## Following the Cookie Crumbs

Let's start our investigation. As mentioned before, some of the log sources would disappear as their sources, like pods, are ephemeral. Let's see this in action first. On the VM, open a terminal as start K8s using the following command:

```
ubuntu@tryhackme:~$ minikube start
😄  minikube v1.32.0 on Ubuntu 20.04
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔄  Restarting existing docker container for "minikube" ...
❗  This container is having trouble accessing https://registry.k8s.io
💡  To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ apiserver.audit-policy-file=/etc/ssl/certs/audit-policy.yaml
    ▪ apiserver.audit-log-path=-
🔗  Configuring Calico (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" clus
```

It will take roughly three minutes for the cluster to configure itself and start. You can verify that the cluster is up and running using the following command:

```bash
ubuntu@tryhackme:~$ kubectl get pods -n wareville
NAME                              READY   STATUS    RESTARTS         AGE
morality-checker                  1/1     Running   10 (2m36s ago)   66d
naughty-or-nice                   1/1     Running   2 (2m36s ago)    55d
naughty-picker-7cbd95dd66-gjm7r   1/1     Running   34 (2m36s ago)   66d
naughty-picker-7cbd95dd66-gshvp   1/1     Running   34 (2m36s ago)   66d
nice-picker-7cd98989c8-bfbqn      1/1     Running   34 (2m36s ago)   66d
nice-picker-7cd98989c8-ttc7t      1/1     Running   34 (2m36s ago)   66d

```

If all of the pods are up and running (based on their status), you are ready to go. This will take another **2 minutes**. Since we know that the web application was compromised, let's connect to that pod and see if we can recover any logs. Connect to the pod using the following command:

```bash
ubuntu@tryhackme:~$ kubectl exec -n wareville naughty-or-nice -it -- /bin/bash

root@naughty-or-nice:/# cat /var/log/apache2/access.log 
172.17.0.1 - - [28/Oct/2024:11:05:45 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:05:45 +0000] "GET /style/style.css HTTP/1.1" 200 1207 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:05:45 +0000] "GET /style/tailwind.css HTTP/1.1" 200 3031 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:05:45 +0000] "GET /index.js HTTP/1.1" 200 2023 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:05:45 +0000] "GET /favicon.ico HTTP/1.1" 404 489 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:07:17 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:09:29 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:12:11 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:12:11 +0000] "GET /style/style.css HTTP/1.1" 200 1207 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:12:11 +0000] "GET /style/tailwind.css HTTP/1.1" 200 3031 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:12:11 +0000] "GET /index.js HTTP/1.1" 200 2022 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:12:13 +0000] "GET /api.php HTTP/1.1" 200 396 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:48:39 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:48:39 +0000] "GET /style/style.css HTTP/1.1" 200 1207 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:48:39 +0000] "GET /style/tailwind.css HTTP/1.1" 200 3031 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:48:39 +0000] "GET /index.js HTTP/1.1" 200 2020 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:48:44 +0000] "GET //api.php HTTP/1.1" 200 396 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:49:05 +0000] "POST //api.php HTTP/1.1" 200 242 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:49:05 +0000] "GET //api.php HTTP/1.1" 200 453 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:51:40 +0000] "GET / HTTP/1.1" 200 2038 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:51:40 +0000] "GET /style/style.css HTTP/1.1" 200 1207 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:51:40 +0000] "GET /index.js HTTP/1.1" 200 2021 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:51:41 +0000] "GET /favicon.ico HTTP/1.1" 404 489 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [28/Oct/2024:11:52:13 +0000] "GET //api.php HTTP/1.1" 200 454 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
172.17.0.1 - - [29/Oct/2024:12:32:37 +0000] "GET / HTTP/1.1" 200 267 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
172.17.0.1 - - [29/Oct/2024:12:32:37 +0000] "GET /favicon.ico HTTP/1.1" 404 489 "http://localhost:8081/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
172.17.0.1 - - [29/Oct/2024:12:32:48 +0000] "GET /shelly.php?cmd=whoami HTTP/1.1" 200 224 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
root@naughty-or-nice:/# 

```
Sadly, we only see logs from the 28th of October when our attack occurred later on. Looking at the last log, however, we do see something interesting with a request being made to a `shelly.php` file. So, this tells us we are on the right track. Terminate your session to the pod using `exit`. Fortunately, McSkidy knew that the log source was ephemeral and decided to ensure that remote backups of the log source were made. Navigate to our backup directory using `cd /home/ubuntu/dfir_artefacts/` where you will find the access logs stored in `pod_apache2_access.log`. Review these logs to see what Mayor Malware was up to on the website and answer the first 3 questions at the bottom of the task!

Sadly, our investigation hits a bit of a brick wall here. Firstly, because the pod was configured using a port forward, we don't see the actual IP that was used to connect to the instance. Also, we still don't fully understand how the webshell found its way into the pod. However, we rebooted the cluster and the webshell was present, meaning it must live within the actual image of the pod itself! That means we need to investigate the docker image registry itself. To view the registry container ID, run the following command:

```
docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS         PORTS                                                                                                                                  NAMES
77fddf1ff1b8   registry:2.7                          "/entrypoint.sh /etc…"   2 months ago   Up 8 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp                                                                                              registry_priv
cd9ee77b8aa5   gcr.io/k8s-minikube/kicbase:v0.0.42   "/usr/local/bin/entr…"   8 months ago   Up 7 minutes   127.0.0.1:32772->22/tcp, 127.0.0.1:32771->2376/tcp, 127.0.0.1:32770->5000/tcp, 127.0.0.1:32769->8443/tcp, 127.0.0.1:32768->32443/tcp   minikube

```

Now, let's connect to the instance to see if we have any logs:

```
buntu@tryhackme:~$ docker exec cd9ee77b8aa5 ls -al /var/log
total 36
drwxr-xr-x  5 root root  4096 Apr  1  2024 .
drwxr-xr-x 14 root root  4096 Apr  1  2024 ..
-rw-r--r--  1 root root  5375 Dec 23 22:16 alternatives.log
drwxr-xr-x  3 root root  4096 Apr  1  2024 calico
drwxr-xr-x  2 root root 12288 Dec 23 22:19 containers
drwxr-xr-x 17 root root  4096 Oct 29 12:36 pods

```


```
ubuntu@tryhackme:~$ docker logs  cd9ee77b8aa5 > x


+ mount --bind /sys/fs/cgroup/freezer /sys/fs/cgroup/freezer/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ for mount_point in $(echo "${cgroup_mounts}" | cut -d' ' -f 2)
+ local target=/sys/fs/cgroup/hugetlb/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ findmnt /sys/fs/cgroup/hugetlb/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mkdir -p /sys/fs/cgroup/hugetlb/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mount --bind /sys/fs/cgroup/hugetlb /sys/fs/cgroup/hugetlb/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ for mount_point in $(echo "${cgroup_mounts}" | cut -d' ' -f 2)
+ local target=/sys/fs/cgroup/blkio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ findmnt /sys/fs/cgroup/blkio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mkdir -p /sys/fs/cgroup/blkio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mount --bind /sys/fs/cgroup/blkio /sys/fs/cgroup/blkio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ for mount_point in $(echo "${cgroup_mounts}" | cut -d' ' -f 2)
+ local target=/sys/fs/cgroup/net_cls,net_prio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ findmnt /sys/fs/cgroup/net_cls,net_prio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mkdir -p /sys/fs/cgroup/net_cls,net_prio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mount --bind /sys/fs/cgroup/net_cls,net_prio /sys/fs/cgroup/net_cls,net_prio/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ for mount_point in $(echo "${cgroup_mounts}" | cut -d' ' -f 2)
+ local target=/sys/fs/cgroup/memory/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ findmnt /sys/fs/cgroup/memory/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mkdir -p /sys/fs/cgroup/memory/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mount --bind /sys/fs/cgroup/memory /sys/fs/cgroup/memory/docker/cd9ee77b8aa5178125d43be70da40ad8fa08e13ea53ef66498051f3ace582730
+ mount --make-rprivate /sys/fs/cgroup
+ echo '/sys/fs/cgroup/systemd
/sys/fs/cgroup/cpuset
/sys/fs/cgroup/devices
/sys/fs/cgroup/perf_event
/sys/fs/cgroup/pids
/sys/fs/cgroup/rdma
/sys/fs/cgroup/cpu,cpuacct
/sys/fs/cgroup/misc
/sys/fs/cgroup/freezer
/sys/fs/cgroup/hugetlb
/sys/fs/cgroup/blkio
/sys/fs/cgroup/net_cls,net_prio
/sys/fs/cgroup/memory'
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/systemd
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/systemd
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/systemd//kubelet
+ '[' /sys/fs/cgroup/systemd == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/systemd//kubelet /sys/fs/cgroup/systemd//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/systemd
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/systemd
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/systemd//kubelet.slice
+ '[' /sys/fs/cgroup/systemd == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/systemd//kubelet.slice /sys/fs/cgroup/systemd//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/cpuset
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/cpuset
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/cpuset//kubelet
+ '[' /sys/fs/cgroup/cpuset == /sys/fs/cgroup/cpuset ']'
+ cat /sys/fs/cgroup/cpuset/cpuset.cpus
+ cat /sys/fs/cgroup/cpuset/cpuset.mems
+ mount --bind /sys/fs/cgroup/cpuset//kubelet /sys/fs/cgroup/cpuset//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/cpuset
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/cpuset
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/cpuset//kubelet.slice
+ '[' /sys/fs/cgroup/cpuset == /sys/fs/cgroup/cpuset ']'
+ cat /sys/fs/cgroup/cpuset/cpuset.cpus
+ cat /sys/fs/cgroup/cpuset/cpuset.mems
+ mount --bind /sys/fs/cgroup/cpuset//kubelet.slice /sys/fs/cgroup/cpuset//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/devices
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/devices
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/devices//kubelet
+ '[' /sys/fs/cgroup/devices == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/devices//kubelet /sys/fs/cgroup/devices//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/devices
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/devices
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/devices//kubelet.slice
+ '[' /sys/fs/cgroup/devices == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/devices//kubelet.slice /sys/fs/cgroup/devices//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/perf_event
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/perf_event
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/perf_event//kubelet
+ '[' /sys/fs/cgroup/perf_event == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/perf_event//kubelet /sys/fs/cgroup/perf_event//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/perf_event
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/perf_event
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/perf_event//kubelet.slice
+ '[' /sys/fs/cgroup/perf_event == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/perf_event//kubelet.slice /sys/fs/cgroup/perf_event//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/pids
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/pids
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/pids//kubelet
+ '[' /sys/fs/cgroup/pids == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/pids//kubelet /sys/fs/cgroup/pids//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/pids
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/pids
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/pids//kubelet.slice
+ '[' /sys/fs/cgroup/pids == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/pids//kubelet.slice /sys/fs/cgroup/pids//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/rdma
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/rdma
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/rdma//kubelet
+ '[' /sys/fs/cgroup/rdma == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/rdma//kubelet /sys/fs/cgroup/rdma//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/rdma
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/rdma
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/rdma//kubelet.slice
+ '[' /sys/fs/cgroup/rdma == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/rdma//kubelet.slice /sys/fs/cgroup/rdma//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/cpu,cpuacct
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/cpu,cpuacct
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/cpu,cpuacct//kubelet
+ '[' /sys/fs/cgroup/cpu,cpuacct == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/cpu,cpuacct//kubelet /sys/fs/cgroup/cpu,cpuacct//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/cpu,cpuacct
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/cpu,cpuacct
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/cpu,cpuacct//kubelet.slice
+ '[' /sys/fs/cgroup/cpu,cpuacct == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/cpu,cpuacct//kubelet.slice /sys/fs/cgroup/cpu,cpuacct//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/misc
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/misc
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/misc//kubelet
+ '[' /sys/fs/cgroup/misc == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/misc//kubelet /sys/fs/cgroup/misc//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/misc
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/misc
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/misc//kubelet.slice
+ '[' /sys/fs/cgroup/misc == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/misc//kubelet.slice /sys/fs/cgroup/misc//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/freezer
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/freezer
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/freezer//kubelet
+ '[' /sys/fs/cgroup/freezer == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/freezer//kubelet /sys/fs/cgroup/freezer//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/freezer
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/freezer
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/freezer//kubelet.slice
+ '[' /sys/fs/cgroup/freezer == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/freezer//kubelet.slice /sys/fs/cgroup/freezer//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/hugetlb
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/hugetlb
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/hugetlb//kubelet
+ '[' /sys/fs/cgroup/hugetlb == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/hugetlb//kubelet /sys/fs/cgroup/hugetlb//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/hugetlb
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/hugetlb
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/hugetlb//kubelet.slice
+ '[' /sys/fs/cgroup/hugetlb == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/hugetlb//kubelet.slice /sys/fs/cgroup/hugetlb//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/blkio
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/blkio
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/blkio//kubelet
+ '[' /sys/fs/cgroup/blkio == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/blkio//kubelet /sys/fs/cgroup/blkio//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/blkio
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/blkio
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/blkio//kubelet.slice
+ '[' /sys/fs/cgroup/blkio == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/blkio//kubelet.slice /sys/fs/cgroup/blkio//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/net_cls,net_prio
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/net_cls,net_prio
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/net_cls,net_prio//kubelet
+ '[' /sys/fs/cgroup/net_cls,net_prio == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/net_cls,net_prio//kubelet /sys/fs/cgroup/net_cls,net_prio//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/net_cls,net_prio
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/net_cls,net_prio
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/net_cls,net_prio//kubelet.slice
+ '[' /sys/fs/cgroup/net_cls,net_prio == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/net_cls,net_prio//kubelet.slice /sys/fs/cgroup/net_cls,net_prio//kubelet.slice
+ IFS=
+ read -r subsystem
+ mount_kubelet_cgroup_root /kubelet /sys/fs/cgroup/memory
+ local cgroup_root=/kubelet
+ local subsystem=/sys/fs/cgroup/memory
+ '[' -z /kubelet ']'
+ mkdir -p /sys/fs/cgroup/memory//kubelet
+ '[' /sys/fs/cgroup/memory == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/memory//kubelet /sys/fs/cgroup/memory//kubelet
+ mount_kubelet_cgroup_root /kubelet.slice /sys/fs/cgroup/memory
+ local cgroup_root=/kubelet.slice
+ local subsystem=/sys/fs/cgroup/memory
+ '[' -z /kubelet.slice ']'
+ mkdir -p /sys/fs/cgroup/memory//kubelet.slice
+ '[' /sys/fs/cgroup/memory == /sys/fs/cgroup/cpuset ']'
+ mount --bind /sys/fs/cgroup/memory//kubelet.slice /sys/fs/cgroup/memory//kubelet.slice
+ IFS=
+ read -r subsystem
+ [[ ! /sys/fs/cgroup/systemd
/sys/fs/cgroup/cpuset
/sys/fs/cgroup/devices
/sys/fs/cgroup/perf_event
/sys/fs/cgroup/pids
/sys/fs/cgroup/rdma
/sys/fs/cgroup/cpu,cpuacct
/sys/fs/cgroup/misc
/sys/fs/cgroup/freezer
/sys/fs/cgroup/hugetlb
/sys/fs/cgroup/blkio
/sys/fs/cgroup/net_cls,net_prio
/sys/fs/cgroup/memory = */sys/fs/cgroup/systemd* ]]
+ return
+ fix_machine_id
+ echo 'INFO: clearing and regenerating /etc/machine-id'
INFO: clearing and regenerating /etc/machine-id
+ rm -f /etc/machine-id
+ systemd-machine-id-setup
Initializing machine ID from random generator.
+ fix_product_name
+ [[ -f /sys/class/dmi/id/product_name ]]
+ echo 'INFO: faking /sys/class/dmi/id/product_name to be "kind"'
INFO: faking /sys/class/dmi/id/product_name to be "kind"
+ echo kind
+ mount -o ro,bind /kind/product_name /sys/class/dmi/id/product_name
+ fix_product_uuid
+ [[ ! -f /kind/product_uuid ]]
+ [[ -f /sys/class/dmi/id/product_uuid ]]
+ echo 'INFO: faking /sys/class/dmi/id/product_uuid to be random'
INFO: faking /sys/class/dmi/id/product_uuid to be random
+ mount -o ro,bind /kind/product_uuid /sys/class/dmi/id/product_uuid
+ [[ -f /sys/devices/virtual/dmi/id/product_uuid ]]
+ echo 'INFO: faking /sys/devices/virtual/dmi/id/product_uuid as well'
INFO: faking /sys/devices/virtual/dmi/id/product_uuid as well
+ mount -o ro,bind /kind/product_uuid /sys/devices/virtual/dmi/id/product_uuid
+ select_iptables
+ local mode num_legacy_lines num_nft_lines
++ grep -c '^-'
+ num_legacy_lines=6
++ grep -c '^-'
++ true
+ num_nft_lines=0
+ '[' 6 -ge 0 ']'
+ mode=legacy
+ echo 'INFO: setting iptables to detected mode: legacy'
INFO: setting iptables to detected mode: legacy
+ update-alternatives --set iptables /usr/sbin/iptables-legacy
+ echo 'retryable update-alternatives: --set iptables /usr/sbin/iptables-legacy'
+ local 'args=--set iptables /usr/sbin/iptables-legacy'
++ seq 0 15
+ for i in $(seq 0 15)
+ /usr/bin/update-alternatives --set iptables /usr/sbin/iptables-legacy
+ return
+ update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
+ echo 'retryable update-alternatives: --set ip6tables /usr/sbin/ip6tables-legacy'
+ local 'args=--set ip6tables /usr/sbin/ip6tables-legacy'
++ seq 0 15
+ for i in $(seq 0 15)
+ /usr/bin/update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
+ return
+ enable_network_magic
+ local docker_embedded_dns_ip=127.0.0.11
+ local docker_host_ip
++ cut '-d ' -f1
++ head -n1 /dev/fd/63
+++ timeout 5 getent ahostsv4 host.docker.internal
+ docker_host_ip=
+ [[ -z '' ]]
++ ip -4 route show default
++ cut '-d ' -f3
+ docker_host_ip=192.168.49.1
+ iptables-save
+ iptables-restore
+ sed -e 's/-d 127.0.0.11/-d 192.168.49.1/g' -e 's/-A OUTPUT \(.*\) -j DOCKER_OUTPUT/\0\n-A PREROUTING \1 -j DOCKER_OUTPUT/' -e 's/--to-source :53/--to-source 192.168.49.1:53/g' -e 's/p -j DNAT --to-destination 127.0.0.11/p --dport 53 -j DNAT --to-destination 127.0.0.11/g'
+ cp /etc/resolv.conf /etc/resolv.conf.original
++ sed -e s/127.0.0.11/192.168.49.1/g /etc/resolv.conf.original
+ replaced='# Generated by Docker Engine.
# This file can be edited; Docker Engine will not make further changes once it
# has been modified.

nameserver 192.168.49.1
search eu-west-1.compute.internal
options edns0 trust-ad ndots:0

# Based on host file: '\''/etc/resolv.conf'\'' (internal resolver)
# ExtServers: [host(127.0.0.53)]
# Overrides: []
# Option ndots from: internal'
+ [[ '' == '' ]]
+ echo '# Generated by Docker Engine.
# This file can be edited; Docker Engine will not make further changes once it
# has been modified.

nameserver 192.168.49.1
search eu-west-1.compute.internal
options edns0 trust-ad ndots:0

# Based on host file: '\''/etc/resolv.conf'\'' (internal resolver)
# ExtServers: [host(127.0.0.53)]
# Overrides: []
# Option ndots from: internal'
+ files_to_update=('/etc/kubernetes/manifests/etcd.yaml' '/etc/kubernetes/manifests/kube-apiserver.yaml' '/etc/kubernetes/manifests/kube-controller-manager.yaml' '/etc/kubernetes/manifests/kube-scheduler.yaml' '/etc/kubernetes/controller-manager.conf' '/etc/kubernetes/scheduler.conf' '/kind/kubeadm.conf' '/var/lib/kubelet/kubeadm-flags.env')
+ local files_to_update
+ local should_fix_certificate=false
++ cut '-d ' -f1
++ head -n1 /dev/fd/63
++++ hostname
+++ timeout 5 getent ahostsv4 minikube
+ curr_ipv4=192.168.49.2
+ echo 'INFO: Detected IPv4 address: 192.168.49.2'
INFO: Detected IPv4 address: 192.168.49.2
+ '[' -f /kind/old-ipv4 ']'
++ cat /kind/old-ipv4
+ old_ipv4=192.168.49.2
+ echo 'INFO: Detected old IPv4 address: 192.168.49.2'
INFO: Detected old IPv4 address: 192.168.49.2
+ [[ -z 192.168.49.2 ]]
+ [[ 192.168.49.2 != \1\9\2\.\1\6\8\.\4\9\.\2 ]]
+ [[ -n 192.168.49.2 ]]
+ echo -n 192.168.49.2
++ cut '-d ' -f1
++ head -n1 /dev/fd/63
++++ hostname
+++ timeout 5 getent ahostsv6 minikube
+ curr_ipv6=::ffff:192.168.49.2
+ echo 'INFO: Detected IPv6 address: ::ffff:192.168.49.2'
INFO: Detected IPv6 address: ::ffff:192.168.49.2
+ '[' -f /kind/old-ipv6 ']'
++ cat /kind/old-ipv6
+ old_ipv6=::ffff:192.168.49.2
+ echo 'INFO: Detected old IPv6 address: ::ffff:192.168.49.2'
INFO: Detected old IPv6 address: ::ffff:192.168.49.2
+ [[ -z ::ffff:192.168.49.2 ]]
+ [[ ::ffff:192.168.49.2 != \:\:\f\f\f\f\:\1\9\2\.\1\6\8\.\4\9\.\2 ]]
+ [[ -n ::ffff:192.168.49.2 ]]
+ echo -n ::ffff:192.168.49.2
+ false
++ uname -a
+ echo 'entrypoint completed: Linux minikube 5.15.0-1071-aws #77~20.04.1-Ubuntu SMP Thu Oct 3 19:39:59 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux'
entrypoint completed: Linux minikube 5.15.0-1071-aws #77~20.04.1-Ubuntu SMP Thu Oct 3 19:39:59 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
+ exec /sbin/init
systemd 249.11-0ubuntu3.11 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
Detected virtualization docker.
Detected architecture x86-64.

Welcome to Ubuntu 22.04.3 LTS!

Queued start job for default target Graphical Interface.
[  OK  ] Created slice Slice /system/modprobe.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
[  OK  ] Set up automount Arbitrary…s File System Automount Point.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Reached target Network is Online.
[  OK  ] Reached target Path Units.
[  OK  ] Reached target Slice Units.
[  OK  ] Reached target Swaps.
[  OK  ] Reached target Local Verity Protected Volumes.
[  OK  ] Listening on Journal Audit Socket.
[  OK  ] Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket.
         Mounting Huge Pages File System...
         Mounting Kernel Debug File System...
         Mounting Kernel Trace File System...
         Starting Journal Service...
         Starting Create List of Static Device Nodes...
         Starting Load Kernel Module configfs...
         Starting Load Kernel Module fuse...
         Starting Remount Root and Kernel File Systems...
         Starting Apply Kernel Variables...
[  OK  ] Mounted Huge Pages File System.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Mounted Kernel Trace File System.
modprobe@configfs.service: Deactivated successfully.
[  OK  ] Finished Load Kernel Module configfs.
[  OK  ] Finished Create List of Static Device Nodes.
modprobe@fuse.service: Deactivated successfully.
[  OK  ] Finished Load Kernel Module fuse.
         Mounting FUSE Control File System...
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Finished Remount Root and Kernel File Systems.
         Starting Create System Users...
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Started Journal Service.
         Starting Flush Journal to Persistent Storage...
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Finished Create System Users.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
[  OK  ] Finished Apply Kernel Variables.
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Preparation for Local File Systems.
[  OK  ] Reached target Local File Systems.
         Starting Set Up Additional Binary Formats...
         Mounting Arbitrary Executable File Formats File System...
[  OK  ] Mounted Arbitrary Executable File Formats File System.
[  OK  ] Finished Set Up Additional Binary Formats.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Podman auto-update timer.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Timer Units.
[  OK  ] Listening on BuildKit.
         Starting CRI Docker Socket for the API...
         Starting Docker Socket for the API...
         Starting Podman API Socket...
[  OK  ] Listening on CRI Docker Socket for the API.
[  OK  ] Listening on Docker Socket for the API.
[  OK  ] Listening on Podman API Socket.
[  OK  ] Reached target Socket Units.
[  OK  ] Reached target Basic System.
         Starting containerd container runtime...
         Starting minikube automount...
         Starting Podman auto-update service...
         Starting Podman Start All …estart Policy Set To Always...
         Starting Podman API Service...
         Starting OpenBSD Secure Shell server...
[  OK  ] Finished minikube automount.
[  OK  ] Started Podman API Service.
[  OK  ] Started OpenBSD Secure Shell server.
[  OK  ] Started containerd container runtime.
         Starting Docker Application Container Engine...
[  OK  ] Finished Podman Start All … Restart Policy Set To Always.
[  OK  ] Finished Podman auto-update service.
         Stopping containerd container runtime...
[  OK  ] Stopped containerd container runtime.
         Starting containerd container runtime...
[  OK  ] Started containerd container runtime.
[  OK  ] Stopped Docker Application Container Engine.
         Starting Docker Application Container Engine...
[  OK  ] Started Docker Application Container Engine.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Record Runlevel Change in UTMP...
[  OK  ] Finished Record Runlevel Change in UTMP.
```


Now we have something we can use! These logs have been pulled for you and are stored in the `/home/ubuntu/dfir_artefacts/docker-registry-logs.log` file. Let's start by seeing all the different connections that were made to the registry by searching for the HEAD HTTP request code and restricting it down to only the first item, which is the IP:

```
cat docker-registry-logs.log | grep HEAD | cut -d ' ' -f 1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
172.17.0.1
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
10.10.130.253
172.17.0.1
ubuntu@tryhackme:~/dfir_artefacts$ 
```

Here we can see that most of the connections to our registry was made from the expected IP of 172.17.0.1, however, we can see that connections were also made by 10.10.130.253, which is not an IP known to us. Let's find all of the requests made by this IP:

```
ubuntu@tryhackme:~/dfir_artefacts$ cat docker-registry-logs.log | grep '10.10.130.253'


10.10.130.253 - - [29/Oct/2024:10:06:33 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:10:06:33 +0000] "GET /v2/ HTTP/1.1" 200 2 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:10:07:01 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:10:07:01 +0000] "GET /v2/wishlistweb/manifests/latest HTTP/1.1" 404 96 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:10:35:03 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:10:35:03 +0000] "GET /v2/ HTTP/1.1" 200 2 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:24:20 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:24:20 +0000] "GET /v2/ HTTP/1.1" 200 2 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:25:17 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:25:17 +0000] "GET /v2/wishlistweb/manifests/latest HTTP/1.1" 200 6366 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:26:40 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"

10.10.130.253 - - [29/Oct/2024:12:26:40 +0000] "GET /v2/wishlistweb/manifests/latest HTTP/1.1" 200 6366 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"

10.10.130.253 - - [29/Oct/2024:12:26:40 +0000] "GET /v2/wishlistweb/blobs/sha256:6f480e61030add6ab7eed1083fa5aaf33991c9768705b5989898389f3d2fb1b1 HTTP/1.1" 200 15791 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "GET /v2/ HTTP/1.1" 401 87 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:7443399442677cae673e7d1d32044c45a10661138de69b096641e923f3e86f34 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:ffdac6b104559c82f185dc12f124832d2723d9e1623ae5413a44efae229802c2 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:9bfcb9d06442776f2471407e415f7a89341b66ad6aaf63286b5fff56cabd2bb2 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:e065bd5bccc8626be767123110f94faf0d902af1aa7dbe61995982aa40a90c76 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:1472f8b101ad4a27d33cd0d2ba3fad5b84c280169887e85ac16ea492deeb9408 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:8ba9e7f930d6417c6416eee5a9f513d6815c33487c9b8f6fdaeb62a280166efa HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "POST /v2/wishlistweb/blobs/uploads/ HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:1cc91c652f0c971c3c0eb1b78b17128a841f1a8bfe6f3c28820b217644190905 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:e721c0d58e24a795a0838931e4b7a240b2a44391f453690b36eebc1f58808ca6 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:28bdfc1a40787fae1be7ca578c83ae2424be9a5299d9a7a06e37877f53f00540 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:7418cc89daa37ed1dc0bb39f5cac13a4f8ab695e8eb3e5cbf0835cdd3341aa15 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:8a575f293d57f2686322a650ba45c7942643fcfed513c939b7fda0cdfc67716d HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:4f7a1c8ef4832db9fef79e4fcc74c6ff29794f57383ebf39dbbca4ef8efbe259 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:0b7a25b71663985a588e2689f6fb60d3ab1d05a988dee3add62d373b5d4b1065 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:8fdead2af5562e2fc83b11cc3555d4b5ca4a99b8430508a1d5caf0a0743dd775 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:b61cd78121f8eee9718626b086d312581d2d65b1408e72caef6671cc30113429 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:fad4a5a21cfc4286a947b3bc821ef3fc8837fde03d3325883925126c9c919df1 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:b626f562f102b04ab99ccf40928f7534f244cc0024a2508a7c7be44f985a442d HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:4103a3ecbaab14a104f6a681fdc48d40fbc65dabaec87e431be5e4f3db1231db HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:04ad9a19c5b3c55cb353b51cc047482abad628dd4b3746692cdc0afa727625cc HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:3066e34dc7b7668d9b18428240f32f748f3dbe66853abf3272fddf0cb869c388 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:18f5b64f7cefb7cfb9ef8c7c7c53dbeb5f89df30899fab828f70a46e56a5fd53 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:21b7b8e7b9c1560972dc1f2bd577563f37594cdadcc262f91b16ab3d22b863b7 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:65599be66378ba1b7638eb7f0ff71dc10f857d45ad289e61627e1256b3c52945 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:d39ece66b66711cd10d00ecca889e6d9471a6c746abd4b1864d5159396013b07 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:e12192999ff18f01315563c63333d7c1059cd8e64dffe75fffe504b95eeb093c HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:01b8b12bad90b51d9f15dd4b63103ea6221b339ac3b3e75807c963e678f28624 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:c5d85cf7a05fec99bb829db84dc5a21cc0aca569253f45d1ea10ca9e8a03fa9a HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:b6b268720157210d21bbe49f6112f815774e6d2a6144b14911749fadfdb034f0 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "HEAD /v2/wishlistweb/blobs/sha256:c64513b741452f95d8a147b69c30f403f6289542dd7b2b51dd8ba0cb35d0e08b HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "PATCH /v2/wishlistweb/blobs/uploads/29667052-1161-4ef0-aa89-dc40a2ff1bcb?_state=AYqTsngRJQiO8AkQuMPShxj8LsmV_ePzL0IgISK-N7N7Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiIyOTY2NzA1Mi0xMTYxLTRlZjAtYWE4OS1kYzQwYTJmZjFiY2IiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MjguNzA0Njc2NTM5WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PUT /v2/wishlistweb/blobs/uploads/29667052-1161-4ef0-aa89-dc40a2ff1bcb?_state=6Aye5AM5Uy_Z74MhYny1-0S1pYQa76kz9YU60pvstPJ7Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiIyOTY2NzA1Mi0xMTYxLTRlZjAtYWE4OS1kYzQwYTJmZjFiY2IiLCJPZmZzZXQiOjEzNTcxNjU0LCJTdGFydGVkQXQiOiIyMDI0LTEwLTI5VDEyOjM0OjI4WiJ9&digest=sha256%3A22c40f93a8f43440cfb0f9ba897e06533f430b53b8f2dcda5ca800e73e3aaa72 HTTP/1.1" 201 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "HEAD /v2/wishlistweb/blobs/sha256:22c40f93a8f43440cfb0f9ba897e06533f430b53b8f2dcda5ca800e73e3aaa72 HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "HEAD /v2/wishlistweb/blobs/sha256:f02c090f7c32d5b1ebf169cabea6e9f5dc2fba679390b5b24a9d7a3d0dd1ebac HTTP/1.1" 404 157 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "POST /v2/wishlistweb/blobs/uploads/ HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PATCH /v2/wishlistweb/blobs/uploads/7d53a7ab-7489-4580-9d60-057ded8d5b15?_state=qgIkGiYWdoRmfiuY42h1hpHXQM89dTDL3Ag7YsIUQA17Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiI3ZDUzYTdhYi03NDg5LTQ1ODAtOWQ2MC0wNTdkZWQ4ZDViMTUiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MzEuODEwNzI0NTQ1WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PUT /v2/wishlistweb/blobs/uploads/7d53a7ab-7489-4580-9d60-057ded8d5b15?_state=s-667yZQ5GF6_BrG9u3L5NeKj9d-HrbRFxNghcU_BiV7Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiI3ZDUzYTdhYi03NDg5LTQ1ODAtOWQ2MC0wNTdkZWQ4ZDViMTUiLCJPZmZzZXQiOjE1OTc5LCJTdGFydGVkQXQiOiIyMDI0LTEwLTI5VDEyOjM0OjMxWiJ9&digest=sha256%3Af02c090f7c32d5b1ebf169cabea6e9f5dc2fba679390b5b24a9d7a3d0dd1ebac HTTP/1.1" 201 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "HEAD /v2/wishlistweb/blobs/sha256:f02c090f7c32d5b1ebf169cabea6e9f5dc2fba679390b5b24a9d7a3d0dd1ebac HTTP/1.1" 200 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PUT /v2/wishlistweb/manifests/latest HTTP/1.1" 201 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
```

Now, we are getting somewhere. If we review the first few requests, we can see that several authentication attempts were made. But, we can also see that the request to read the manifest for the wishlistweb image succeeded, as the HTTP status code of 200 is returned in this log entry:

```
10.10.130.253 - - [29/Oct/2024:12:26:40 +0000] "GET /v2/wishlistweb/manifests/latest HTTP/1.1" 200 6366 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
```

What we also notice is the User Agent in the request is docker, meaning this was a request made through the docker CLI to pull the image. This is confirmed as we see several requests then to download the image. From this, we learn several things:

- The docker CLI application was used to connect to the registry.
- Connections came from 10.10.130.253, which is unexpected since we only upload images from 172.17.0.1.
- The client was authenticated, which allowed the image to be pulled. This means that whoever made the request had access to credentials.

If they had access to credentials to pull an image, the same credentials might have allowed them to also push a new image.  We can verify this by narrowing our search to any PATCH HTTP methods. The PATCH method is used to update docker images in a registry:

```bash
ubuntu@tryhackme:~/dfir_artefacts$ cat docker-registry-logs.log | grep '10.10.130.253' | grep PATCH
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "PATCH /v2/wishlistweb/blobs/uploads/29667052-1161-4ef0-aa89-dc40a2ff1bcb?_state=AYqTsngRJQiO8AkQuMPShxj8LsmV_ePzL0IgISK-N7N7Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiIyOTY2NzA1Mi0xMTYxLTRlZjAtYWE4OS1kYzQwYTJmZjFiY2IiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MjguNzA0Njc2NTM5WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"

10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PATCH /v2/wishlistweb/blobs/uploads/7d53a7ab-7489-4580-9d60-057ded8d5b15?_state=qgIkGiYWdoRmfiuY42h1hpHXQM89dTDL3Ag7YsIUQA17Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiI3ZDUzYTdhYi03NDg5LTQ1ODAtOWQ2MC0wNTdkZWQ4ZDViMTUiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MzEuODEwNzI0NTQ1WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
ubuntu@tryhackme:~/dfir_artefacts$ 
```

This is not good! It means that Mayor Malware could push a new version of our image! This would explain how the webshell made its way into the image, since Mayor Malware pulled the image, made malicious updates, and then pushed this compromised image back to the registry! Use the information to answer questions 4 through 6 at the bottom of the task. Now that we know Mayor Malware had access to the credentials of the docker registry, we need to learn how he could have gained access to them. We use these credentials in our Kubernetes cluster to read the image from the registry, so let's see what could have happened to disclose them!

Okay, so it looks like the attack happened via an authenticated docker registry push. Now, it's time to return to our Kubernetes environment and determine how this was possible. 

McSkidy was made aware that Mayor Malware was given user access to the naughty or nice Kubernetes environment but was assured by the DevSecOps team that he wouldn't have sufficient permissions to view secrets, etc. The first thing we should do is make sure this is the case. To do this, McSkidy decides to check what role was assigned to the mayor. She first checks the rolebindings (binds a role to a user):

```
ubuntu@tryhackme:~/dfir_artefacts$ kubectl get rolebindings -n wareville
NAME                 ROLE              AGE
job-runner-binding   Role/job-runner   67d
mayor-user-binding   Role/mayor-user   67d
ubuntu@tryhackme:~/dfir_artefacts$ 
```

McSkidy then sees a rolebinding named after Mayor Malware and decides to take a closer look:
```
ubuntu@tryhackme:~/dfir_artefacts$ kubectl describe rolebinding mayor-user-binding -n wareville
Name:         mayor-user-binding
Labels:       <none>
Annotations:  <none>
Role:
  Kind:  Role
  Name:  mayor-user
Subjects:
  Kind  Name           Namespace
  ----  ----           ---------
  User  mayor-malware  

```

From the output, she could see that there is a role "mayor-user" that is bound to the user "mayor-malware". McSkidy then checked this role to see what permissions it has (and therefore Mayor Malware had):

```
ubuntu@tryhackme:~/dfir_artefacts$ kubectl describe role mayor-user -n wareville
Name:         mayor-user
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources                               Non-Resource URLs  Resource Names  Verbs
  ---------                               -----------------  --------------  -----
  pods/exec                               []                 []              [create get list]
  rolebindings.rbac.authorization.k8s.io  []                 []              [get list describe]
  roles.rbac.authorization.k8s.io         []                 []              [get list describe]
  pods                                    []                 []              [get list watch]
ubuntu@tryhackme:~/dfir_artefacts$          
```

The output here tells McSkidy something very important. A lot of the permissions listed here are as you would expect for a non-admin user in a Kubernetes environment, all of those except for the permissions associated with "pods/exec". Exec allows the user to shell into the containers running within a pod. This gives McSkidy an idea of what Mayor Malware might have done. To confirm her suspicious, she checks the audit logs for Mayor Malware's activity:

```bash
ubuntu@tryhackme:~/dfir_artefacts$ cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"RequestResponse","auditID":"a02486f1-3a7c-4bca-8bcb-9019fa43dac4","stage":"RequestReceived","requestURI":"/api/v1/namespaces/wareville/secrets?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"secrets","namespace":"wareville","apiVersion":"v1"},"requestReceivedTimestamp":"2024-10-29T12:20:30.664633Z","stageTimestamp":"2024-10-29T12:20:30.664633Z"}

{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"RequestResponse","auditID":"a02486f1-3a7c-4bca-8bcb-9019fa43dac4","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/secrets?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"secrets","namespace":"wareville","apiVersion":"v1"},"responseStatus":{"metadata":{},"status":"Failure","message":"secrets is forbidden: User \"mayor-malware\" cannot list resource \"secrets\" in API group \"\" in the namespace \"wareville\"","reason":"Forbidden","details":{"kind":"secrets"},"code":403},"responseObject":{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"secrets is forbidden: User \"mayor-malware\" cannot list resource \"secrets\" in API group \"\" in the namespace \"wareville\"","reason":"Forbidden","details":
{"kind":"secrets"},"code":403},"requestReceivedTimestamp":"2024-10-29T12:20:30.664633Z","stageTimestamp":"2024-10-29T12:20:30.666165Z","annotations":{"authorization.k8s.io/decision":"forbid","authorization.k8s.io/reason":""}}

{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"8084daec-f59f-4d90-b343-f59f4f3cd67c","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/roles?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"roles","namespace":"wareville","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:20:39.761026Z","stageTimestamp":"2024-10-29T12:20:39.762868Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}


{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"01891338-4f15-4121-b779-e7ace5764d4f","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/roles/job-runner","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"roles","namespace":"wareville","name":"job-runner","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:20:49.491912Z","stageTimestamp":"2024-10-29T12:20:49.494511Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}


{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"6ef973f4-82ab-4326-b66b-24d7036cae64","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/roles/job-runner","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"roles","namespace":"wareville","name":"job-runner","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:20:49.497325Z","stageTimestamp":"2024-10-29T12:20:49.498588Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}


{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"25b7417e-550c-4b9a-bb2c-dad64662cce0","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/rolebindings?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"rolebindings","namespace":"wareville","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:20:59.570824Z","stageTimestamp":"2024-10-29T12:20:59.575620Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"b0f9aa98-9039-4df8-b990-9bf6ca48ab2f","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/rolebindings/job-runner-binding","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"rolebindings","namespace":"wareville","name":"job-runner-binding","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:11.521236Z","stageTimestamp":"2024-10-29T12:21:11.523301Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"a8043bea-e489-418d-8fa4-260a7d96171f","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/rolebindings/job-runner-binding","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"rolebindings","namespace":"wareville","name":"job-runner-binding","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:11.524795Z","stageTimestamp":"2024-10-29T12:21:11.526478Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"9d13a9b6-78d2-4cfc-8dc5-889b83aafc44","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/pods?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:22.660584Z","stageTimestamp":"2024-10-29T12:21:22.664112Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"5965471b-4fb9-49c9-9a16-7fd466c762c8","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/pods/morality-checker","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","name":"morality-checker","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:33.182365Z","stageTimestamp":"2024-10-29T12:21:33.185006Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"205fbd55-d2a9-408f-8e28-9fa1d47ea95b","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/pods/morality-checker","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","name":"morality-checker","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:33.187353Z","stageTimestamp":"2024-10-29T12:21:33.188742Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"24444640-7e57-4ac9-b7e8-c3bf5a2942d9","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/events?fieldSelector=involvedObject.name%3Dmorality-checker%2CinvolvedObject.namespace%3Dwareville%2CinvolvedObject.uid%3Da20761b8-1a36-4318-a048-96d61644b436\u0026limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"events","namespace":"wareville","apiVersion":"v1"},"responseStatus":{"metadata":{},"status":"Failure","message":"events is forbidden: User \"mayor-malware\" cannot list resource \"events\" in API group \"\" in the namespace \"wareville\"","reason":"Forbidden","details":{"kind":"events"},"code":403},"requestReceivedTimestamp":"2024-10-29T12:21:33.194329Z","stageTimestamp":"2024-10-29T12:21:33.194846Z","annotations":{"authorization.k8s.io/decision":"forbid","authorization.k8s.io/reason":""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"7fc89d4f-a2e2-4223-b25e-a46f05fce881","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/pods/morality-checker","verb":"get","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","name":"morality-checker","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:21:44.176371Z","stageTimestamp":"2024-10-29T12:21:44.179359Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"927fcde7-74e5-4a57-af53-dceacefaf47c","stage":"ResponseStarted","requestURI":"/api/v1/namespaces/wareville/pods/morality-checker/exec?command=%2Fbin%2Fsh\u0026container=kubectl-container\u0026stdin=true\u0026stdout=true\u0026tty=true","verb":"create","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","name":"morality-checker","apiVersion":"v1","subresource":"exec"},"responseStatus":{"metadata":{},"code":101},"requestReceivedTimestamp":"2024-10-29T12:21:44.189258Z","stageTimestamp":"2024-10-29T12:21:44.214173Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"927fcde7-74e5-4a57-af53-dceacefaf47c","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/pods/morality-checker/exec?command=%2Fbin%2Fsh\u0026container=kubectl-container\u0026stdin=true\u0026stdout=true\u0026tty=true","verb":"create","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"pods","namespace":"wareville","name":"morality-checker","apiVersion":"v1","subresource":"exec"},"responseStatus":{"metadata":{},"code":101},"requestReceivedTimestamp":"2024-10-29T12:21:44.189258Z","stageTimestamp":"2024-10-29T12:22:19.873022Z","annotations":{"apiserver.latency.k8s.io/etcd":"1.150272ms","apiserver.latency.k8s.io/total":"35.683763759s","authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}

```

This log snippet tells us that Mayor Malware attempted to get the secrets stored on the cluster but received a 403 response as he didn't have sufficient permissions to do so (Note: a plural get command runs a list on the backend, and is why it appears as so in the logs).

**Get Roles**

```
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"RequestResponse","auditID":"a02486f1-3a7c-4bca-8bcb-9019fa43dac4","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/wareville/secrets?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"secrets","namespace":"wareville","apiVersion":"v1"},"responseStatus":{"metadata":{},"status":"Failure","message":"secrets is forbidden: User \"mayor-malware\" cannot list resource \"secrets\" in API group \"\" in the namespace \"wareville\"","reason":"Forbidden","details":{"kind":"secrets"},"code":403},"responseObject":{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"secrets is forbidden: User \"mayor-malware\" cannot list resource \"secrets\" in API group \"\" in the namespace \"wareville\"","reason":"Forbidden","details":
{"kind":"secrets"},"code":403},"requestReceivedTimestamp":"2024-10-29T12:20:30.664633Z","stageTimestamp":"2024-10-29T12:20:30.666165Z","annotations":{"authorization.k8s.io/decision":"forbid","authorization.k8s.io/reason":""}}

```

After being denied secret access, Mayor Malware then started snooping to see what roles were present on the cluster.

**Describe Role**

```
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"8084daec-f59f-4d90-b343-f59f4f3cd67c","stage":"ResponseComplete","requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/wareville/roles?limit=500","verb":"list","user":{"username":"mayor-malware","groups":["example","system:authenticated"]},"sourceIPs":["192.168.49.1"],"userAgent":"kubectl/v1.29.3 (linux/amd64) kubernetes/6813625","objectRef":{"resource":"roles","namespace":"wareville","apiGroup":"rbac.authorization.k8s.io","apiVersion":"v1"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2024-10-29T12:20:39.761026Z","stageTimestamp":"2024-10-29T12:20:39.762868Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"mayor-user-binding/wareville\" of Role \"mayor-user\" to User \"mayor-malware\""}}
```

Whilst running the previous "get roles" command, Mayor Malware will have found a role named "job-runner". These logs tell us that Mayor Malware then described this role, which would have given him key pieces of information regarding the role. Most importantly for our investigation, it would have told him this role has secret read access.

**Get Rolebindings**

```
cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
```

Now, knowing this role can view secrets, Mayor Malware tried to find its role binding to see what was using this role.

**Describe Rolebinding**

After seeing a role binding named "job-runner-binding", Mayor Malware described it and found out this role is bound to a service account named "job-runner-sa" (aka this service account has permission to view secrets)

```
cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
```


**Get Pods**

Here, we can see that Mayor Malware, now armed with the knowledge that a service account has the permissions he needs, lists all of the pods running in the Wareville namespace with a kubectl get pods command.

```
cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
```

**Describe Pod**

Mayor Malware describes the pod as a "morality-checker" he then would have found out that this pod runs with the job-runner-sa service account attached. Meaning that if he were able to gain access to this pod, he would be able to gain secret read access.

```
cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
```

**Exec**

As mentioned in the role discussion, exec is permission usually not included in a non-admin role. It is for this exact reason that this is the case; McSkidy feels confident that the DevSecOps team had overly permissive Role-Based Access Control (RBAC) in place in the Kubernetes environment, and it was this that allowed Mayor Malware to run an exec command (as captured by the logs above) and gain shell access into morality-checker. To confirm her suspicions further, McSkidy runs the following command to retrieve audit logs captured from the job-runner-sa service account:

```
cat audit.log | grep --color=always '"user":{"username":"mayor-malware"' | grep --color=always '"resource"' | grep --color=always '"verb"'
```





The final piece of the puzzle revolved around this secret. Finally, she runs the command, and the attack path is confirmed:

```
kubectl get secret pull-creds -n wareville -o jsonpath='{.data.\.dockerconfigjson}' | base64 --decode

{"auths":{"http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}

```

Shaking her head, McSkidy then confirms that the docker registry pull password is the same as the push password. This means that after retrieving these credentials, Mayor Malware would have been able to make the docker registry push we saw earlier and ensure his malicious web shell was deployed into the Kubernetes environment and gain persistence. It is for this reason that push and pull credentials should always be different. With that, the investigation is all tied up, the conclusion being that Mayor Malware most certainly belongs on the naughty list this year!



### Answer the questions below

What is the name of the webshell that was used by Mayor Malware?

 `shelly.php`
 
What file did Mayor Malware read from the pod?

`db.php`

What tool did Mayor Malware search for that could be used to create a remote connection from the pod?

`nc`

What IP connected to the docker registry that was unexpected?

`10.10.130.253`

At what time is the first connection made from this IP to the docker registry?

 ```
 cat docker-registry-logs.log | grep "10.10.130.253" | head
 
 29/Oct/2024:10:06:33 +0000
 
```

At what time is the updated malicious image pushed to the registry?

```
cat docker-registry-logs.log | grep "10.10.130.253" | grep "PATCH"
10.10.130.253 - - [29/Oct/2024:12:34:28 +0000] "PATCH /v2/wishlistweb/blobs/uploads/29667052-1161-4ef0-aa89-dc40a2ff1bcb?_state=AYqTsngRJQiO8AkQuMPShxj8LsmV_ePzL0IgISK-N7N7Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiIyOTY2NzA1Mi0xMTYxLTRlZjAtYWE4OS1kYzQwYTJmZjFiY2IiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MjguNzA0Njc2NTM5WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"
10.10.130.253 - - [29/Oct/2024:12:34:31 +0000] "PATCH /v2/wishlistweb/blobs/uploads/7d53a7ab-7489-4580-9d60-057ded8d5b15?_state=qgIkGiYWdoRmfiuY42h1hpHXQM89dTDL3Ag7YsIUQA17Ik5hbWUiOiJ3aXNobGlzdHdlYiIsIlVVSUQiOiI3ZDUzYTdhYi03NDg5LTQ1ODAtOWQ2MC0wNTdkZWQ4ZDViMTUiLCJPZmZzZXQiOjAsIlN0YXJ0ZWRBdCI6IjIwMjQtMTAtMjlUMTI6MzQ6MzEuODEwNzI0NTQ1WiJ9 HTTP/1.1" 202 0 "" "docker/19.03.12 go/go1.13.10 git-commit/48a66213fe kernel/4.15.0-213-generic os/linux arch/amd64 UpstreamClient(Docker-Client/19.03.12 \\(linux\\))"

```

What is the value stored in the "pull-creds" secret?

```
kubectl get secret pull-creds -n wareville -o jsonpath='{.data.\.dockerconfigjson}' | base64 --decode

{"auths":{"http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}

```

Enjoy today's lesson? Check out our [Intro to Kubernetes](https://tryhackme.com/r/room/introtok8s) for a more in-depth introduction to Kubernetes!


