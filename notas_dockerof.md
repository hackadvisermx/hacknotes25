
--------------------------------------------------------------------------------------------------

Video Youtube:
https://www.youtube.com/watch?v=pk9cxR27mGg


Repositorio:
https://github.com/aaaguirrep/offensive-docker/


Otras referencias:
https://blog.ropnop.com/docker-for-pentesters/
https://www.youtube.com/watch?v=IJUU6BdC1b4
https://github.com/l34r00t
https://www.youtube.com/watch?v=2OmPFhveRQ4



--------------------------------------------------------------------------------------------------
>>> En mi MAC
--------------------------------------------------------------------------------------------------

brew install terraform
https://www.terraform.io/

brew install ansible



--------------------------------------------------------------------------------------------------
>>> Definiciones de las tools
--------------------------------------------------------------------------------------------------



~ Configurar el git inicial

git config --global user.email "hackadviser@gmail.com"



~ Construir la imagen del docker-ofensivo

docker build -t docker-ofensivo .



~ Como ejecutar el docker ofesivo

. Escenario 1

docker run --rm -it --name dockerataque1 docker-ofensivo /bin/zsh


. Escenario 2 / soporte para vpn

docker run --rm -it --name ofensivovpn --cap-add=NET_ADMIN --device=/dev/net/tun --sysctl net.ipv6.conf.all.disable_ipv6=0  -v /Users/castr/hack/ofensivo:/ofensivo docker-ofensivo /bin/zsh






~ Instalar go

https://golang.org/dl/

https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz

https://golang.org/dl/go1.15.5.linux-amd64.tar.gz


796076 

~ Crear shorcutos 

RUN echo "alias vpnhtb=\"openvpn /offensive/path/to/ovpn/file\"" >> /root/.zshrc





>>> Sobre Oh My Zsh > https://ohmyz.sh/



~ Instalar ohmyzsh y plugins

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
git clone --depth 1 https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions 
git clone --depth 1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting 
git clone --depth 1 https://github.com/zsh-users/zsh-history-substring-search ~/.oh-my-zsh/custom/plugins/zsh-history-substring-search 
sudo chmod -R 755 /usr/local/share/zsh
sudo chmod -R 755 /usr/local/share/zsh/site-functions

~ Configurar .zshrc

---------------------------------------------------------------------------------------------------
plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search)

export LC_CTYPE="C.UTF-8"
export LC_ALL="C.UTF-8"
export LANG="C.UTF-8"
export LANGUAGE="C.UTF-8"

alias ofensivoBuild="docker build -t docker-ofensivo ."
alias ofensivoUp="docker run --rm -it --name ofensivo docker-ofensivo /bin/zsh"
alias ofensivoVPN="docker run --rm -it --name ofensivovpn --cap-add=NET_ADMIN --device=/dev/net/tun --sysctl net.ipv6.conf.all.disable_ipv6=0  -v /Users/castr/hack/ofensivo:/ofensivo docker-ofensivo /bin/zsh"plug
---------------------------------------------------------------------------------------------------



>> subversion

~ descargar archivos de github con subversion
svn ls https://github.com/daviddias/node-dirbuster
svn checkout https://github.com/daviddias/node-dirbuster/trunk/lists/



>> cmd linux
forfiles /P directory /S /D +08/01/2013
forfiles /P . /S /D +11/1/2020 /M *.doc


~ share desde el contenedor

 docker run --rm -it -p 445:445 -v "${PWD}:/tmp/serve" docker-ofensivo smbserver.py -smb2support share /tmp/serve


~ desde mac

smbutil view -G //localhost
Password for localhost: 
Share                                           Type    Comments
-------------------------------
SHARE                                           Disk    
IPC$   


mount_smbfs //tmp:tmp@localhost/share /Users/castr/tmp
umount /Users/castr/Downloads/tmp


>> Docker

docker system prune
docker ps --size


~ Borrar todas las imagenes
docker rmi -f $(docker images -a -q)




--------------------------------------------------------------------------------------------------
Terraform en Google
--------------------------------------------------------------------------------------------------


https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform





















