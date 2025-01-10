#threatintelligence

Threat Intelligence is the analysis of data and information using tools and techniques to generate meaningful patterns on how to mitigate against potential risks associated with existing or emerging threats targeting organisations, industries, sectors or governments.

To mitigate against risks, we can start by trying to answer a few simple questions:

-   Who's attacking you?
-   What's their motivation?
-   What are their capabilities?
-   What artefacts and indicators of compromise should you look out for?

With these questions, threat intelligence would be gathered from different sources under the following categories:

-   **Internal:**    
    -   Corporate security events such as vulnerability assessments and incident response reports.
    -   Cyber awareness training reports.
    -   System logs and events.
-   **Community:**
    -   Open web forums.
    -   Dark web communities for cybercriminals.
-   **External**
    -   Threat intel feeds (Commercial & Open-source)
    -   Online marketplaces.
    -   Public sources include government data, publications, social media, financial and industrial assessments.

## Threat Intelligence Classifications:

Threat Intel is geared towards understanding the relationship between your operational environment and your adversary. With this in mind, we can break down threat intel into the following classifications:
-   **Strategic Intel:** 
	- High-level intel that looks into the organisation’s threat landscape and maps out the risk areas based on trends, patterns and emerging threats that may impact business decisions.
-   **Technical Intel:** 
	- Looks into evidence and artefacts of attack used by an adversary. Incident Response teams can use this intel to create a baseline attack surface to analyse and develop defence mechanisms.
-   **Tactical Intel:** 
	- Assesses adversaries’ tactics, techniques, and procedures (TTPs). This intel can strengthen security controls and address vulnerabilities through real-time investigations.
-   **Operational Intel:** 
	- Looks into an adversary’s specific motives and intent to perform an attack. Security teams may use this intel to understand the critical assets available in the organisation (people, processes and technologies) that may be targeted.


## TTP Mapping

**TTP Mapping** is employed by the red cell to map adversaries' collected TTPs to a standard cyber kill chain. Mapping TTPs to a kill chain aids the red team in planning an engagement to emulate an adversary.

To begin the process of mapping TTPs, an adversary must be selected as the target. An adversary can be chosen based on,

1.  Target Industry
2.  Employed Attack Vectors
3.  Country of Origin
4.  Other Factors

#### OST-Map
https://www.intezer.com/ost-map/



## CTI Life Cycle
Threat intel is obtained from a data-churning process that transforms raw data into contextualised and action-oriented insights geared towards triaging security incidents. The transformational process follows a six-phase cycle.

### Direction
Every threat intel program requires to have objectives and goals defined, involving identifying the following parameters:
-   Information assets and business processes that require defending.
-   Potential impact to be experienced on losing the assets or through process interruptions.
-   Sources of data and intel to be used towards protection.
-   Tools and resources that are required to defend the assets.
This phase also allows security analysts to pose questions related to investigating incidents.

### Collection
Once objectives have been defined, security analysts will gather the required data to address them. Analysts will do this by using commercial, private and open-source resources available. Due to the volume of data analysts usually face, it is recommended to automate this phase to provide time for triaging incidents.

### Processing
Raw logs, vulnerability information, malware and network traffic usually come in different formats and may be disconnected when used to investigate an incident. This phase ensures that the data is extracted, sorted, organised, correlated with appropriate tags and presented visually in a usable and understandable format to the analysts. SIEMs are valuable tools for achieving this and allow quick parsing of data.

### Analysis
Once the information aggregation is complete, security analysts must derive insights. Decisions to be made may involve:
-   Investigating a potential threat through uncovering indicators and attack patterns.
-   Defining an action plan to avert an attack and defend the infrastructure.
-   Strengthening security controls or justifying investment for additional resources.  

### Dissemination
Different organisational stakeholders will consume the intelligence in varying languages and formats. For example, C-suite members will require a concise report covering trends in adversary activities, financial implications and strategic recommendations. At the same time, analysts will more likely inform the technical team about the threat IOCs, adversary TTPs and tactical action plans.

### Feedback
The final phase covers the most crucial part, as analysts rely on the responses provided by stakeholders to improve the threat intelligence process and implementation of security controls. Feedback should be regular interaction between teams to keep the lifecycle working.


## CTI Standards & Frameworks
Standards and frameworks provide structures to rationalise the distribution and use of threat intel across industries. They also allow for common terminology, which helps in collaboration and communication. Here, we briefly look at some essential standards and frameworks commonly used.

### MITRE ATT&CK®
The ATT&CK framework is a knowledge base of adversary behaviour, focusing on the indicators and tactics. Security analysts can use the information to be thorough while investigating and tracking adversarial behaviour. MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

### TAXII
The Trusted Automated eXchange of Indicator Information (TAXII) defines protocols for securely exchanging threat intel to have near real-time detection, prevention and mitigation of threats. The protocol supports two sharing models:
- Collection: Threat intel is collected and hosted by a producer upon request by users using a request-response model.
- Channel: Threat intel is pushed to users from a central server through a publish-subscribe model.

### STIX
Structured Threat Information Expression (STIX) is a language developed for the "specification, capture, characterisation and communication of standardised cyber threat information". It provides defined relationships between sets of threat info such as observables, indicators, adversary TTPs, attack campaigns, and more.

### Cyber Kill Chain
Developed by Lockheed Martin, the Cyber Kill Chain breaks down adversary actions into steps. This breakdown helps analysts and defenders identify which stage-specific activities occurred when investigating an attack. The phases defined are shown in the image below.

| Technique | Purpose | Examples |
| --- | --- | --- |
| Reconnaissance | Obtain information about the victim and the tactics used for the attack. | Harvesting emails, OSINT, and social media, network scans |
| Weaponisation | Malware is engineered based on the needs and intentions of the attack. | Exploit with backdoor, malicious office document |
| Delivery | Covers how the malware would be delivered to the victim's system. | Email, weblinks, USB |
| Exploitation | Breach the victim's system vulnerabilities to execute code and create scheduled jobs to establish persistence. | EternalBlue, Zero-Logon, etc. |
| Installation | Install malware and other tools to gain access to the victim's system. | Password dumping, backdoors, remote access trojans |
| Command & Control | Remotely control the compromised system, deliver additional malware, move across valuable assets and elevate privileges. | Empire, Cobalt Strike, etc. |
| Actions on Objectives | Fulfil the intended goals for the attack: financial gain, corporate espionage, and data exfiltration. | Data encryption, ransomware, public defacement |




## Referencias
#### Tryhackme rooms
- https://tryhackme.com/room/threatinteltools
- https://tryhackme.com/room/cyberthreatintel
- https://tryhackme.com/room/mitre

#### Ligas
- [MITRE ATT&CK](https://attack.mitre.org/)
- [TAXII](https://oasis-open.github.io/cti-documentation/taxii/intro)
- [STIX](https://oasis-open.github.io/cti-documentation/stix/intro)



- https://urlscan.io/
- https://abuse.ch/
- https://app.phishtool.com/
- https://talosintelligence.com/
- https://www.virustotal.com



# Convertir html to markdown

https://www.convertsimple.com/convert-html-to-markdown/