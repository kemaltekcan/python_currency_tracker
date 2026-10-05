import requests

class CurrencyAPI:
    def __init__(self, base_currency="USD"):
        self.base_url = f"https://open.er-api.com/v6/latest/{base_currency}"

    def fetch_rates(self):
        """API'den güncel kurları çeker ve JSON olarak döndürür."""
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get("result") == "success":
                return data['rates'], data.get('time_last_update_utc', '')
            else:
                raise Exception("API yanıtı başarısız döndü.")
                
        except requests.exceptions.RequestException as e:
            print(f"[HATA] Ağ/API Bağlantı Hatası: {e}")
            return None, None