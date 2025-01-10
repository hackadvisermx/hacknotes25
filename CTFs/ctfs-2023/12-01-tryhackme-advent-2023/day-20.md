
# Task 26  [Day 20] DevSecOps Advent of Frostlings

## Learning Objectives

In today's task, you will:

- Learn about poisoned pipeline execution.
- Understand how to secure CI/CD pipelines.
- Get an introduction to secure software development lifecycles (SSDLC) & DevSecOps.
- Learn about CI/CD best practices.

## GitLab and SDLC Concepts

GitLab is a platform that enables collaboration and automation throughout the software development lifecycle, which is the framework structure that describes the stages that code goes through, from design and development to deployment. GitLab is built around Git, a distributed version control system (VCS) where code is managed.

Here are the key components of GitLab:

- **Version control system:** A VCS is the environment where you manage and track changes made in the codebase. It makes it easier to collaborate with others and maintain the history and versioning of a project.
- **CI/CD pipelines:** Pipelines automate the building, testing, and deployment processes. Pipelines ensure the code is consistently integrated, tested, and delivered to the specified environment (production or staging).
- **Security scanning:** GitLab has a few scanning features, like incorporating static application security testing (SAST), dynamic application security testing (DAST), container scanning, and dependency scanning. All these tools help identify and mitigate security threats in code and infrastructure.

## CI/CD

We mentioned CI/CD earlier in the context of pipelines. CI/CD stands for continuous integration and continuous delivery.

- **Continuous integration:** CI refers to integrating code changes from multiple contributors into a shared repository (where code is stored in a VCS; you can think of it as a folder structure). In GitLab, CI allows developers and engineers to commit code frequently, triggering automations that lead to builds and tests. This is what CI is all about: ensuring that code changes and updates are continuously validated, which reduces the likelihood of vulnerabilities when introducing security scans and tests as part of the validation process (here, we start entering the remit of DevSecOps).
- **Continuous deployment:** CD automates code deployment to different environments. During SDLC, code travels to environments like sandbox and staging, where the tests and validations are performed before they go into the production environment. The production environment is where the final version of an app or service lives, which is what we, as users, tend to see. CD pipelines ensure the code is securely deployed consistently and as part of DevSecOps. Integrating security checks before deployment to production is key.

## DevSecOps

We have mentioned that integrating security into CI/CD ensures consistency and threat reduction when integrating it into the SDLC. This is what DevSecOps aims to achieve. Everything we have seen so far is part of a cultural and technical approach that aims to improve collaboration, automation, and CI/CD. It's what we call developer operations, or DevOps for short. DevSecOps was born from DevOps and is an extension specialising in security for DevOps practices.

## CI/CD Attacks: PPE

In today's AoC, you will learn about poisoned pipeline execution. This type of attack involves compromising a component or stage in the SDLC. For this attack to work, it takes advantage of the trust boundaries established within the supply chain, which is extremely common in CI/CD, where automation is everywhere.

When an attacker has access to version control systems and can manipulate the build process by injecting malicious code into the pipeline, they don't need access to the build environment. This is where the "poisoned" pipelines come into play. It's crucial to have effective, secure gates and guardrails to prevent malicious code from getting far if there is an account compromise.

## Answer the questions below

What is the handle of the developer responsible for the merge changes?

 @BadSecOps

What port is the defaced calendar site server running on?  

9081

What server is the malicious server running on?  

 apache

What message did the Frostlings leave on the defaced site?  

 frostlings rule :)

What is the commit ID of the original code for the Advent Calendar site?  

 986b7407

If you enjoyed today's challenge, please check out the [Source Code Security](https://tryhackme.com/room/sourcecodesecurity) room.







I completed  Task 26  [Day 20] DevSecOps Advent of Frostlings !, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023