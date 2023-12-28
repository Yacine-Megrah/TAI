import cv2

# Load query image
query_img = cv2.imread("query_fruit.jpg", 0)

# Load 100 comparison images (replace with your actual image loading)
comparison_images = [...]  # Load 100 images

# Pre-compute SIFT descriptors for all images
all_descriptors = []
for img in comparison_images:
    kp, des = sift.detectAndCompute(img, None)
    all_descriptors.append(des)


query_kp, query_des = sift.detectAndCompute(query_img, None)

# Store matching results
matching_results = []
for i, des in enumerate(all_descriptors):
    matches = bf.knnMatch(query_des, des, k=2)
    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
    matching_results.append((len(good_matches), i))  # Store (num_matches, image_index)

# Find the image with the most good matches
most_similar_index, _ = max(matching_results)
most_similar_image = comparison_images[most_similar_index]

print("Most similar image:", most_similar_image)
import cv2

# Load query image
query_img = cv2.imread("query_fruit.jpg", 0)

# Load 100 comparison images (replace with your actual image loading)
comparison_images = [...]  # Load 100 images

# Pre-compute SIFT descriptors for all images
all_descriptors = []
for img in comparison_images:
    kp, des = sift.detectAndCompute(img, None)
    all_descriptors.append(des)


query_kp, query_des = sift.detectAndCompute(query_img, None)

# Store matching results
matching_results = []
for i, des in enumerate(all_descriptors):
    matches = bf.knnMatch(query_des, des, k=2)
    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
    matching_results.append((len(good_matches), i))  # Store (num_matches, image_index)

# Find the image with the most good matches
most_similar_index, _ = max(matching_results)
most_similar_image = comparison_images[most_similar_index]

print("Most similar image:", most_similar_image)
