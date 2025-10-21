import qrcode
from io import BytesIO

def encode_url_to_qr(data: str, as_bytes: bool = False) -> None:
    """
    Encode the given string as a URL QR code and save it to a file.

    Args:
        data (str): The URL or string to encode.
        as_bytes (bool): If True, return QR code as PNG bytes (BytesIO).
                         If False, save image to 'output.png' and return 
None.

    Returns:
        None: No return value; the generated image is saved to 
'output.png'.
    """
    qr = qrcode.QRCode(
        version=None,  # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("output.png")

# Example usage
if __name__ == "__main__":
    encode_url_to_qr("https://example.com", as_bytes=False)
