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
│   ├── commands
│   │   ├── base_command.py
│   │   ├── get_analitics.py
│   │   └── ping.py
│   ├── errors
│   │   ├── errors.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
│   
└── tests
    ├── __init__.py
    └── test_create_reporte.py
```


## Uso

### 1. Reporte Gráfico de Análitica

Consolida y cálcula los datos que se mostraran en la interfaz gráficando los resultados

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/analitica/reporte</strong> </td>
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
<td>

```json
{
    

}
```
</td>
</tr>
</td>
<td> Respuesta </td>
<td>
Reporte de Incidentes 

```json
{
    
}
```
</td>
<tr>

</table>

### 2. Obtener la infromacion de los incidentes
Obtiene un cliente a partir del id.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/clients/get_client</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> <strong>idCliente</strong></td>
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

### 4. Limpiar la base de datos

Limpia la base de datos de clientes.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/incidents/clear_database</strong> </td>
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
<td>N/A</td>
</tr>
</td>
<td> Respuesta </td>
<td>

```json
{
    "message": "Database cleared successfully"
}
```
</td>
<tr>

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