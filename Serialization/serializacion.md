# Serlializacion

- Serialización

Convertir objetos en datastreams y almacenarlos para un uso posterior

- Des serialización

El objeto previamente serializado se deserializa para volverlo a su version original.

- Ataque

Un ataque de serialización es la inyección o modificacion de los datos en el datasteam. Cuando los datos son luego accedidos por la aplicacion, el codigo malicioso resulta en implicaciones serias.

Ocurre cuando las aplicaciones deserializan objetos de fuentes no confiables.


## Java Byte Streams
Son usados para entrada y salida de 8-bit bytes

InputStream
OutputStream

## Serializacion en Java

java.io.Serializable

## Referencias

- [Serialization and Deserialization in Java](https://www.geeksforgeeks.org/serialization-in-java/)


## Utilerias
[JexBoss](https://github.com/joaomatosf/jexboss)