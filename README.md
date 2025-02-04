
# 🐝 Bee Detection with YOLOv8s / YOLOv8s ile Arı Tespiti

This project is a **real-time bee detection system** using a custom-trained **YOLOv8s** model. The model was trained on **10,000 bee images** using the Ultralytics platform and is deployed for real-time detection using OpenCV.

Bu proje, **özel olarak eğitilmiş bir YOLOv8s modeli** kullanarak **gerçek zamanlı arı tespiti sistemi** geliştirmek için oluşturulmuştur. Model, **10.000 arı görüntüsü** ile Ultralytics platformunda eğitilmiş ve OpenCV kullanılarak gerçek zamanlı tespit için uygulanmıştır.

## 📌 Features / Özellikler

- 🟢 **Real-time bee detection** using a webcam / **Gerçek zamanlı arı tespiti**
- 🏎 **Optimized YOLOv8s model** for fast performance / **Hızlı performans için optimize edilmiş model**
- 🎯 **Confidence filtering** (only detections with >75% confidence are shown) / **Doğruluk filtresi** (Sadece %75'in üzerindeki tespitler gösterilir)
- 📊 **Model Accuracy:** 93% / **Model Doğruluk Oranı:** %93
- 🖼 **Bounding boxes with labels** for detected bees / **Tespit edilen arılar için kutular ve etiketler**

## 🚀 Installation / Kurulum

1️⃣ **Clone the repository / Depoyu klonlayın:**

```sh
git clone https://github.com/yazilimcihanim/BeeDetection_YoloV8s.git
cd BeeDetection_YoloV8s
```

2️⃣ **Create a virtual environment (optional but recommended) / Sanal ortam oluşturun (isteğe bağlı ancak önerilir):**

```sh
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

3️⃣ **Install dependencies / Bağımlılıkları yükleyin:**

```sh
pip install ultralytics opencv-python
```

4️⃣ **Download the trained model / Eğitilmiş modeli indirin:**

- Place your `best.pt` file in the project folder. / `best.pt` dosyanızı proje klasörüne yerleştirin.

## 🎥 Running the Bee Detection / Arı Tespiti Çalıştırma

```sh
python 
```

## &#x20;BeeDetection\_YoloV8.py📝 Project Structure / Proje Yapısı

```
BeeDetection_YoloV8s/
│── best.pt              # Trained YOLOv8s model / Eğitilmiş model
│── BeeDetection_YOLOV8.py        # Main script for real-time detection / Gerçek zamanlı tespit için ana script
│── requirements.txt     # Dependencies / Bağımlılıklar
│── README.md            # Project documentation / Proje dokümantasyonu
```


## 🔧 Model Training Details / Model Eğitim Detayları

- **Dataset / Veri Kümesi:** 10,000 bee images / 10.000 arı görüntüsü
- **Model:** YOLOv8s
- **Platform:** Ultralytics
- **Training Epochs / Eğitim Epok Sayısı:** 100
- **Confidence Threshold / Doğruluk Eşiği:** 0.75 (only detections above 75% are displayed) / (Sadece %75'in üzerindeki tespitler gösterilir)
- **Overall Model Accuracy / Genel Model Doğruluğu:** 93%

## 🤝 Contributing / Katkıda Bulunma

This project was developed individually without any collaboration.
İyileştirme önerileriniz varsa, bir issue açabilir veya pull request gönderebilirsiniz!

## 📜 License / Lisans

This project is licensed under the MIT License.
Bu proje MIT Lisansı altında lisanslanmıştır.

---

**Author / Yazar:** Fatma Gençer
📧 Contact / İletişim: yazilimci00hanim@gmail.com 
🔗 GitHub: [yazilimcihanim](https://github.com/yazilimcihanim)

