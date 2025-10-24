# Gerçek Zamanlı Yüz Tespiti Aracı (Real-Time Face Detector)

OpenCV ve Haar Cascade sınıflandırıcıları kullanılarak Python ile geliştirilmiş basit bir gerçek zamanlı yüz tespiti uygulaması.

![Proje Demosu](https://i.imgur.com/your-demo-image.gif)  
*(İsteğe bağlı: Projenizin çalıştığına dair bir ekran görüntüsü veya GIF eklerseniz harika görünür!)*

## 📝 Açıklama (Description)

Bu proje, bir web kamerası akışından alınan video görüntülerini kare kare analiz eder ve görüntüdeki insan yüzlerini tespit eder. Tespit edilen her yüzün etrafına mavi bir dikdörtgen çizer.

Bu proje, renk tabanlı nesne takibinin (arka plan renkleriyle karıştırma gibi) zayıflıklarını göstermiş ve bu sorunu çözmek için desen tanımaya dayalı (pattern recognition) daha sağlam bir yöntem olan Haar Cascade'lere geçiş yapmıştır.

## ✨ Özellikler

* **Gerçek Zamanlı Tespit:** Web kamerasından gelen canlı video akışı üzerinde çalışır.
* **Yüksek İsabet:** OpenCV'nin önceden eğitilmiş `haarcascade_frontalface_default.xml` modelini kullanarak yüksek doğrulukla yüzleri bulur.
* **Ayna Modu:** Kullanıcı deneyimini iyileştirmek için kamera görüntüsü yatay olarak çevrilmiştir (ayna efekti).
* **Sağlamlık:** Arka plan renginden veya aydınlatma koşullarından (renk tabanlı yöntemlere kıyasla) daha az etkilenir.

## 🛠️ Kullanılan Teknolojiler

* **Python 3**
* **OpenCV** (`opencv-python` kütüphanesi)
* **Haar Cascade Sınıflandırıcıları** (OpenCV'nin bir parçası olarak)

## 🚀 Projeyi Yerel Olarak Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### 1. Gereksinimler

* Python 3.x
* Bilgisayarınıza bağlı bir web kamerası

### 2. Kurulum

1.  **Depoyu Klonlayın (veya ZIP olarak indirin):**
    ```bash
    git clone [https://github.com/aybukezehra/face_detector.git](https://github.com/aybukezehra/face_detector.git)
    cd face_detector
    ```

2.  **Sanal Ortam (Virtual Environment) Oluşturun ve Aktifleştirin:**
    *(Bu, sisteminizdeki diğer Python projelerini etkilememek için en iyi pratiktir.)*
    ```bash
    # venv adında bir sanal ortam oluştur
    python -m venv venv
    
    # Windows için aktifleştirme
    .\venv\Scripts\activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install opencv-python numpy
    ```
    *(Not: Bu proje için `numpy` zorunlu olmasa da, OpenCV'nin birçok işlemi için gereklidir.)*

### 3. Çalıştırma

Aşağıdaki komutla ana betiği çalıştırın. Kamera açılacak ve yüzünüzü algılamaya başlayacaktır.

```bash
python tracker.py