# Entrega final Grupo de trabajo Backend Python

Jhonnatan Leoanrdo Daza Ibarra - 20162020011

## Modelos
### Pensum
Es el modulo principal de Django

### Carreras
Es la aplicacion correspondiente al modelo de las materias.

El modelo esta fromado por:
* codigo_carrera (PK)
* nombre_carrera
* total_creditos

Para el codigo de la carrera este se maneja con 3 digitos (020, 025, 015)

### Materias
Es la aplicación correspondiente al modelo de las materias.
El modelo esta formado por:
* codigo_materia (PK)
* nombre_materia
* creditos
* semestre
* horas_cl
* horas_au
* codigo_carrera (FK)

Para el codigo de la asignatura, este se maneja con tres digitos, si el codigo es de solo dos digitos se agrega un '0' al inicio.

## Syllabus
Dentro de la carpeta de src/syllabus, estan los sillabus de materias correspondientes a ingenieira de sistemas, ingenieria catastral e ingenieria industrial
