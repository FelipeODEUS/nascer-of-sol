import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
fps = cv2.imread(images[0])
jordan, garfild, globo = fps.shape
lebron = (garfild, jordan)
print(lebron)
hollywood = cv2.VideoWriter("Kobe_Bryan.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 25, lebron)
for i in range(count -1, 0, -1):
    fps = cv2.imread(images[i])
    hollywood.write(fps)
hollywood.release()
print("acabou")