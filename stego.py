import cv2
import os

# Get user input FIRST
msg = input("Enter secret message: ")
password = input("Enter a passcode: ").strip()

# Load the image AFTER user input
img = cv2.imread("image1.jpg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Image not found. Make sure 'image1.jpg' is in the same folder.")
    exit()

# Now, display the original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Character mappings for encoding & decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encode the message into the image
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save and show encrypted image
cv2.imwrite("encryptedImage.jpg", img)
cv2.imshow("Encrypted Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Decryption process
message = ""
n, m, z = 0, 0, 0

# Get password for decryption
pas = input("Enter passcode for Decryption: ").strip()

if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("\nDecrypted message:", message)
else:
    print("\nERROR: Incorrect passcode! Unauthorized access.")
