https://hhc23-wetty.holidayhackchallenge.com/?&challenge=azure101&username=hackadviser&id=7fce7d26-ccc9-4f55-8100-3806f4245556&area=ci-rudolphsrest&location=5,27&tokens=azure101&dna=ATATATTAATATATATATATTATAATATATATCGATCGGCATATATATATATATATATATATATATATATTAATATCGTAATATATATATATGCATATATATATATATTATAATATATTA


- Este vato guardo algunas cosas aqui > Alabaster Snowball

```
elf@4296ceb7ed22:~$ cat .azure/az.json 
{}elf@4296ceb7ed22:~$ cat .azure/azureProfile.json 
{
  "subscriptions": [
    {
      "id": "2b0942f3-9bca-484b-a508-abdae2db5e64",
      "name": "northpole-sub",
      "state": "Enabled",
      "user": {
        "name": "northpole@northpole.invalid",
        "type": "user"
      },
      "isDefault": true,
      "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
      "environmentName": "AzureCloud"
    }
  ],
  "installationId": "1de3b9db-5e5b-48a5-81e5-7eafe2d2bace"
}elf@4296ceb7ed22:~$ 
```

```
az account show
{
  "environmentName": "AzureCloud",
  "id": "2b0942f3-9bca-484b-a508-abdae2db5e64",
  "isDefault": true,
  "name": "northpole-sub",
  "state": "Enabled",
  "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
  "user": {
    "name": "northpole@northpole.invalid",
    "type": "user"
  }
}
```

- listar grupos de recursos a los que tengo acceso

```
elf@6cd96aa97620:~/.azure$ az group list
[
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1",
    "location": "eastus",
    "managedBy": null,
    "name": "northpole-rg1",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  },
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg2",
    "location": "westus",
    "managedBy": null,
    "name": "northpole-rg2",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  }
]
elf@6cd96aa97620:~/.azure$ 
```

- listar vms en esos resource groups
```
az vm list -g northpole-rg2
[
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg2/providers/Microsoft.Compute/virtualMachines/NP-VM1",
    "location": "eastus",
    "name": "NP-VM1",
    "properties": {
      "hardwareProfile": {
        "vmSize": "Standard_D2s_v3"
      },
      "provisioningState": "Succeeded",
      "storageProfile": {
        "imageReference": {
          "offer": "UbuntuServer",
          "publisher": "Canonical",
          "sku": "16.04-LTS",
          "version": "latest"
        },
        "osDisk": {
          "caching": "ReadWrite",
          "createOption": "FromImage",
          "managedDisk": {
            "storageAccountType": "Standard_LRS"
          },
          "name": "VM1_OsDisk_1"
        }
      },
      "vmId": "e5f16214-18be-4a31-9ebb-2be3a55cfcf7"
    },
    "resourceGroup": "northpole-rg2",
    "tags": {}
  }
]
```

- ejecutar comando el la vm

```
az vm run-command invoke -g northpole-rg2 --name NP-VM1 --command-id RunShellScript --scripts "echo helloworld"

az vm show -g northpole-rg2 --name NP-VM1


az functionapp list -g northpole-rg2
```

