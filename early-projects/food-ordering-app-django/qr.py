import qrcode

# URL for the QR code (change to production URL when ready)
url = "http://127.0.0.1:8000"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # pixel size of each box
    border=4,  # border boxes
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save to file
img.save("qr.png")
print("QR code generated successfully!")
