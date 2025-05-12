# OpenSpace QR Generator (PDF)

Skrypt w Pythonie wspierający aplikację **OpenSpace**. Służy do pobierania kodów QR z bazy danych **Firebase Firestore** i generowania z nich jednego pliku **PDF** — gotowego do druku.

## 🧰 Technologie

- Python
- Firebase Admin SDK
- Google Firestore
- `qrcode` – generowanie kodów QR
- `fpdf` – tworzenie pliku PDF

## 🔧 Jak uruchomić

1. **Zainstaluj wymagane biblioteki** (najlepiej wirtualne środowisko):

   ```bash
   pip install firebase-admin qrcode[pil] fpdf
   ```

2. **Wgraj plik z kluczem Firebase** do katalogu głównego:  
   `openspace-79755-firebase-adminsdk-xxx.json`

3. **Upewnij się, że kolekcja `qrcodes` istnieje w Firestore** i zawiera pola `qrData`.

4. **Uruchom skrypt:**

   ```bash
   python generate_qr.py
   ```

5. **Efekt działania:**  
   Plik `kody_qr.pdf` pojawi się w katalogu głównym i będzie zawierał osobną stronę z kodem QR dla każdego wpisu.

## 📁 Przykładowa struktura danych w Firestore

```
qrcodes (kolekcja)
├── auto_id_1
│   └── qrData: "seat-1"
├── auto_id_2
│   └── qrData: "seat-2"
```

## 🔐 Uwaga

Plik z kluczem Firebase **nie powinien być przesyłany na GitHuba**. Upewnij się, że dodałeś go do `.gitignore`:


## 📄 Licencja

Projekt edukacyjny stworzony jako wsparcie dla aplikacji mobilnej **OpenSpace** (rezerwacja przestrzeni typu open space).
