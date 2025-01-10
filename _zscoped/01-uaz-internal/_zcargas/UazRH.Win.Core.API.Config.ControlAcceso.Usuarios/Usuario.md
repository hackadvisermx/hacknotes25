```
http://10.1.205.9:8080/uaz-rh/config/controlAcceso/usuarios/obtenerusuarios
http://10.1.205.9:8080/uaz-rh/config/controlAcceso/usuarios/usuarioActivos

http://10.1.205.9:8080/uaz-rh/config/controlAcceso/usuarios/50
http://10.1.205.9:8080/uaz-rh/config/controlAcceso/usuarios/actualizarPassword/50/hola


post

editarUsuario

```


```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Win.Core.API.Config.ControlAcceso.Usuarios.UsuarioRest
using System.Collections.Generic;
using System.Threading.Tasks;
using Exodo.SAL.Util;
using UazRH.Win.Core.API.Config.ControlAcceso.Usuarios;

public class UsuarioRest : ApiRestHttpClient
{
	private string url = "/config/controlAcceso/usuarios/";

	public async Task<List<Usuario>> listaEmpleados()
	{
		return await GetAsync<List<Usuario>>(url + "obtenerusuarios");
	}

	public async Task<List<Usuario>> listaEmpleadosActivos()
	{
		return await GetAsync<List<Usuario>>(url + "usuarioActivos");
	}

	public async Task<bool> cambiarContraseña(int? idUsuario, string newPassword)
	{
		UsuarioRest usuarioRest = this;
		string[] obj = new string[5] { url, "actualizarPassword/", null, null, null };
		int? num = idUsuario;
		obj[2] = num.ToString();
		obj[3] = "/";
		obj[4] = newPassword;
		return await usuarioRest.GetAsync<bool>(string.Concat(obj));
	}

	public async Task<Usuario> usuarioPorId(int? idUsuario)
	{
		UsuarioRest usuarioRest = this;
		string text = url;
		int? num = idUsuario;
		return await usuarioRest.GetAsync<Usuario>(text + num);
	}

	public async Task<Usuario> guardarUsuario(Usuario usuario)
	{
		return await PostAsync<Usuario>(url + "guardarUsuario", usuario);
	}

	public async Task<Usuario> editarUsuario(Usuario usuario)
	{
		return await PostAsync<Usuario>(url + "editarUsuario", usuario);
	}

	public async Task<bool> UsuarioHonorarioValidar(int? idUsuario)
	{
		UsuarioRest usuarioRest = this;
		string text = url;
		int? num = idUsuario;
		return await usuarioRest.GetAsync<bool>(text + "usuarioHonorarioValidar/" + num);
	}

	public async Task<bool> cambiarContraseñaPrimeraVez(CambiarClaveRequest request)
	{
		return await PostAsync<bool>(url + "cambiarContraseñaPrimeraVez", request);
	}
}

```

```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Win.Core.API.Config.ControlAcceso.Usuarios.Usuario
using System;
using System.Runtime.Serialization;

[DataContract]
public class Usuario
{
	[DataMember(Name = "idUsuario")]
	public int? IdUsuario { get; set; }

	[DataMember(Name = "userName")]
	public string UserName { get; set; }

	[DataMember(Name = "password")]
	public string Password { get; set; }

	[DataMember(Name = "idEmpleado")]
	public int? idEmpleado { get; set; }

	[DataMember(Name = "fechaCreacion")]
	public DateTime? FechaCreacion { get; set; }

	[DataMember(Name = "estatus")]
	public string Estatus { get; set; }

	[DataMember(Name = "puesto")]
	public string Puesto { get; set; }

	[DataMember(Name = "idPuesto")]
	public int? IdPuesto { get; set; }

	[DataMember(Name = "email")]
	public string Email { get; set; }

	[DataMember(Name = "idArea")]
	public int? IdArea { get; set; }

	[DataMember(Name = "nombreArea")]
	public string NombreArea { get; set; }

	[DataMember(Name = "esAdministrador")]
	public bool? esAdministrador { get; set; }

	[DataMember(Name = "primerIngreso")]
	public bool? PrimerIngreso { get; set; }

	[DataMember(Name = "nombre")]
	public string Nombre { get; set; }

	[DataMember(Name = "matricula")]
	public string Matricula { get; set; }

	[DataMember(Name = "idUnidad")]
	public int? IdUnidad { get; set; }

	[DataMember(Name = "nombreUnidad")]
	public string NombreUnidad { get; set; }

	[DataMember(Name = "idAccion")]
	public int? IdAccion { get; set; }

	[DataMember(Name = "accion")]
	public string Accion { get; set; }

	[DataMember(Name = "asignado")]
	public bool? Asignado { get; set; }

	[DataMember(Name = "ambiente")]
	public string Ambiente { get; set; }

	[DataMember(Name = "idUsuarioPermiso")]
	public int? IdUsuarioPermiso { get; set; }

	[DataMember(Name = "grupo")]
	public string Grupo { get; set; }

	[DataMember(Name = "idGrupo")]
	public int? IdGrupo { get; set; }

	[DataMember(Name = "estatusMostrar")]
	public string EstatusMostrar { get; set; }

	[DataMember(Name = "permisoHonorario")]
	public bool? PermisoHonorario { get; set; }

	[DataMember(Name = "rfc")]
	public string Rfc { get; set; }
}

```