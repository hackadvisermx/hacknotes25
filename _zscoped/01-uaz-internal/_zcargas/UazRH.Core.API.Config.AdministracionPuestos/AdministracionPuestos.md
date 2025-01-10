
```

http://10.1.205.9:8080/uaz-rh/config/administracion_puesto/obtenerlistapuestos
http://10.1.205.9:8080/uaz-rh/config/administracion_puesto/obtenerPorId/1


```


```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Core.API.Config.AdministracionPuestos.AdministracionPuestoRest
using System.Collections.Generic;
using System.Threading.Tasks;
using Exodo.SAL.Util;
using UazRH.Core.API.Config.AdministracionPuestos;

public class AdministracionPuestoRest : ApiRestHttpClient
{
	public async Task<List<Puestos>> listaPuestos()
	{
		return await GetAsync<List<Puestos>>("config/administracion_puesto//obtenerlistapuestos");
	}

	public async Task<Puestos> obtenerPorId(int? id)
	{
		AdministracionPuestoRest administracionPuestoRest = this;
		int? num = id;
		return await administracionPuestoRest.GetAsync<Puestos>("config/administracion_puesto/obtenerPorId/" + num);
	}

	public async Task<int> GuardarPuesto(Puestos request)
	{
		return await PostAsync<int>("config/administracion_puesto/guardarPuesto", request);
	}
}

```

```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Core.API.Config.AdministracionPuestos.Puestos
using System.Runtime.Serialization;

[DataContract]
public class Puestos
{
	[DataMember(Name = "idPuesto")]
	public int? IdPuesto { get; set; }

	[DataMember(Name = "puesto")]
	public string Puesto { get; set; }

	[DataMember(Name = "activo")]
	public bool Activo { get; set; }
}

```