import matplotlib.pyplot as plt
import numpy as np

# Function to generate random Chernoff face features
def generate_chernoff_face():
    # Define the range and weights for each facial feature
    ranges = {
        "face_width": (0.5, 1.5, 0.3),
        "face_height": (0.8, 1.2, 0.2),
        "eye_size": (0.05, 0.25, 0.05),
        "eye_slant": (-0.3, 0.3, 0.1),
        "eyebrow_slant": (-0.3, 0.3, 0.1),
        "eyebrow_thickness": (0.01, 0.1, 0.02),
        "nose_length": (0.3, 0.7, 0.1),
        "nose_width": (0.1, 0.3, 0.05),
        "mouth_width": (0.3, 0.7, 0.1),
        "mouth_thickness": (0.05, 0.15, 0.02)
    }
    
    # Generate random values for each facial feature
    face = {}
    for feature, (min_value, max_value, step) in ranges.items():
        face[feature] = np.random.choice(np.arange(min_value, max_value + step, step))
    
    return face

# Generate multiple Chernoff faces
num_faces = 5

plt.figure(figsize=(10, 2))

for i in range(num_faces):
    face = generate_chernoff_face()
    
    # Plot each facial feature using the generated values
    plt.subplot(1, num_faces, i + 1)
    plt.axis('off')
    plt.title("Face {}".format(i + 1))
    
    plt.fill_between([0, 1], [0, 0], [face['face_height'], face['face_height']], color='lightgray')
    
    plt.plot([0.4, 0.5], [0.4, 0.6], linewidth=face['eye_size']*10, color='black')
    plt.plot([0.6, 0.5], [0.4, 0.6], linewidth=face['eye_size']*10, color='black')
    
    plt.plot([0.3, 0.4], [0.7, 0.7+face['eyebrow_thickness']], linewidth=face['eyebrow_thickness']*10, color='black')
    plt.plot([0.6, 0.7], [0.7, 0.7+face['eyebrow_thickness']], linewidth=face['eyebrow_thickness']*10, color='black')
    
    plt.plot([0.5, 0.5], [0.5, 0.5+face['nose_length']], linewidth=face['nose_width']*10, color='black')
    
    plt.plot([0.3, 0.7], [0.3, 0.3], linewidth=face['mouth_thickness']*10, color='black')
    plt.plot([0.3, 0.3], [0.3, 0.3+face['mouth_width']], linewidth=face['mouth_thickness']*10, color='black')
    plt.plot([0.7, 0.7], [0.3, 0.3+face['mouth_width']], linewidth=face['mouth_thickness']*10, color='black')
    
plt.tight_layout()
plt.show()

