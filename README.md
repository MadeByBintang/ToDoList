UAS ASJ 2025 - Aplikasi To-Do List

Nama: Adrian Bintang Saputera
NIM: 2310817110006
Kelas: Sistem Informasi
Mata Kuliah: Administrasi Sistem dan Jaringan

---

Deskripsi Proyek

Aplikasi ini adalah to-do list berbasis web yang dibangun dengan:

- ✅ Python (Flask) sebagai backend
- ✅ PostgreSQL sebagai database
- ✅ Docker dan Docker Compose untuk environment containerized
- ✅ CI/CD pipeline dengan GitLab
- ✅ HTML, CSS, dan JavaScript untuk tampilan modern dan interaktif

Aplikasi ini memungkinkan pengguna untuk:

- Menambah tugas
- Mengedit tugas
- Menghapus tugas
- Menyimpan data ke database
- Menampilkan tugas dalam tampilan rapi dan modern

---

Cara Menjalankan Aplikasi

1. Jalankan Docker Compose

   sudo docker-compose up

   Akses aplikasi di browser:

   http://localhost:5000

2. Hentikan

   sudo docker-compose down

---

CI/CD

CI/CD pipeline menggunakan GitHub Actions:

- Build image Docker secara otomatis dari Dockerfile
- Simulasi deployment melalui docker-compose
- Pipeline berjalan otomatis setiap kali terjadi perubahan (push) ke branch main
- File pipeline terletak di: .github/workflows/docker-build.yml

---

Keamanan & Konfigurasi

- File .env digunakan untuk menyimpan variabel sensitif seperti kredensial database.
- File ini diabaikan dari Git menggunakan .gitignore.
