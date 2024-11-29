# Servicio de Analitica

Este microservicio permite la consulta y cálculo de datos de los 
incidentes para la analítica

## Índice

1. [Estructura](#estructura)
2. [Ejecución](#ejecución)
3. [Uso](#uso)
4. [Pruebas](#pruebas)
5. [Autor](#autor)

## Estructura

```plaintext
.
├── Dockerfile
├── Pipfile
├── README.md
├── src
│   ├── blueprints
│   │   ├── __init__.py
│   │   └── services.py
│   ├── clients
│   │   ├── manage_client.py
│   │   └── manage_incident.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── base_command.py
│   │   ├── get_incidents.py
│   │   ├── get_user.py
│   │   └── ping.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── errors.py
│   ├── __init__.py
│   └── main.py
└── tests
│   ├── blueprints
│   │   ├── test_incidents.py
│   │   └── test_ping.py
│   │   └── test_user.py
│   ├── commands
│   │   ├── test_create_user.py
│   │   ├── test_get_incidents.py
│   │   ├── test_get_user.py
│   │   ├── test_ping_command.py

```


## Uso

### 1. Reporte Gráfico de Análitica

Consolida y cálcula los datos que se mostraran en la interfaz gráficando los resultados

### Obtener la infromacion de los incidentes
Obtiene un cliente a partir del id.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/analitica/get_incidents/<company> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> <strong>company</strong></td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>
N/A
</td>
</tr>
</td>
<td> Respuesta </td>
<td>

```json
{
    
}
```
</td>
<tr>

</table>

### 3. Consulta de salud del servicio

Usado para verificar el estado del servicio analítica.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/analitica/ping</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>



## Pruebas

Para correr las pruebas del proyecto ejecutar los siguientes comandos: 

```bash
pipenv shell
```
```bash
pipenv run pytest --cov=src -v -s --cov-fail-under=70
```

## Autor

Alvaro Arlex Pérez Moncada
