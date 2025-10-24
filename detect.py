import cv2
import numpy as np
import os # Dosya yollarını birleştirmek için bu kütüphaneye ihtiyacımız var

# Adım 0: Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera başlatılamadı.")
    exit()

# --- YENİ ADIM 1: Modeli Otomatik Olarak Kütüphaneden Bul ---
# OpenCV kütüphanesine, içinde .xml modellerinin olduğu
# 'data' klasörünün tam yolunu soruyoruz
cascade_dir = cv2.data.haarcascades

# Yüz tespiti modelimizin tam yolunu bu klasörün içinde oluşturuyoruz
face_cascade_path = os.path.join(cascade_dir, 'haarcascade_frontalface_default.xml')

# Modeli bu tam (dinamik) yolu kullanarak yüklüyoruz
face_cascade = cv2.CascadeClassifier(face_cascade_path)
# ---------------------------------------------------------

# Modelin doğru yüklenip yüklenmediğini kontrol et
if face_cascade.empty():
    print(f"Hata: Cascade classifier dosyası yüklenemedi: {face_cascade_path}")
    print("Lütfen OpenCV kurulumunuzu kontrol edin (pip install opencv-python).")
    exit()

print("Kamera başlatıldı. (Ayna Modu Aktif). Çıkmak için 'q' tuşuna basın.")
print(f"Model başarıyla yüklendi: {face_cascade_path}")
print("Yüz tespiti başladı...")

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü yatay eksende (ayna görüntüsü) çevir
    frame = cv2.flip(frame, 1)

    # Adım 2: Tespiti hızlandırmak için görüntüyü Gri Tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Adım 3: Yüz tespiti yap
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Adım 4: Tespit edilen yüzlerin etrafına kutu çiz
    for (x, y, w, h) in faces:
        # Orijinal 'frame' (renkli) üzerine dikdörtgeni çiz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Yüzün üzerine bir metin ekle
        cv2.putText(frame, "Yuz", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Sonucu göster
    cv2.imshow('Yuz Tespiti Ekrani', frame)

    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şeyi serbest bırak
cap.release()
cv2.destroyAllWindows()