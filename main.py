from api_client import CurrencyAPI
from converter import CurrencyConverter
from ui import TerminalUI

def main():
    api = CurrencyAPI(base_currency="USD")
    rates, last_update = api.fetch_rates()

    if not rates:
        print("Uygulama başlatılamadı. Lütfen internet bağlantınızı kontrol edin.")
        return

    converter = CurrencyConverter(rates)

    while True:
        choice = TerminalUI.show_menu()

        if choice == '1':
            usd_try = converter.convert(1, "USD", "TRY")
            eur_try = converter.convert(1, "EUR", "TRY")
            jpy_try = converter.convert(1, "JPY", "TRY")
            gbp_try = converter.convert(1, "GBP", "TRY")
            
            TerminalUI.display_dashboard(usd_try, eur_try, jpy_try, gbp_try, last_update)

        elif choice == '2':
            print("\n--- DÖVİZ ÇEVİRİCİ ---")
            from_curr = input("Kaynak Para Birimi (Örn: USD, EUR, GBP, TRY): ").upper()
            to_curr = input("Hedef Para Birimi (Örn: TRY, JPY, USD): ").upper()
            
            try:
                amount = float(input(f"Çevrilecek Miktar ({from_curr}): "))
                result = converter.convert(amount, from_curr, to_curr)
                
                if result is not None:
                    print(f"\n✅ {amount:,.2f} {from_curr} = {result:,.2f} {to_curr}\n")
                else:
                    print("\n❌ Geçersiz para birimi kodu girdiniz.\n")
            except ValueError:
                print("\n❌ Lütfen geçerli bir sayısal miktar girin.\n")

        elif choice == '3':
            print("Uygulamadan çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.\n")

if __name__ == "__main__":
    main()