```
[
  {
    "appServicePlanId": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/serverfarms/EastUSLinuxDynamicPlan",
    "availabilityState": "Normal",
    "clientAffinityEnabled": false,
    "clientCertEnabled": false,
    "clientCertExclusionPaths": null,
    "clientCertMode": "Required",
    "cloningInfo": null,
    "containerSize": 0,
    "customDomainVerificationId": "201F74B099FA881DB9368A26C8E8B8BB8B9AF75BF450AF717502AC151F59DBEA",
    "dailyMemoryTimeQuota": 0,
    "defaultHostName": "northpole-ssh-certs-fa.azurewebsites.net",
    "enabled": true,
    "enabledHostNames": [
      "northpole-ssh-certs-fa.azurewebsites.net"
    ],
    "extendedLocation": null,
    "hostNameSslStates": [
      {
        "certificateResourceId": null,
        "hostType": "Standard",
        "ipBasedSslResult": null,
        "ipBasedSslState": "NotConfigured",
        "name": "northpole-ssh-certs-fa.azurewebsites.net",
        "sslState": "Disabled",
        "thumbprint": null,
        "toUpdate": null,
        "toUpdateIpBasedSsl": null,
        "virtualIPv6": null,
        "virtualIp": null
      },
      {
        "certificateResourceId": null,
        "hostType": "Repository",
        "ipBasedSslResult": null,
        "ipBasedSslState": "NotConfigured",
        "name": "northpole-ssh-certs-fa.scm.azurewebsites.net",
        "sslState": "Disabled",
        "thumbprint": null,
        "toUpdate": null,
        "toUpdateIpBasedSsl": null,
        "virtualIPv6": null,
        "virtualIp": null
      }
    ],
    "hostNames": [
      "northpole-ssh-certs-fa.azurewebsites.net"
    ],
    "hostNamesDisabled": false,
    "hostingEnvironmentProfile": null,
    "httpsOnly": false,
    "hyperV": false,
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa",
    "identity": {
      "principalId": "d3be48a8-0702-407c-89af-0319780a2aea",
      "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
      "type": "SystemAssigned",
      "userAssignedIdentities": null
    },
    "inProgressOperationId": null,
    "isDefaultContainer": null,
    "isXenon": false,
    "keyVaultReferenceIdentity": "SystemAssigned",
    "kind": "functionapp,linux",
    "lastModifiedTimeUtc": "2023-11-09T14:43:01.183333",
    "location": "East US",
    "maxNumberOfWorkers": null,
    "name": "northpole-ssh-certs-fa",
    "outboundIpAddresses": "",
    "possibleOutboundIpAddresses": "",
    "publicNetworkAccess": null,
    "redundancyMode": "None",
    "repositorySiteName": "northpole-ssh-certs-fa",
    "reserved": true,
    "resourceGroup": "northpole-rg1",
    "scmSiteAlsoStopped": false,
    "siteConfig": {
      "acrUseManagedIdentityCreds": false,
      "acrUserManagedIdentityId": null,
      "alwaysOn": false,
      "antivirusScanEnabled": null,
      "apiDefinition": null,
      "apiManagementConfig": null,
      "appCommandLine": null,
      "appSettings": null,
      "autoHealEnabled": null,
      "autoHealRules": null,
      "autoSwapSlotName": null,
      "azureMonitorLogCategories": null,
      "azureStorageAccounts": null,
      "connectionStrings": null,
      "cors": null,
      "customAppPoolIdentityAdminState": null,
      "customAppPoolIdentityTenantState": null,
      "defaultDocuments": null,
      "detailedErrorLoggingEnabled": null,
      "documentRoot": null,
      "elasticWebAppScaleLimit": null,
      "experiments": null,
      "fileChangeAuditEnabled": null,
      "ftpsState": null,
      "functionAppScaleLimit": 200,
      "functionsRuntimeScaleMonitoringEnabled": null,
      "handlerMappings": null,
      "healthCheckPath": null,
      "http20Enabled": true,
      "http20ProxyFlag": null,
      "httpLoggingEnabled": null,
      "ipSecurityRestrictions": null,
      "ipSecurityRestrictionsDefaultAction": null,
      "javaContainer": null,
      "javaContainerVersion": null,
      "javaVersion": null,
      "keyVaultReferenceIdentity": null,
      "limits": null,
      "linuxFxVersion": "Python|3.11",
      "loadBalancing": null,
      "localMySqlEnabled": null,
      "logsDirectorySizeLimit": null,
      "machineKey": null,
      "managedPipelineMode": null,
      "managedServiceIdentityId": null,
      "metadata": null,
      "minTlsCipherSuite": null,
      "minTlsVersion": null,
      "minimumElasticInstanceCount": 0,
      "netFrameworkVersion": null,
      "nodeVersion": null,
      "numberOfWorkers": 1,
      "phpVersion": null,
      "powerShellVersion": null,
      "preWarmedInstanceCount": null,
      "publicNetworkAccess": null,
      "publishingPassword": null,
      "publishingUsername": null,
      "push": null,
      "pythonVersion": null,
      "remoteDebuggingEnabled": null,
      "remoteDebuggingVersion": null,
      "requestTracingEnabled": null,
      "requestTracingExpirationTime": null,
      "routingRules": null,
      "runtimeADUser": null,
      "runtimeADUserPassword": null,
      "scmIpSecurityRestrictions": null,
      "scmIpSecurityRestrictionsDefaultAction": null,
      "scmIpSecurityRestrictionsUseMain": null,
      "scmMinTlsVersion": null,
      "scmType": null,
      "push": null,
      "pythonVersion": null,
      "remoteDebuggingEnabled": null,
      "remoteDebuggingVersion": null,
      "requestTracingEnabled": null,
      "requestTracingExpirationTime": null,
      "routingRules": null,
      "runtimeADUser": null,
      "runtimeADUserPassword": null,
      "scmIpSecurityRestrictions": null,
      "scmIpSecurityRestrictionsDefaultAction": null,
      "scmIpSecurityRestrictionsUseMain": null,
      "scmMinTlsVersion": null,
      "scmType": null,
      "sitePort": null,
      "sitePrivateLinkHostEnabled": null,
      "storageType": null,
      "supportedTlsCipherSuites": null,
      "tracingOptions": null,
      "use32BitWorkerProcess": null,
      "virtualApplications": null,
      "vnetName": null,
      "vnetPrivatePortsCount": null,
      "vnetRouteAllEnabled": null,
      "webSocketsEnabled": null,
      "websiteTimeZone": null,
      "winAuthAdminState": null,
      "winAuthTenantState": null,
      "windowsConfiguredStacks": null,
      "windowsFxVersion": null,
      "xManagedServiceIdentityId": null
    },
    "slotSwapStatus": null,
    "state": "Running",
    "storageAccountRequired": false,
    "suspendedTill": null,
    "tags": {
      "create-cert-func-url-path": "/api/create-cert?code=candy-cane-twirl",
      "project": "northpole-ssh-certs"
    },
    "targetSwapSlot": null,
    "trafficManagerHostNames": null,
    "type": "Microsoft.Web/sites",
    "usageState": "Normal",
    "virtualNetworkSubnetId": null,
    "vnetContentShareEnabled": false,
    "vnetImagePullEnabled": false,
    "vnetRouteAllEnabled": false
  }
]
```

