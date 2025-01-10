# Nuclei

https://github.com/projectdiscovery/nuclei


## Instalar Nuclei
```shell
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
nuclei -update-templates
```




Weaponizes nuclei Workflows to Pwn All the Things
https://medium.com/@dwi.siswanto98/weaponizes-nuclei-workflows-to-pwn-all-the-things-cd01223feb77

## Configuracion

## templates

```
cves
vulnerabilities
exposed-panels
takeovers
exposures
technologies
misconfiguration
workflows
miscellaneous
default-logins
file
dns
fuzzing
helpers
iot
```


## Ejemplos

```bash
nuclei -id CVE-2022-26134 -l targets.txt -vv
nuclei -w workflows/fortinet-workflow.yaml -l targets.txt
nuclei -t cves/2022 -l targets.txt -vv
nuclei -t takeovers -l targets.txt

nuclei -t cves/ -severity critical -l targets.txt
nuclei -t cves/ -t vulnerabilities -severity critical,high -l targets.txt

nuclei -t exposures/apis/ -l targets.txt

nuclei -t vulnerabilities/wordpress/ -l targets.txt
```

