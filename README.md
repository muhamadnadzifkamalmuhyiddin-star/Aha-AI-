# AHA AI - Asisten Tutor Percakapan Maharah Kalam Interaktif

AHA AI adalah aplikasi berbasis web pintar yang dirancang khusus sebagai media pembelajaran mandiri bagi siswa Kelas XI Madrasah Aliyah (MA). Aplikasi ini berfokus pada peningkatan **Maharah Kalam** (Keterampilan Berbicara) menggunakan simulasi percakapan dua arah interaktif bersama guru virtual yang ditenagai oleh kecerdasan buatan (AI).

---

## 👤 Identitas Pengembang
* **Nama Mahasiswa:** [Isi Nama Anda di Sini]
* **NIM:** [Isi NIM Anda di Sini]
* **Mata Kuliah / Proyek:** Pembelajaran Bahasa Arab Berbasis Digital / Tugas Akhir

---

## 🎯 Maharah dan Level yang Dipilih beserta Alasan

* **Maharah (Keterampilan):** Maharah Kalam (مهارة الكلام) - Keterampilan Berbicara.
* **Level Target:** Kelas XI Madrasah Aliyah (MA).
* **Alasan Pemilihan:**
  1. **Tantangan Praktik Mandiri:** Pembelajaran Maharah Kalam di kelas sering terkendala keterbatasan waktu, sehingga siswa jarang mendapatkan giliran untuk mempraktikkan dialog bahasa Arab secara langsung.
  2. **Rasa Percaya Diri:** Banyak siswa merasa takut salah atau malu ketika berbicara di depan umum. AHA AI hadir sebagai ruang aman (safe space) bagi siswa untuk melatih respons percakapan tanpa tekanan sosial.
  3. **Kontekstualisasi Kurikulum:** Topik percakapan disesuaikan secara presisi dengan kurikulum bahasa Arab Kelas XI MA (seperti berbelanja, pasar, dan hobi) agar sejalan dengan target pembelajaran di madrasah.

---

## 🛠️ Layanan API yang Digunakan
Aplikasi ini diintegrasikan secara penuh dengan **Google AI Studio API** menggunakan model generasi terbaru:
* **`gemini-2.5-flash`** (Sebagai mesin utama untuk pemrosesan teks dialog yang cepat dan kontekstual).
* **`gemini-1.5-flash`** (Sebagai mesin cadangan/fallback otomatis jika server utama mengalami lonjakan antrean/overload).

---

## 🕹️ Fitur-Fitur yang Tersedia
1. **Gerbang Keamanan Validasi Data:** Form input Nama, NIM, dan API Key yang wajib diisi sebelum masuk ke ruang chatbot guna menjaga otentikasi pengguna.
2. **Multi-Persona Partner Hiwar:** Siswa dapat memilih partner berbicara virtual yang diinginkan, yaitu **Ustadz Syarif** atau **Ustadzah Fatimah** dengan karakteristik gaya bahasa yang unik.
3. **Pilihan Tema Pembelajaran Adaptif Kelas XI:** Modul materi percakapan mencakup tema *At-Tasawuq* (Berbelanja), *Fissuqi* (Di Pasar), dan *Al-Hiwayah* (Hobi).
4. **Sistem Deteksi Auto-Retry (Anti-Error 503):** Kode dilengkapi penanganan galat (*error handling*) bertingkat jika server Google AI Studio sedang sibuk, lengkap dengan rekomendasi perpindahan model secara manual di panel samping.
5. **Koreksi dan Apresiasi Islami:** AI akan secara otomatis menilai tata bahasa/diksi siswa, memberikan perbaikan konstruktif, serta memberikan kalimat pujian Islami (*Mumtaz*, *Barakallahufiik*).

---

## 🚀 Cara Instalasi dan Menjalankan Aplikasi

### 1. Kloning Repositori
Langkah pertama, unduh repositori ini ke komputer lokal Anda:
```bash
git clone [https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git](https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git)
cd NAMA_REPOSITORI