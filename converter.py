class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def get_exchange_rate(self, target_currency):
        """1 USD'nin istenen para birimindeki değerini döndürür."""
        return self.rates.get(target_currency.upper())

    def convert(self, amount, from_curr, to_curr):
        """Herhangi iki para birimi arasında çapraz kur dönüşümü yapar."""
        from_curr = from_curr.upper()
        to_curr = to_curr.upper()

        if from_curr not in self.rates or to_curr not in self.rates:
            return None

        # USD üzerinden çapraz kur hesabı
        # (Amount / From_Rate) -> Tutarı önce USD'ye çevirir
        # * To_Rate -> Sonra hedef birime çevirir
        usd_amount = amount / self.rates[from_curr]
        converted_amount = usd_amount * self.rates[to_curr]
        
        return converted_amount