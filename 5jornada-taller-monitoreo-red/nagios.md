
## Instalar nagios en ubunto

- https://support.nagios.com/kb/article/nagios-core-installing-nagios-core-from-source-96.html#Ubuntu
```
sudo apt-get update  
sudo apt-get install -y autoconf gcc libc6 make wget unzip apache2 php libapache2-mod-php7.4 libgd-dev

sudo apt-get install openssl libssl-dev
```

```
cd /tmp/nagioscore-nagios-4.4.14/  
sudo ./configure --with-httpd-conf=/etc/apache2/sites-enabled  
sudo make all

sudo make install-groups-users
sudo usermod -a -G nagios www-data

sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

sudo service apache start



cd nagios-plugins-2.3.3
./configure --with-nagios-user=nagios --with-nagios-group=nagios
make all
make install


systemctl start nagios.service
systemctl status nagios.service

systemctl enable nagios.service

systemctl enable apache2
 

```

## Habilitar cgi en apache2 ubuntu
```
sudo a2enmod cgid 
systemctl restart apache2
```


## Instalar mariadb en Ubuntu

- https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04
