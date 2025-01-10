
```
path = "/config/nomina/nivel/


http://10.1.205.9:8080/uaz-rh/config/nomina/nivel/listaNiveles


```



```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Core.API.Nomina.Nivel.NivelRest
using System.Collections.Generic;
using System.Threading.Tasks;
using Exodo.SAL.Util;
using UazRH.Core.API.Nomina.Categoria;
using UazRH.Core.API.Nomina.Nivel;

public class NivelRest : ApiRestHttpClient
{
	private string path = "/config/nomina/nivel/";

	public async Task<List<Nivel>> ListaNiveles()
	{
		return await GetAsync<List<Nivel>>(path + "listaNiveles");
	}

	public async Task<List<Nivel>> obtenerParaEventuales()
	{
		return await GetAsync<List<Nivel>>(path + "obtenerParaEventuales");
	}

	public async Task<List<Nivel>> ListaNivelesPorGrupoLaboral(int? idGrupoLaboral)
	{
		NivelRest nivelRest = this;
		string text = path;
		int? num = idGrupoLaboral;
		return await nivelRest.GetAsync<List<Nivel>>(text + "listaNivelesPorGrupoLaboral/" + num);
	}

	public async Task<List<Nivel>> obtenerParaAsignacionCategoria(BuscarCategoria request)
	{
		return await PostAsync<List<Nivel>>(path + "obtenerParaAsignacionCategoria", request);
	}

	public async Task<List<Nivel>> porGrupoLaboralParaMovimientos(int? idGrupoLaboral)
	{
		return await GetAsync<List<Nivel>>($"{path}porGrupoLaboralParaMovimientos/{idGrupoLaboral}");
	}
}

```