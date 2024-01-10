import cv2
import datetime
import requests
import numpy as np
#connecting to openai
from openai import OpenAI
import os

client = OpenAI(api_key = os.environ.get('API_KEY'))
#generating an image

response = client.images.generate(
  model="dall-e-3",
  prompt= """
create a beautiful and visualy appealing certificate background.
The background should have enough space for the names of the participant, the date,
 and the logo of the certificate.
 The certificate background should be an official background.
 Where the name will be write the word name and where the date will be write the word date.

""",
  size="1024x1024",
  quality="standard",
  n=1,
)

#getting the image url
image_url = response.data[0].url
print(image_url)

#Getting a variety of images based on the first image
response = client.images.create_variation(
  image=open(r"c:\Users\User\Documents\Data Science Project 1\Machine learning\10academy week5\image_generation\cert.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url1 = response.data[0].url
print(image_url1)



# Load the certificate image
image_path = r"c:\Users\User\Documents\Data Science Project 1\Machine learning\10academy week5\image_generation\cert1.png"
certificate = cv2.imread(image_path)

# Define the name and date
name = "Yvvon Majala"
current_date = datetime.date.today().strftime("%Y-%m-%d")

# Set font and text color
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (0, 0, 0)  # Black

# Add name
cv2.putText(certificate, f"Name: {name}", (100, 200), font, 1, text_color, 2, cv2.LINE_AA)

# Add date
cv2.putText(certificate, f"Date: {current_date}", (100, 250), font, 1, text_color, 2, cv2.LINE_AA)

# Save or display the modified certificate
cv2.imwrite("path/to/your/output_certificate.png", certificate)
cv2.imshow('Modified Certificate', certificate)
cv2.waitKey(0)
cv2.destroyAllWindows()