```
northpole-ssh-certs-fa.azurewebsites.net

```

https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl

```
https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDISS0p/EVbeHvbaVNZmXcsgqfvzxw/I4gqW7oNyX1An/biCmZIkgHGUmKho9NSslVyeITbAZZs8WcSoAoDSJ3biO/SlHGmkW2LkKvyWQIwXJrpYAgAhvsbdrKmJeN5TYyrXKvQqH7mukaG3ZGI+uE/Iju7Qm68Hzrkg/Z/nX+6TGgE2ZcmUb9V6ZGgEmbPN3yRqavT4lR7RPl+Fd7sF3xIK3jp+FXL8zyH7h/qNkHMSBhzZ/I51I4NFYmNx+9PTh5HbOgqdN3vRgCXLeXzTXBxUbIdswclyEYcI5OtqG8ZRdPMRpuIzUaj4z9Ln0Mcg30KCOJA556TZRcCcxPrcc/R7kpD9sWugMYMuMFKaMRyCHONsR3FHhIrGvb3Udz0/Q2idISxWVnZeLPsi78WBewYBlA4u+bDo20IC2lePi/eoV/Wn/TebLn3PV5YVLmnb3k7bujScQSG4ajy/R/oEgTkccsKXijrpstv1YylO0ycFgtfnJimDVAqM/cG2M3nszc= castr@mymac.local


{  
    "ssh_cert": "rsa-sha2-512-cert-v01@openssh.com AAAAIXJzYS1zaGEyLTUxMi1jZXJ0LXYwMUBvcGVuc3NoLmNvbQAAACcxNTAzMjMzOTUzNzc4MDUxMTUyMjYzNDAwMDgxOTI2OTY2ODg4NTkAAAADAQABAAABgQDISS0p/EVbeHvbaVNZmXcsgqfvzxw/I4gqW7oNyX1An/biCmZIkgHGUmKho9NSslVyeITbAZZs8WcSoAoDSJ3biO/SlHGmkW2LkKvyWQIwXJrpYAgAhvsbdrKmJeN5TYyrXKvQqH7mukaG3ZGI+uE/Iju7Qm68Hzrkg/Z/nX+6TGgE2ZcmUb9V6ZGgEmbPN3yRqavT4lR7RPl+Fd7sF3xIK3jp+FXL8zyH7h/qNkHMSBhzZ/I51I4NFYmNx+9PTh5HbOgqdN3vRgCXLeXzTXBxUbIdswclyEYcI5OtqG8ZRdPMRpuIzUaj4z9Ln0Mcg30KCOJA556TZRcCcxPrcc/R7kpD9sWugMYMuMFKaMRyCHONsR3FHhIrGvb3Udz0/Q2idISxWVnZeLPsi78WBewYBlA4u+bDo20IC2lePi/eoV/Wn/TebLn3PV5YVLmnb3k7bujScQSG4ajy/R/oEgTkccsKXijrpstv1YylO0ycFgtfnJimDVAqM/cG2M3nszcAAAAAAAAAAQAAAAEAAAAkNTQ1NWU2YTItNzE3ZC00NDNiLWFmMTktN2VmZmExZWE1ODJhAAAABwAAAANlbGYAAAAAZXO5ywAAAABlmKT3AAAAAAAAABIAAAAKcGVybWl0LXB0eQAAAAAAAAAAAAAAMwAAAAtzc2gtZWQyNTUxOQAAACBpNhjTApiZFzyRx0UB/fkzOAka7Kv+wS9MKfj+qwiFhwAAAFMAAAALc3NoLWVkMjU1MTkAAABA8dxSCO5O8D5VqT80YXpqFKZpSZYTxfIMcQ1fDxSNR6mQqHQDNvzEg9pZJPc6Lfdw/VK3HjbZ4A0+FVWmwouLBg== ",  
    "principal": "elf"  
}
```

```
az ssh vm -g northpole-rg2 --name NP-VM1
```