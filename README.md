# Skin-Cancer-Detection
Developed an AI-powered Skin Cancer detection system utilizing Convolutional Neural Networks in Python, enhancing early diagnosis and treatment through machine learning techniques

Detecting skin cancer using AI, and ML, specifically CNN in Python, addresses a critical need for early and accurate diagnosis in healthcare. Skin cancer, often manifesting subtly, requires precise identification for timely intervention. AI-based detection systems harness vast datasets to recognize intricate patterns in skin lesions, significantly augmenting the accuracy and speed of diagnosis. Integrating a chatbot within the website further extends this impact by providing accessible information and guidance to users concerned about skin health. This dynamic interface offers real-time assistance, educational resources, and even preliminary assessments, empowering individuals to seek timely medical advice and potentially identify concerning symptoms earlier. The fusion of AI, ML, CNN in Python, and a website-based chatbot not only revolutionizes skin cancer detection but also serves as a proactive tool for education, prevention, and early intervention. Use cases span from supporting healthcare professionals in their diagnostic processes to empowering individuals to make informed decisions about their skin health, ultimately improving outcomes and reducing the burden of this prevalent disease.

## Disclaimer:  
The AI-driven Skin Cancer detection system, chatbot functionalities, and information provided on this website are intended for informational purposes only. While the system aims to enhance early detection and provide guidance, it should not substitute professional medical advice, diagnosis, or treatment. Users are encouraged to consult qualified healthcare professionals for personalized assessments and recommendations concerning their skin health. The accuracy of the AI-based detection system is subject to the limitations of available data and technology and should be used as a supplementary tool rather than a definitive diagnostic method.

## Run the application
### Note: Download Models form Models.txt file 
●	Run pip install requirements.txt in the terminal

●	Run the Python files(85% acc.ipynb) in the Kaggle notebook(recommended) to get h5 file and add it to the MainWebsite folder

●	Run train.py

●	Run chatbot.py

●	Run app.py

●	Navigate to the localhost where you can view your web page.

![image](https://github.com/saadmdsabah/AI-Enabled-car-parking-System/assets/103499208/32207286-2f3d-4a7d-8270-a8b9543da650)

# Main Page 

![image](https://github.com/saadmdsabah/Skin-Cancer-Detection/assets/103499208/06101a42-9a97-4dba-9bec-8827570ed6a8)


The main page serves as the gateway to the website, prominently displaying a disclaimer acknowledging that the information provided on the site is for educational purposes only. It emphasizes the importance of consulting healthcare professionals for accurate diagnosis, treatment, and medical advice.

## Team Information:
This section introduces the team behind the website's creation. It includes brief profiles and roles of the team members involved in developing the skin cancer detection model, chatbot functionality, and website design. This fosters transparency and establishes credibility.

## Brief About Skin Cancer:
Offering a concise overview, this section outlines essential information about skin cancer. It covers key facts, types of skin cancer, risk factors, the importance of early detection, and general preventive measures. The content aims to raise awareness and emphasize the significance of proactive health management.

## Subpage 1: Model Prediction
This subpage focuses on the skin cancer detection model. It elaborates on the model's functionality, using Convolutional Neural Networks (CNN) in Python for image analysis. Users can access this page to upload an image of a skin lesion for analysis. The page explains the process, showcases sample results, and emphasizes the model's role in aiding early detection.

## Subpage 2: Chatbot
This subpage introduces the healthcare chatbot. It explains how users can interact with the chatbot to obtain information about diseases, symptoms, medications, and even schedule appointments. The chatbot is designed to engage users in informative conversations, offering guidance and support in understanding health-related queries.

# Skin Cancer Detection ML Model

![image](https://github.com/saadmdsabah/Skin-Cancer-Detection/assets/103499208/ca5bc980-f140-497e-806d-202839bd0f0b)

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

![image](https://github.com/saadmdsabah/Skin-Cancer-Detection/assets/103499208/8562acbf-262b-4537-b217-ea0ae9b49b37)

# Healthcare Chatbot Description

![image](https://github.com/saadmdsabah/Skin-Cancer-Detection/assets/103499208/a01680c8-c51f-4e41-abe2-ddf71cd679db)

## Description:
The Healthcare Chatbot is an AI-driven conversational interface designed to provide informational support and guidance regarding various diseases, symptoms, medications, and appointment scheduling. Developed using the Chatterbot module in Python, this chatbot leverages natural language processing (NLP) techniques to understand user queries and respond with relevant and accurate information related to healthcare.

## Process:
### User Input:
The chatbot accepts user input in the form of text, allowing individuals to ask questions or seek information about specific diseases, symptoms, medications, or appointment booking.

### Chatterbot:
Using the Chatterbot module's NLP capabilities, the chatbot analyzes and processes the user's input to understand the intent and extract key information.

### Functionalities:

1) Disease and Symptoms Explanation:
The chatbot provides detailed explanations of various diseases and their associated symptoms, aiding users in understanding health conditions better.

2) Medication Information:
It offers information about medications, including dosage, usage instructions, and potential side effects.

3) Appointment Booking Assistance:
The chatbot assists users in scheduling appointments with healthcare professionals by providing available time slots or facilitating connections to appointment scheduling systems.

## Output:
The Healthcare Chatbot delivers informative and user-specific responses based on the input queries. It aims to educate individuals about healthcare-related topics, address concerns, and guide them towards appropriate actions, such as seeking medical attention or scheduling appointments. By offering accessible and accurate information, the chatbot empowers users to make informed decisions about their health and facilitates the process of seeking professional medical assistance when necessary.

![image](https://github.com/saadmdsabah/Skin-Cancer-Detection/assets/103499208/50ba38cb-1636-4464-8bbe-d2522425f0e0)
