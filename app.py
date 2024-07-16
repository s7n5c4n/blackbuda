import requests
from datetime import datetime, timedelta

market_id = 'btc-clp'
url_price = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'

response_price = requests.get(url_price)
data_price = response_price.json()

def obtener_precio_actual_de_btc():
    url = 'https://www.buda.com/api/v2/tickers'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for ticker in data['tickers']:
            if ticker['market_id'] == 'BTC-CLP':
                last_price_clp = float(ticker['last_price'][0])
                price_variation_24h = float(ticker['price_variation_24h'])
                price_variation_7d = float(ticker['price_variation_7d'])
                break
        
        # Imprimir los resultados
        print(f"Último precio de BTC en CLP: {last_price_clp} CLP")
        print(f"Variación de precio en las últimas 24 horas: {price_variation_24h}")
        print(f"Variación de precio en los últimos 7 días: {price_variation_7d}")
    else:
        print(f"Error al obtener datos del endpoint. Código de estado: {response.status_code}")

def obtener_volumen_transacciones_24h():
    market_id = 'btc-clp'
    url_volume = f'https://www.buda.com/api/v2/markets/{market_id}/volume'
    response_volume = requests.get(url_volume)
    data_volume = response_volume.json()
    
    if 'volume' in data_volume:
        volume_data = data_volume['volume']
        
        ask_volume_24h = float(volume_data['ask_volume_24h'][0])
        bid_volume_24h = float(volume_data['bid_volume_24h'][0])
        
        volume_btc_24h = ask_volume_24h + bid_volume_24h
        
        return volume_btc_24h
    else:
        print("Error: Volume data not found in API response.")
        return None

def obtener_volumen_transacciones_hace_un_ano():
    fecha_hace_un_ano = datetime.now() - timedelta(days=365)
    fecha_hace_un_ano_str = fecha_hace_un_ano.strftime("%Y-%m-%d")
    
    market_id = 'btc-clp'
    url_volume = f'https://www.buda.com/api/v2/markets/{market_id}/volume?date={fecha_hace_un_ano_str}'
    response_volume = requests.get(url_volume)
    data_volume = response_volume.json()
    
    if 'volume' in data_volume:
        volume_data = data_volume['volume']
        
        ask_volume_24h = float(volume_data['ask_volume_24h'][0])
        bid_volume_24h = float(volume_data['bid_volume_24h'][0])
        
        volume_btc_24h = ask_volume_24h + bid_volume_24h
        
        return volume_btc_24h
    else:
        print(f"Error: Volume data not found for {fecha_hace_un_ano_str} in API response.")
        return None

def calcular_aumento_porcentual():

    volume_actual = obtener_volumen_transacciones_24h()
    volume_hace_un_ano = obtener_volumen_transacciones_hace_un_ano()
    
    if volume_actual is not None and volume_hace_un_ano is not None:
        if volume_hace_un_ano > 0:
            aumento_porcentual = ((volume_actual - volume_hace_un_ano) / volume_hace_un_ano) * 100
            aumento_porcentual = round(aumento_porcentual, 2)
            print(f"Aumento porcentual en el volumen de transacciones en BTC-CLP respecto al año anterior: {aumento_porcentual}%")
        else:
            print("Error: No se pudo calcular el aumento porcentual debido a datos insuficientes.")
    else:
        print("Error: No se pudo obtener el volumen actual o el volumen del año anterior de transacciones.")

def obtener_volumen_transacciones():
    if 'ticker' in data_price:
        ticker_data = data_price['ticker']
        
        price_clp = float(ticker_data['last_price'][0])
      
        ask_volume_btc_event = 4.97  
        bid_volume_btc_event = 8.03  
        
        traded_amount_ask_clp = ask_volume_btc_event * price_clp
        traded_amount_bid_clp = bid_volume_btc_event * price_clp
        
    
        total_transacted_clp = traded_amount_ask_clp + traded_amount_bid_clp
        

        total_transacted_clp = round(total_transacted_clp, 2)
        

        print(f"Total transacted in CLP during Black Buda BTC-CLP: {total_transacted_clp} CLP")
        return total_transacted_clp
    else:
        print("Error: Price data not found in API response.")
        return None

def calcular_comision_perdida():
    total_transacted_clp = obtener_volumen_transacciones()
    if total_transacted_clp is not None:
        comision_perdida = total_transacted_clp * 0.008 
        comision_perdida = round(comision_perdida, 2)
        print(f"Dinero (en CLP) dejado de ganar debido a la liberación de comisiones durante el Black Buda: {comision_perdida} CLP")
    else:
        print("Error: No se pudo calcular la comisión perdida debido a datos insuficientes.")


obtener_precio_actual_de_btc()
calcular_aumento_porcentual()
obtener_volumen_transacciones()
calcular_comision_perdida()
