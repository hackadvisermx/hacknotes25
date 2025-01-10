 
```
// UazRH.MainForm  
using System.ComponentModel;  
using System.Windows.Forms;  
using DevExpress.XtraBars.Docking2010;  
using DevExpress.XtraBars.Docking2010.Views.Tabbed;  
using DevExpress.XtraBars.Navigation;  
using DevExpress.XtraEditors;  
using DevExpress.XtraGrid.Columns;  
using DevExpress.XtraGrid.Views.Grid;  
using UazRH.ABC.Config.ControlAcceso.Usuarios;  
using UazRH.ABC.Config.Nomina.ConcesionesPension;  
using UazRH.ABC.Config.Nomina.ConfiguracionNomina;  
using UazRH.ABC.Config.Nomina.CuentasPagadoras;  
using UazRH.ABC.Config.Nomina.ProyeccionEmpleadoAdm;  
using UazRH.ABC.Config.TarifasViaticos;  
using UazRH.ABC.Config.TarifasViaticosDocente;  
using UazRH.ABC.Config.Unidades.CargaAcademica;  
using UazRH.ABC.Config.Unidades.CargaAcademica.PlanEstudios;  
using UazRH.ABC.Nomina.Autorizar;  
using UazRH.ABC.Nomina.CalendariooNoLaboral;  
using UazRH.ABC.Nomina.ConsultarMovimientos;  
using UazRH.ABC.Nomina.Dispersion;  
using UazRH.ABC.Nomina.GestionBitacora;  
using UazRH.ABC.Nomina.ImpresionesNomina;  
using UazRH.ABC.Nomina.IsssteConsultaEmpleado;  
using UazRH.ABC.Nomina.MovimientoNomina;  
using UazRH.ABC.Nomina.Pago;  
using UazRH.ABC.Nomina.Pensionados;  
using UazRH.ABC.Nomina.PensionesAlimenticias;  
using UazRH.ABC.Nomina.PolizaFondeo;  
using UazRH.ABC.Nomina.Producto;  
using UazRH.ABC.Nomina.ProductoEspecial;  
using UazRH.ABC.Nomina.SubsidioEmpleado;  
using UazRH.ABC.Nomina.TarifaRetencion;  
using UazRH.ABC.Personal.AntiguedadISSSTE;  
using UazRH.ABC.Personal.BandejaHonorarioOrdinario;  
using UazRH.ABC.Personal.BandejaIncidencias;  
using UazRH.ABC.Personal.Beneficiarios;  
using UazRH.ABC.Personal.CancelarCargasTD;  
using UazRH.ABC.Personal.CargaLaboral.Administracion.Administrativos;  
using UazRH.ABC.Personal.CargaLaboral.Administracion.Docentes.CrearPlaza;  
using UazRH.ABC.Personal.CargaLaboral.Administracion.FuncConfObraDet;  
using UazRH.ABC.Personal.CargaLaboral.Administracion.MovimientosSinRestricciones;  
using UazRH.ABC.Personal.CargaUnidadEmpleado.RevisionCargaLaboralUnidad;  
using UazRH.ABC.Personal.CodigoAutorizacion;  
using UazRH.ABC.Personal.Constancias;  
using UazRH.ABC.Personal.Defunciones;  
using UazRH.ABC.Personal.Empleados;  
using UazRH.ABC.Personal.Empleados.Persona;  
using UazRH.ABC.Personal.FuncionAsignada.AsignarTiempoDeterminadoUnidad;  
using UazRH.ABC.Personal.Honorario.OrdenesPago;  
using UazRH.ABC.Personal.Honorario.Unidades;  
using UazRH.ABC.Personal.Honorarios;  
using UazRH.ABC.Personal.Jubilados;  
using UazRH.ABC.Personal.Jubilados.Admi;  
using UazRH.ABC.Personal.Madres;  
using UazRH.ABC.Personal.MovimientoEmpleado.AplicarSuplencias;  
using UazRH.ABC.Personal.PersonalApoyo;  
using UazRH.ABC.Personal.PersonalTiempoDeterminado;  
using UazRH.ABC.Personal.ProyecctosInvestigacion;  
using UazRH.ABC.Personal.Reincorporacion;  
using UazRH.ABC.Personal.ReportesCoordinacionPersonal;  
using UazRH.ABC.Personal.Suplencias;  
using UazRH.ABC.Personal.Viaticos;  
using UazRH.ABC.Personal.ViaticosDocente;  
using UazRH.ABC.Sindicato.AsignacionEventual;  
using UazRH.ABC.Sindicato.BandejaIncidencia;  
using UazRH.ABC.Sindicato.BandejaSolicitudesEventual;  
using UazRH.ABC.Sindicato.Propuesta_Sindical;  
using UazRH.ABC.Sindicato.Propuesta_Sindical.Sindicato;  
using UazRH.ABC.Sindicato.Propuesta_Sindical.Unidad;  
using UazRH.ABC.Sindicato.Solicitud.RegistroSolicitud;  
using UazRH.ABC.Sindicato.TiempoDeterminado;  
using UazRH.ABC.Unidades.Honorarios.Creacion;  
using UazRH.ABC.Unidades.HorariosInvestigacionPNPC;  
using UazRH.ABC.Unidades.ImpresionCargaUnidades;  
using UazRH.ABC.Unidades.SolicitudesEventuales;  
using UazRH.ABC.Unidades.UnidadLiberada;  
using UazRH.Core.UI;  
using UazRH.Win.Core.API.Config.ControlAcceso.Usuarios;  
  
private Usuario usuarioSession;
```

```
[DataMember(Name = "url")]  
private string urlApiRh = "http://10.1.205.9:8080/uaz-rh";  
[DataMember(Name = "urlNomina")]  
private string urlApiNomina = "http://10.1.205.9:8081/nomina";  
[DataMember(Name = "urlApiReportes")]  
private string urlApiReportes = "http://10.1.205.9:8083/reportes/";
```

```
wget http://10.1.205.9/uaz-rh/downloads/test/uaz-rh_win_1.0.0.0_patch.zip

http://10.1.205.9/uaz-rh/downloads/test/
```


