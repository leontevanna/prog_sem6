# подключаем библиотеку компьютерного зрения 
import cv2
import os


# функция определения лиц
def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]

    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    # устанавливаем этот объект как входной параметр для нейросети
    net.setInput(blob)
    # выполняем прямой проход для распознавания лиц
    detections=net.forward()
    # переменная для рамок вокруг лица
    faceBoxes=[]
    # перебираем все блоки после распознавания
    for i in range(detections.shape[2]):
        # получаем результат вычислений для очередного элемента
        confidence=detections[0,0,i,2]
        # если результат превышает порог срабатывания — это лицо
        if confidence>conf_threshold:
            # формируем координаты рамки
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            # добавляем их в общую переменную
            faceBoxes.append([x1,y1,x2,y2])
            # рисуем рамку на кадре
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    # возвращаем кадр с рамками
    return frameOpencvDnn,faceBoxes

def findFaces(input_= None):
    faceProto="D:\LR8\detector.pbtxt"
    faceModel="D:\LR8\detector_uint.pb"

    # запускаем нейросеть по распознаванию лиц
    faceNet=cv2.dnn.readNet(faceModel,faceProto)
    
    if input_== None:
        # получаем видео с камеры
        video=cv2.VideoCapture(0)
        # пока не нажата любая клавиша — выполняем цикл
        while cv2.waitKey(1)<0:
            # получаем очередной кадр с камеры
            hasFrame,frame=video.read()
            # если кадра нет
            if not hasFrame:
                # останавливаемся и выходим из цикла
                cv2.waitKey()
                break
            # распознаём лица в кадре
            resultImg,faceBoxes=highlightFace(faceNet,frame)
            # если лиц нет
            if not faceBoxes:
                # выводим в консоли, что лицо не найдено
                print("Лица не распознаны")
            # выводим картинку с камеры
            cv2.imshow("Face detection", resultImg)
    else:
        # распознаём лица в кадре
        frame = cv2.imread(input_)
        resultImg, faceBoxes = highlightFace(faceNet, frame)
         # если лиц нет
        if not faceBoxes:
            # выводим в консоли, что лицо не найдено
            print("Лица не распознаны")
        while cv2.waitKey(1) < 0:
            cv2.imshow("Laboratory work #8", resultImg)



if __name__ == '__main__': 
    #os.startfile(r'D:\LR8\gosling.jpg')
    
    print("Select mode: \n Camera - cam \n File - file")
    data = input("Your answer: ")
    if data == 'cam':
        findFaces()
    elif data == 'file':
        file = input("Enter the full path to the file: ")
        print("Name: ", file)
        #os.startfile(file)
        findFaces(file)
    else:
        print("No action was selected")