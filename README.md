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
│   │   ├── get_analitica.py
│   │   ├── create_reporte.py
│   │   └── ping.py
│   ├── errors
│   │   ├── errors.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   └── models
│       ├── __init__.py
│       └── incidente.py
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
    "id": "ed140dbe-06d8-45dc-b5fc-4eb46606fc47",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "idNumber": "123456789",
    "phoneNumber": "321567890",
    "plan": "EMPRENDEDOR_PLUS",
    "rol": "CLIENTE",
    "company": "uniandes"

}
```
</td>
</tr>
</td>
<td> Respuesta </td>
<td>
Informacion 

```json
{
    "company": "uniandes",
    "email": "john.doe@example.com",
    "id": "ed140dbe-06d8-45dc-b5fc-4eb46606fc47",
    "id_number": "123456789",
    "name": "John Doe",
    "phoneNumber": "321567890",
    "plan": "EMPRENDEDOR_PLUS",
    "rol": "client"
}
```
</td>
<tr>

</table>

### 2. Obtener la infromacion de un cliente
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
    "email": "john.doe@example.com",
    "id": "b030dabc-ff9e-4cbb-8d0b-974a68f297da"
}
```
</td>
<tr>

</table>

### 3. Actualización de plan de clientes

Actualiza el plan de un cliente con los datos brindados.

<table>
<tr>
<td> Método </td>
<td> PUT </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/clients/update_client_plan</strong> </td>
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
  "email": "john.doe@example.com",
  "plan": "EMPRENDEDOR"
}
```
</td>
</tr>
</table>



### 4. Consulta de salud del servicio

Usado para verificar el estado del servicio.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/clients/ping</strong> </td>
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

### 5. Limpiar la base de datos

Limpia la base de datos de clientes.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/clients/clear_database</strong> </td>
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