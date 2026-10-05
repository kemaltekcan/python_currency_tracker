class TerminalUI:
    @staticmethod
    def display_dashboard(usd_try, eur_try, jpy_try, gbp_try, last_update):
        print("\n==========================================")
        print("       CANLI DÖVİZ KURU PANOSU            ")
        print("==========================================")
        print(f" 💵 ABD Doları (USD/TRY) : ₺{usd_try:.2f}")
        print(f" 💶 Euro       (EUR/TRY) : ₺{eur_try:.2f}")
        print(f" 💷 Sterlin    (GBP/TRY) : ₺{gbp_try:.2f}")
        print(f" 💴 Japon Yeni (JPY/TRY) : ₺{jpy_try:.2f}")
        print("==========================================")
        print(f"Son Güncelleme: {last_update[:16] if last_update else 'N/A'}\n")

    @staticmethod
    def show_menu():
        print("--- MENÜ ---")
        print("1. Anlık Kurları Göster")
        print("2. Döviz Çevirici (Converter)")
        print("3. Çıkış")
        return input("Seçiminiz (1-3): ")