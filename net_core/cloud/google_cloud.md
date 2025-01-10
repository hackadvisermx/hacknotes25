
# Nube de Google Cloud

Referencias: 
https://cloud.google.com/sdk/gcloud/reference/

## Consola de gcloud

### **Loguerase en el cliente de consola**
~~~
gcloud auth login
~~~
### **Listar poryectos**
~~~
gcloud projects list
PROJECT_ID         NAME        PROJECT_NUMBER
pentesting-296602  Pentesting  295003610107
~~~
~~~
gcloud projects describe pentesting-296602
createTime: '2020-11-24T02:39:19.485Z'
lifecycleState: ACTIVE
name: Pentesting
projectId: pentesting-296602
projectNumber: '295003610107'
~~~
~~~
auth list
   Credentialed Accounts
ACTIVE  ACCOUNT
* chcramirez@gmail.com

To set the active account, run:
    $ gcloud config set account `ACCOUNT`
~~~

-------------------------------------------------------
Terraform
-------------------------------------------------------
- crear llaves ssh
- habiliar Compute Engine API


terraform init
terraform apply -auto-aprove





