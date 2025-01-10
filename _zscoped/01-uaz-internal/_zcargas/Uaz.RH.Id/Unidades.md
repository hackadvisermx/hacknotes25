
```


// UazRH, Version=1.0.2.46, Culture=neutral, PublicKeyToken=null
// UazRH.Id.C.Unidades
public class Unidades
{
	public class HorarioSemana
	{
		public class Dia
		{
			public const string LUNES = "Lunes";
			public const string MARTES = "Martes";
			public const string MIERCOLES = "Miercoles";
			public const string JUEVES = "Jueves";
			public const string VIERNES = "Viernes";
			public const string SABADO = "Sabado";
			public const string DOMINGO = "Domingo";
		}
	}

	public class EstatusUnidad
	{
		public const int BASE = 1;
		public const int TIEMPO_DETERMINADO = 2;
		public const int HONORARIOS = 3;
		public const int LIBERADA = 4;
	}

	public class TipoSolicitudHonorario
	{
		public const int HONORARIOS_ORDINARIOS = 1;
		public const int PERSONAL_ACTIVIDAD_DOCENTE = 2;
	}

	public class TipoActividad
	{
		public const int HORAS_FRENTE_A_GRUPO = 1;
		public const int OTROS = 2;
	}

	public class EstatusSolicitudHonorario
	{
		public const int CREADA = 1;
		public const int CONFIGURADA = 2;
		public const int REVISION_PENDIENTE = 3;
		public const int APROBADA = 4;
		public const int NOMINA_CONFIGURADA = 5;
		public const int PAGADA = 6;
		public const int RECHAZADA = 7;
		public const int CANCELADA = 8;
	}

	public class TipoPagoHonorario
	{
		public const int CONTINUO = 1;
		public const int UNICO = 2;
	}
}
```