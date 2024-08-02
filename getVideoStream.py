import cv2
from urllib.request import urlopen
import numpy as np

# Replace with your ESP32-CAM IP address
url = 'http://<YOURIP>/capture'

while True:
    try:
        # Open a connection to the ESP32-CAM
        img_resp = urlopen(url)

        # Read the image data
        img_data = img_resp.read()

        # Convert the image data to a numpy array
        img_np = np.frombuffer(img_data, dtype=np.uint8)

        # Decode the image
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

        # Display the image
        cv2.imshow("Camera", img)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"Error: {e}")

cv2.destroyAllWindows()
