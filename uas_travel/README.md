# ✈️ SkyTravel - Flight Booking App
**UAS Web Application Development - Semester Ganjil 2025 — Prasetiya Mulya University**

Aplikasi web pencarian tiket pesawat real-time terintegrasi dengan Amadeus API, dibangun menggunakan Django dengan UI modern bertema macOS.

---

## 🛠 Tech Stack
- **Backend:** Django 5.2.9 (Python)
- **Frontend:** HTML5, Tailwind CSS (CDN), Vanilla JS
- **API:** Amadeus Flight Offers Search API
- **Design:** macOS Big Sur Style

---

## ✨ Fitur
1. Realtime flight search
2. UI macOS Style
3. Smart validation (IATA code, tanggal, penumpang)
4. Round trip support
5. Multi-city parsing dengan transit route detection
6. Responsive (mobile-first)

---

## 🚀 Cara Menjalankan

### 1. Clone Repo
```bash
git clone https://github.com/Earthen8/UAS-WEB-2025-Earthen.git
cd uas_travel
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux / Mac
```

### 3. Install Dependency
```bash
pip install django amadeus python-dotenv
```

### 4. Tambahkan .env
```env
AMADEUS_API_KEY=isi_key
AMADEUS_API_SECRET=isi_secret
```

### 5. Run
```bash
python manage.py runserver
```