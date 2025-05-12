import firebase_admin
from firebase_admin import credentials, firestore
import qrcode
from fpdf import FPDF
import os

# 🔹 1. Firebase
cred = credentials.Certificate("openspace-79755-firebase-adminsdk-fbsvc-338051babd.json")  # Wgraj plik JSON z Firebase
firebase_admin.initialize_app(cred)
db = firestore.client()

# 🔹 2. Pobieranie kodów QR z Firestore
def fetch_qr_codes():
    qr_codes = []
    docs = db.collection("qrcodes").stream()  
    for doc in docs:
        qr_codes.append(doc.to_dict()["qrData"])  
    return qr_codes

# 🔹 3. Tworzenie pliku PDF
def generate_qr_pdf(qr_codes):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for code in qr_codes:
        pdf.add_page()
        
        
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, f"Kod QR: {code}", ln=True, align="C")

       
        qr = qrcode.make(code)
        qr_path = f"{code}.png"
        qr.save(qr_path)

       
        pdf.image(qr_path, x=60, y=40, w=90)

        
        os.remove(qr_path)

   
    pdf.output("kody_qr.pdf")
    print("✅ Plik 'kody_qr.pdf' został zapisany!")

# 🔹 4. Pobiera kody QR i generuje PDF
qr_codes = fetch_qr_codes()
if qr_codes:
    generate_qr_pdf(qr_codes)
    print("✅ Gotowe! Otwórz 'kody_qr.pdf' i wydrukuj!")
else:
    print("❌ Brak kodów QR w bazie!")
