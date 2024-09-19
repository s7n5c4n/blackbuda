# Proyecto de Análisis de Mercado BTC-CLP

Este proyecto contiene un conjunto de funciones en Python para analizar el mercado de Bitcoin en relación con el Peso Chileno (BTC-CLP) utilizando la API de Buda.com.

## Funcionalidades

1. **Obtener Precio Actual de BTC**: Recupera el precio actual de Bitcoin en CLP, así como las variaciones de precio en las últimas 24 horas y 7 días.
2. **Obtener Volumen de Transacciones en las Últimas 24 Horas**: Calcula el volumen total de transacciones de BTC en CLP en las últimas 24 horas.
3. **Obtener Volumen de Transacciones Hace un Año**: Recupera el volumen de transacciones de BTC en CLP de hace exactamente un año.
4. **Calcular Aumento Porcentual**: Calcula el aumento porcentual en el volumen de transacciones de BTC-CLP respecto al año anterior.
5. **Obtener Volumen de Transacciones Durante un Evento**: Calcula el volumen total de transacciones en CLP durante un evento específico.
6. **Calcular Comisión Perdida**: Calcula la comisión perdida debido a la liberación de comisiones durante un evento específico.

## Requisitos

- Python 3.x
- Biblioteca `requests`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Instala las dependencias:
    ```bash
    pip install requests
    ```

## Uso

Ejecuta el script principal para obtener los análisis del mercado BTC-CLP:
```python
import requests
from datetime import datetime, timedelta

# Definición de funciones aquí...

obtener_precio_actual_de_btc()
calcular_aumento_porcentual()
obtener_volumen_transacciones()
calcular_comision_perdida()
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
