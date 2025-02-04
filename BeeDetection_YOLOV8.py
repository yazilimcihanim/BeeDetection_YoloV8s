from ultralytics import YOLO
import cv2

# Kamera başlatma
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Genişlik
cap.set(4, 480)  # Yükseklik

# YOLO modelini yükleme
model = YOLO('best.pt')

while True:
    success, img = cap.read()  # Kameradan görüntü al
    if not success:
        break

    # Model ile tahmin yap
    results = model(img)

    # Sonuçları işleyerek yalnızca doğruluk değeri 0.7 üzerindekileri çiz
    for result in results:
        for box in result.boxes:
            conf = box.conf[0].item()  # Doğruluk değeri (confidence score)
            if conf > 0.75:  # Sadece 0.75'in üzerindeki tahminleri göster
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Koordinatları al
                label = f"{model.names[int(box.cls[0])]}: {conf:.2f}"  # Etiket oluştur

                # Kutuyu çiz
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("YOLO Detection", img)

    # Çıkış için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()