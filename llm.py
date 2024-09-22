from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

def SKClassification(image_path):
    # Step 1: Download the processor and model
    processor = AutoImageProcessor.from_pretrained("NeuronZero/SkinCancerClassifier")
    model = AutoModelForImageClassification.from_pretrained("NeuronZero/SkinCancerClassifier")

    # Step 2: Save the processor and model locally
    processor.save_pretrained("local_processor_directory")
    model.save_pretrained("local_model_directory")

    # Step 3: Load the processor and model locally
    processor = AutoImageProcessor.from_pretrained("local_processor_directory")
    model = AutoModelForImageClassification.from_pretrained("local_model_directory")

    # Step 4: Use the processor and model
    # Example local file path (replace this with the path to your image file)

    # Load the image
    image = Image.open(image_path)

    # Process the image
    inputs = processor(images=image, return_tensors="pt")

    # Get predictions
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    # MEL: Melanoma
    # NV: Nevus (also known as a mole)
    # BKL: Benign Keratosis-like Lesions
    # BCC: Basal Cell Carcinoma
    # SCC: Squamous Cell Carcinoma

    # Print the predicted class
    prediction = model.config.id2label[predicted_class_idx]
    result = None
    if(prediction == "MEL"):
        result = "Melanoma";
    elif(prediction == "NV"):
        result = "Nevus (also known as a mole)"
    elif(prediction == "BKL"):
        result = "Benign Keratosis-like Lesions"
    elif(prediction == "BCC"):
        result = "Basal Cell Carcinoma"
    else:
        result = "Squamous Cell Carcinoma"
    return result