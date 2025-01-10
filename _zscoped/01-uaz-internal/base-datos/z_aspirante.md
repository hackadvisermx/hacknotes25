
```
SELECT as_clave, as_curp FROM aspirante

SELECT as_curp, as_apaterno, as_amaterno, as_nombre, as_tipo_sangre FROM aspirante WHERE as_clave = $P{as_clave}

```

```
as_apaterno                                                                      
as_amaterno
as_nombre                                                                                                                                   as_sexo as_estadocivil as_fecha_nacimiento
as_lugar_nacimiento
as_domicilio_calle
as_domicilio_colonia
as_domicilio_cp      as_trabaja as_status as_curp                                                                  as_pago as_recibo   as_clave              as_matricula
numfuncion               
numunidad
as_observacion
as_domi_ed_clave 
as_domi_pa_clave as_domi_mu_clave as_naci_pa_clave as_naci_ed_clave as_naci_mu_clave as_telefono
as_usuario                                                               
as_fecha_mod        
as_tipo_sangre                                   
ficha_impresion 
fecha_impresion
as_programa             
ci_clave                         as_fecha_registro   as_enuaz as_ceneval
        as_email


        as_discapacidad
        as_tipo_discapacidad

        as_hijo_migrantes as_pertenece_comunidad_indigena
        as_comunidad_indigena
```

```
549627 SAGP930217HZSMML09
549628 OEMY930111MZSRRS09
549629 ZAMS930702MZSVRN02
549630 MAHH900518MGRYRL08
549631 SASD930613HZSNNG04
549632 PAHA930226MZSLRN01
549633 GOAR951211HZSNCM02
549634 PAPB921209MZSLDR01
549635 BABG960419MZSRRD04
549636 UIHI920224HZSRRS03
549637 MAAO960328HZSRLS07
549638 COPD831115MDGRXL07
```


```
 SELECT as_clave, as_fecha_registro, as_email, ci_clave FROM aspirante WHERE ci_clave = '1819SNON'
```