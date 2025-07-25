import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

# loding the image
image_path = "output_2_cropped.png"  # Replace with your uploaded file name if needed
image = cv2.imread(image_path)
image = cv2.resize(image, (512, 512))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# load sam model
sam_checkpoint = "model_weights/sam_vit_h_4b8939.pth"
model_type = "vit_h"
# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device)

mask_generator = SamAutomaticMaskGenerator(
    model=sam,
    points_per_side=32,
    pred_iou_thresh=0.88,
    stability_score_thresh=0.92,
    crop_n_layers=1,
    min_mask_region_area=500 
)
masks = mask_generator.generate(image_rgb)

def classify_region(mask, image_rgb):
    region_pixels = image_rgb[mask]
    avg_color = np.mean(region_pixels, axis=0)  # [R, G, B]
    std_color = np.std(region_pixels, axis=0)
    r, g, b = avg_color
    std_dev = np.mean(std_color)
    
    if b > 130 and r < 100 and g < 120:
        return "Water"

    elif g > 120 and r < 100 and b < 100 and std_dev < 45:
        return "Green Area"

    elif (r > 170 and g > 150 and b > 130) or (r > 140 and abs(r - g) < 25 and abs(g - b) < 25):
        return "Bare Land"

    elif 100 < r < 180 and 100 < g < 180 and 100 < b < 180 and std_dev < 30:
        return "Road"

    elif r > 130 and r - g > 20 and r - b > 20:
        return "Building"

    elif std_dev > 60:
        return "Waste"

    else:
        return None  


segmented_classes = []
for mask_info in masks:
    mask = mask_info["segmentation"]
    label = classify_region(mask, image_rgb)
    if label:  # Only keep meaningful classes
        segmented_classes.append((mask, label))

colors = {
    "Building": (194, 115, 92),       # #c2735c
    "Water": (70, 92, 147),           # #465c93
    "Green Area": (61, 84, 79),       # #3d544f
    "Waste": (128, 0, 128),           # Purple
    "Bare Land": (117, 112, 104),     # #757068
    "Road": (183, 177, 174),          # #b7b1ae
}

legend_elements = [Patch(facecolor=np.array(c) / 255, label=l) for l, c in colors.items()]
overlay = image_rgb.copy()

for mask, label in segmented_classes:
    color = np.array(colors[label])
    overlay[mask] = overlay[mask] * 0.3 + color * 0.7

plt.figure(figsize=(12, 12))
plt.imshow(overlay.astype(np.uint8))
plt.title("SAM-based Urban Feature Segmentation (Kathmandu)", fontsize=14)
plt.axis('off')
plt.legend(handles=legend_elements, loc='lower right')
plt.tight_layout()
plt.show()
