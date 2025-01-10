# DevGuru


## Directorios
- October CMS

http://10.10.118.196/backend/backend/auth/signin

- Gitea

http://10.10.186.74:8585/frank

frank

- Git repo

http://10.10.186.74/.git/config

- Descargar repo 
```
 git clone https://github.com/lijiejie/GitHack
 python GitHack.py http://10.10.186.74/.git/
```
- Existe vulnerabilidad en Gitea, pero requiere repo publico

https://www.exploit-db.com/exploits/44996

El problema que no hay repos pubicos y esta deshabiliado el registro de usuarios

## Hallazgos

'mysql' => [
            'driver'     => 'mysql',
            'engine'     => 'InnoDB',
            'host'       => 'localhost',
            'port'       => 3306,
            'database'   => 'octoberdb',
            'username'   => 'october',
            'password'   => 'SQ66EBYx4GT3byXH',
            'charset'    => 'utf8mb4',
            'collation'  => 'utf8mb4_unicode_ci',
            'prefix'     => '',
            'varcharmax' => 191,

