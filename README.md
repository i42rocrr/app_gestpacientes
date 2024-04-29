# Contenedores de aplicaciones potenciadas con lenguajes de programación invitados:
### Módulo "app_pacientes"
***

### Rafael Rojas Crespo
#####  Junio/2024

***
## Tabla de contenidos
1. [Información general](#info-general)
2. [app_gestpacientes](#app_gestpacientes)
3. [Tecnologías](#tecnologías)
4. [Instalación](#instalación)


## Información general
***
Este trabajo forma parte de un Trabajo Fin de Grado desarrollado para la obtención del título de Grado en Ingeniería informática, especialidad Computación.
Se trata de un proyecto en el que se muestra cómo se trabaja con los lenguajes Java y Python dentro de un mismo proyecto.
El ejemplo que se ha diseñado puede verse en su totalidad como un sistema de información que emula cómo interactuarían varias empresas 
para obtener información estratégica de cara al crecimiento de sus negocios, siendo la información el eje principal que daría sentido a un caso de uso
que podría darse en un entorno real.
El sistema desarrollado es un conjunto de contenedores que contendrían los subsistemas software virtualizados y que forman una red tipo C entre ellos.
Este subsistema tendría por ip la 192.168.0.5.
Realiza una conexión a un servidor de base de datos de MySQL cuya IP es 192.168.0.4.

## app_gestpacientes
***
Es el nombre que se le da a este módulo, que forma parte de un sistema de información más global.
Se encarga de recopilar datos de pacientes que toman algún tipo de medicación,
anotando en una base de datos tanto sus datos personales como los medicamentos que toma.
El sistema ofrece un servicio de predicción en el que, a partir de una serie de datos que indica
el propio usuario (paciente) se le informa, mediante algoritmos de Machine Learning,
el grado de riesgo que tiene de que se le reproduzca un tumor mamario.

## Tecnologías usadas
***
* [Spring Boot](https://example.com): Versión 3.2.5
* [Java+GraalVM](https://www.graalvm.org/): Versión 21.0.2+13.1
* [Maven](https://maven.apache.org/): Versión 3.8.8
* [Docker](https://www.docker.com/): Versión 4.29.0
* [Python](https://www.python.org/) Versión 3.12.1
* [Thymeleaf](www.thymeleaf.org): Versión 2.34
* [MySQL](https://www.mysql.com/): Versión 8.0.36


## Instalación
***
```
$ git clone https://github.com/i42rocrr/app_gestpacientes.git
$ cd app_gestpacientes
$ doker-compose up

$ http://localhost:8085
```
 
