
#Virtualizacion


## Aislameinto / Sandbox

. Aislamiento de disco
. Aislamiento de memoria RAM
. Aislamiento de red



>> Hypervisores



> Tipo 1 > Baremetal: interactua directamente con el hardware


. se peuden ejecutar directamente en el hardware

xen project: 
	https://xenproject.org/

usado por:
	https://www.qubes-os.org/
	aws para toda la nuve



> Tipo 2 > Hosteados: los de abajo deben ser de la misma arquitectura

kvm 
Microsoft hyper V





>> Contenedores 

Gestores de contenedores
. SystemD-Nspawn
. Podman
. Docker
. LXC
. RunC


Gestor Docker

docker ui > docker enginie > cotainerd > RunC

docker search fedora
docker pull fedora



>> Kubernates (K8s)

Administra contenedores en forma de red

. Master
. Workers


Pod -> Conjunto de contairnes


- KubeAdm
 Crear y amdministr cluster 

- Calico
  Administra la comunicacion entre master y workers



Implementaciones de kubernates

Red OpenShift > https://www.openshift.com/
okd > https://www.okd.io/

rancher > https://rancher.com/open
