# ✈️ SkyTravel - Flight Booking App

**UAS Web Application Development - Semester Ganjil 2025** **Prasetiya Mulya University**

Aplikasi web pencarian tiket pesawat real-time yang terintegrasi dengan Amadeus API. Dibangun menggunakan Django Framework dengan antarmuka modern bertema macOS.

---

## 🛠 Tech Stack
* **Backend:** Django 5.x (Python)
* **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JS
* **API Integration:** Amadeus Flight Offers Search API
* **Design System:** macOS Big Sur/Monterey Style (Glassmorphism & Native UI)

---

## ✨ Fitur Unggulan
1.  **Realtime Flight Search:** Data penerbangan langsung dari Global Distribution System (GDS) via Amadeus.
2.  **macOS UI Experience:** Desain antarmuka mengikuti style guide macOS.
3.  **Smart Validation:**
    * Validasi kode bandara (IATA 3-letter code only).
    * Validasi tanggal (H+1 logic untuk round trip).
    * Validasi form penumpang (Nama & Paspor).
4.  **Round Trip Support:** Logika otomatis untuk menangani perjalanan pulang-pergi.
5.  **Multi-City Parsing:** Akurasi data rute transit (mengambil segmen awal keberangkatan dan segmen akhir tujuan).
6.  **Responsive Design:** Mobile-first approach, tampilan beradaptasi sempurna di desktop maupun layar smartphone.

---

## 🚀 Cara Menjalankan Project

### 1. Clone Repository
```bash
git clone <repository_url_anda>
cd uas_travel

### 2. Setup Virtual Environment (Recommended)
Windows:
```bash
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
```bash
pip install django amadeus python-dotenv

### 4. Konfigurasi API Key (.env)
AMADEUS_API_KEY=masukkan_api_key_disini
AMADEUS_API_SECRET=masukkan_api_secret_disini

### 5. Jalankan Server
```bash
python manage.py runserver