# Web Application Layout

Una aplicación web consiste en diferentes capas:

| Categoria | Descripción |
|:-----------------------------------|:-----------------------------|
| Web Application Infraestrucure    | Estructura de los componentes requeridos, servidores, bds, etc|
| Web Application Componentes       | ui/ux, client, server
| Web Application Architecture      | relaciones entre los componentes
|

## Web Application Infraestructure

Que modelo utiliza la app:

- Cliente-Server
- One Server
- Many Servers - One Database
- Many Servers - Many Databases


## Web Applcation Componentes

Cada aplicación puede tener diferente número de componentes:

1. Client
2. Server
   - Webserver
   - Web Application Logic
   - Database
3. Services (Micrservices
   - 3d Party Integrations
   - Web Application Integrations
4. Functions (Serverless)


## Web Application Architecture

Los componentes de la aplicación son divididos en capas:

- Presentation Layer
- Application Layer
- Data Layer

### **Microservicios**

Podemos pensar en los microservicios como componentes independientes de la aplicación web, los cuales son programados solo para una tarea: `Registration, Search, Payments, Ratings, Reviews`

Estos componentes se comunican con el cliente y unos con otros, la comunicación entre ellos es `stateless` es decir que las peticiones y respuestas son independientes. A esto también suele llamarsele `service oriented architecture SOA`

Pueden ser escritos en diferentes lenguajes, escalarse y desarrollarse fácilmente, algunos beneficos adicionales del los microservicios: `Agility, Flexible scaling, Easy deployment, Reusable code, Resilence`

### **Serverless**

Proveedores de nuve como `AWS, GCP, Azure, Digital Ocean` ofrecen arquitecturas `serverless`, proporcionan marcos de trabajo para el desarrollo sin tener que preocuparse por los servidores en si mismos. 

## Architecture Seurity

Entender la arquitectura al realizar Pentest es importante 

