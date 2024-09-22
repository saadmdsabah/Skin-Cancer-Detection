def ultimateResult(cnn_probs, fastai_probs, mobilenet_probs):
    # Weights based on accuracy
    weights = [cnn_probs.cor, fastai_probs.cor, mobilenet_probs.cor]

    # Probabilities from each model
    probs = [cnn_probs.probs, fastai_probs.probs, mobilenet_probs.probs]

    # Calculate weighted sum of probabilities for each class
    weighted_probs = [0, 0]
    for i in range(len(probs)):
        for j in range(len(weighted_probs)):
            weighted_probs[j] += weights[i] * probs[i][j]

    # Determine final classification based on weighted probabilities
    final_class = weighted_probs.index(max(weighted_probs))

    # Print the final predicted class based on [cancer, non_cancer] format
    if final_class == 0:
        return "Cancer"
    return "NonCancer"