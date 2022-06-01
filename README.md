# Catbreeds-ta

## Objective
A cat owner can have more than one cat, either the same breed or different breeds. But not all cat owners know the breeds of their cats. Therefore, this project of cat breeds classification would be conducted with Convolutional Neural Network (CNN) in the multi-object images. 

## Dataset
The dataset is obtained from [Kaggle](https://www.kaggle.com/ma7555/cat-breeds-dataset). This project used 5 type of cat breeds there are Bengal, Calico, Persian, Siamese and Sphynx. Those type of cat breeds were chosen because it has a difference in color and pattern between each other. The data that used for training is a single object image. 

| Label | Number of Images |
| :---------: | :----------------: |
| Bengal | 2477 |
| Calico | 3468 |
| Persian | 4018 |
| Siamese | 2888 |
| Sphynx | 209 |
| Total | 13059 |


![image](https://user-images.githubusercontent.com/60678535/171352315-fd531a3a-0688-4360-9969-05eaf200591a.png)

## CNN Architecture
The CNN architecture applied in this project is Xception which consists of 36 convolutional layers to generate feature extraction for image classification. The architecture divided into 3 main parts: the entry flow, the middle flow and the exit flow.

## Result
The test results were measured using confusion matrix obtaining the precision, recall, f1 score and accuracy of 100% on multi-object images with 2 objects and 3 objects. On images with 4 objects achieved the precision, recall, f1 score and accuracy value of 89%, 87%, 87% and 95%. While the value of precision, recall, f1 score and accuracy on images with 5 objects get 87%, 86%, 86% and 94%, respectively.

![33](https://user-images.githubusercontent.com/60678535/171354652-0d82e848-e9ee-4af7-846e-2418eaddd056.jpg)
![40](https://user-images.githubusercontent.com/60678535/171354665-3d4d8ec3-39d6-4efb-b875-2ae67bd99270.jpg)
![3](https://user-images.githubusercontent.com/60678535/171354670-5b11b4f9-6500-43b5-a81a-c748070e1af6.jpg)
![16](https://user-images.githubusercontent.com/60678535/171354676-c5b4c8d5-1ad0-4454-9e31-e7eb2f36b1c0.jpg)
![30](https://user-images.githubusercontent.com/60678535/171354678-ea556a23-0990-4b6a-bc3a-2250c514f323.jpg)
