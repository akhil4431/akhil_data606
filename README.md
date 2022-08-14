# Data 606 - Capstone Project

# TEA LEAF DISEASE PREDICTION

### Goal:
The main objective of this study is to use machine learning and image processing techniques to predict the tea sickness in its early phases.  In this way, my model will help for tea plant farmers for early prediction. 

### Introduction:  
The second most popular beverage worldwide is tea. Most of it is grown in the continents of Asia, Africa, and South America. It has medicinal and health care purposes, contains a range of powerful substances that the human body needs, and is very good at boosting immunity. For tea producers, planting tea is a crucial part of their business strategy for success. The productivity of agriculture is greatly impacted by changes in the weather. The number of diseases is growing as time goes on because of climatic changes. Crop disease attacks result in significant productivity losses for agriculture, and the use of chemicals in agriculture has further diversified the issue. Early illness attack detection is crucial for proactive, efficient, and successful disease control and for promoting sustainable development. Furthermore, the majority of these tea plants are grown on mountain areas. Due to the small number of residents in these locations, it is difficult to gain much assistance from others in identifying these diseases. As a result, it takes a long time and costs money for professionals to travel visit the tea estate and establish a diagnosis.

### Dataset Description: 
This tea sickness dataset contains tea leaves showing 7 common diseases of tea:

* Red leaf spot 
* Algal leaf spot 
* Bird’s eyespot 
* Gray blight 
* White spot 
* Anthracnose 
* Brown blight 

![image](https://user-images.githubusercontent.com/100260849/184511652-c615b45c-d8c5-4756-a5c9-c67699ab87bf.png)

![image](https://user-images.githubusercontent.com/100260849/184511655-0094e01a-6502-404b-ac1c-7bf7c9917338.png)

Images of healthy leaves are also included, along with images of the seven diseases, to train my algorithm to recognize even leaves in good health. The dataset was collected in Johnstone Boiyon farm, Koiwa location, Bomet county from a clone of 1510.

### EDA:

![image](https://user-images.githubusercontent.com/100260849/184511671-4c3f4e06-7db6-47fc-918b-73a7a839ef1d.png)

The number of tea leaf photos in my data set is depicted in the bar graph. More than 100 photos are included in each category.

Models Used and Results:

Three models are utilized in this project: XgBoost, Convolution Neural Networks, and K-Nearest Neighbors. In testing, XGBoosting outperformed CNN and KNN in terms of accuracy.

![image](https://user-images.githubusercontent.com/100260849/184511676-226ae228-6487-42c4-ac3d-8ecccf331388.png)


### Deployment:
The entire project is deployed using Streamlit. Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. We can instantly develop web apps and deploy them easily using Streamlit.
Below image shows the user interface:

![image](https://user-images.githubusercontent.com/100260849/184511679-19616689-b472-4c0f-92f4-66ef54a14e4e.png)

###Video Presentation Link: https://youtu.be/an-780CFrNU

### Conclusion:
In conclusion, it is advisable to choose and deploy the Xgboost model. Increasing the data volume will help this model perform better and working on this model even further can definitely improve the accuracy.


### References:

1) Pandey, A. K., Sinniah, G. D., Babu, A. K., & Tanti, A. (2021). How the Global Tea Industry Copes up with Fungal Diseases-Challenges and Opportunities. Plant Disease. https://doi.org/10.1094/pdis-09-20-1945-fe .
2)  vikaspedia Domains. (n.d.). Vikaspedia.in. Retrieved June 10, 2022, from https://vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-commercial-crops/ipm-strategies-for-tea/tea-diseases
3) Chauhan, A. (2022, February 6). Make WebApp With Streamlit With Python. The Pythoneers. https://medium.com/pythoneers/make-webapp-with-streamlit-with-python-ecc59e488a5
4) Rao, A. (2018, November 27). Convolutional Neural Network Tutorial (CNN) – Developing An Image Classifier In Python Using TensorFlow. Edureka; Edureka. https://www.edureka.co/blog/convolutional-neural-network/
5) https://realpython.com/knn-python/#:~:text=The%20kNN%20algorithm%20is%20a%20supervised%20machine%20learning,Practical%20Guide.%20kNN%20Is%20a%20Nonlinear%20Learning%20Algorithm
6) Maklin, C. (2020, May 9). XGBoost Python Example. Medium. https://towardsdatascience.com/xgboost-python-example-42777d01001e
