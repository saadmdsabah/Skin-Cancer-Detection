# Skin-Cancer-Detection
Developed an AI-powered Skin Cancer detection system utilizing Convolutional Neural Networks in Python, enhancing early diagnosis and treatment through machine learning techniques

Detecting skin cancer using AI, and ML, specifically CNN in Python, addresses a critical need for early and accurate diagnosis in healthcare. Skin cancer, often manifesting subtly, requires precise identification for timely intervention. AI-based detection systems harness vast datasets to recognize intricate patterns in skin lesions, significantly augmenting the accuracy and speed of diagnosis. Integrating a chatbot within the website further extends this impact by providing accessible information and guidance to users concerned about skin health. This dynamic interface offers real-time assistance, educational resources, and even preliminary assessments, empowering individuals to seek timely medical advice and potentially identify concerning symptoms earlier. The fusion of AI, ML, CNN in Python, and a website-based chatbot not only revolutionizes skin cancer detection but also serves as a proactive tool for education, prevention, and early intervention. Use cases span from supporting healthcare professionals in their diagnostic processes to empowering individuals to make informed decisions about their skin health, ultimately improving outcomes and reducing the burden of this prevalent disease.

## Disclaimer:  
The AI-driven Skin Cancer detection system, chatbot functionalities, and information provided on this website are intended for informational purposes only. While the system aims to enhance early detection and provide guidance, it should not substitute professional medical advice, diagnosis, or treatment. Users are encouraged to consult qualified healthcare professionals for personalized assessments and recommendations concerning their skin health. The accuracy of the AI-based detection system is subject to the limitations of available data and technology and should be used as a supplementary tool rather than a definitive diagnostic method.

## Run the application
●	Run pip install requirements.txt in the terminal

●	Run the Python files(85% acc.ipynb) in the Kaggle notebook(recommended) given in MainWebsite folder to get h5 file and add it to the MainWebsite folder

●	Run train.py

●	Run chatbot.py

●	Run app.py

●	Navigate to the localhost where you can view your web page.

![image](https://github.com/saadmdsabah/AI-Enabled-car-parking-System/assets/103499208/32207286-2f3d-4a7d-8270-a8b9543da650)

# Skin Cancer Detection ML Model

## Description:
The Skin Cancer Detection ML Model is a Convolutional Neural Network (CNN) based on Python, designed to identify and classify skin lesions as cancerous or non-cancerous. Trained on extensive datasets comprising various skin lesion images, the model has learned to recognize intricate patterns and features indicative of skin cancers such as melanoma, basal cell carcinoma, and squamous cell carcinoma.

## Process:
### Input: 
The model takes an input image of a skin lesion, usually as a digital image file.

### Preprocessing:

The input image undergoes preprocessing steps such as normalization, resizing, and enhancement to standardize it for analysis.
### Feature Extraction:

Leveraging its CNN architecture, the model extracts essential features from the image, identifying distinct patterns, textures, and structures.
### Classification:

Using the extracted features, the model performs classification to determine whether the lesion is cancerous or non-cancerous.
### Output:

The model generates an output indicating the classification result:
Cancerous: If the lesion exhibits characteristics associated with skin cancers.
Non-cancerous: If the lesion doesn't show signs of malignancy.
