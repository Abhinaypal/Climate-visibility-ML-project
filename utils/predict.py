import pickle
import numpy as np

# Load models
fog_model = pickle.load(open("models/fog_model.pkl", "rb"))
vis_model = pickle.load(open("models/visibility_model.pkl", "rb"))
features = pickle.load(open("models/features.pkl", "rb"))

def predict_all(user_input):

    input_array = []
    for feature in features:
        input_array.append(user_input.get(feature, 0))

    input_array = [input_array]

    # Fog prediction
    fog_prob = fog_model.predict_proba(input_array)[0][1]

    # Visibility prediction
    visibility = vis_model.predict(input_array)[0]

    # Fog message
    if fog_prob > 0.7:
        fog_msg = f"🔴 RED ALERT: High fog ({fog_prob:.2f})"
    elif fog_prob > 0.4:
        fog_msg = f"🟡 YELLOW ALERT: Moderate fog ({fog_prob:.2f})"
    else:
        fog_msg = f"🟢 CLEAR: Low fog ({fog_prob:.2f})"

    return fog_msg, visibility