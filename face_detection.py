import cv2
import numpy as np

# 1. تحميل مصنف الكشف عن الوجوه (مدمج مع OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. تحديد مسار الفيديو (يجب أن يكون في نفس المجلد)
video_path = 'test_video.mp4'

# 3. بدء قراءة الفيديو
cap = cv2.VideoCapture(video_path)

# 4. التحقق من فتح الفيديو بنجاح
if not cap.isOpened():
    print("خطأ: لا يمكن فتح ملف الفيديو! تأكد من:")
    print("- أن الملف موجود في نفس المجلد")
    print("- أن اسم الملف مطابق (test_video.mp4)")
    exit()

# 5. معالجة إطار كل فيديو
while True:
    # قراءة الإطار التالي
    ret, frame = cap.read()
    
    # إذا وصلنا لنهاية الفيديو، نخرج من الحلقة
    if not ret:
        print("تم معالجة الفيديو بالكامل!")
        break
    
    # 6. تحويل الإطار إلى تدرجات الرمادي (مطلوب للكشف)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 7. الكشف عن الوجوه
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # حساسية الكشف (كلما قل الرقم زادت الدقة لكن مع بطء)
        minNeighbors=5,   # عدد الجيران المطلوبة لتأكيد الوجه
        minSize=(30, 30)  # أصغر حجم للوجه المكتشف
    )
    
    # 8. رسم مستطيل أخضر حول كل وجه
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # 9. عرض النتيجة في نافذة
    cv2.imshow('Face Detection - Press Q to Exit', frame)
    
    # 10. الخروج بالضغط على زر Q
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 11. إغلاق كل النوافذ وتحرير الذاكرة
cap.release()
cv2.destroyAllWindows()