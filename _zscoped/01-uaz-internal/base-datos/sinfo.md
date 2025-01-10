```
SELECT DISTINCT    materia_plan.mt_clave, materia_plan.pl_clave, materia.mt_desclarga, materia.mt_clave AS Expr1
FROM         materia_plan INNER JOIN
                      materia ON materia_plan.mt_clave = materia.mt_clave
WHERE     (materia_plan.pl_clave = '175IC2')

148.217.18.12
produsr_aa
%©¤Ñ™€atƒ²µ˜~†


select ps_rfcbien,ps_curp,ps_apaterno,ps_amaterno,ps_nombre,cd.ca_clave,nc.nc_desc ,nomunidad
from carga_docentes cd,personal p, categoria c,nomcat nc,unidad u
where 
c.ca_clave =cd.ca_clave and c.gl_clave =cd.gl_clave and p.ps_rfc = cd.ps_rfc and
cd.gl_clave ='F' and cd.cd_status =2 and cd.cd_revisada =3
and nc.nc_clave = c.nc_clave and nc.gl_clave =c.gl_clave and cd.numunidad = u.numunidad
order by ps_apaterno,ps_amaterno,ps_nombre

--select * from nomcat

select ps_apaterno,ps_amaterno,ps_nombre,PS_CURP from personal 
where ps_apaterno ='MARQUEZ'
order by ps_apaterno,ps_amaterno,ps_nombre

select * from carga_docentes
where numunidad = '23201' and ci_clave='0809SNON'
order by ps_rfc

select ps_claved, ps_rfcbien, ps_curp, pu_fechaingreso, ps_fecha_nacimiento, ps_apaterno, 
ps_amaterno, ps_nombre,* 
from personal
where ps_apaterno like 'cast%'
order by ps_apaterno


```