from flask import Flask, request, send_file, render_template_string
import qrcode
import io

app = Flask(__name__)

# HTML form template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px;background-color: #f9f9f9; }
        input, button { padding: 10px; margin: 5px; }
        img { margin-top: 20px; }
        button { cursor: pointer; }
        h2 { color: #333; } 
        body { background-color: #f4f4f4; }
        
    </style>
</head>
<body>
    <h2>QR Code Generator</h2>
    <form method="POST" action="/generate">
        <label>Enter text or URL to generate QR Code:</label>
        <input type="text" name="data" placeholder="Enter text or URL" required><br>
        <label>Enter filename(without .png):</label>
        <input type="text" name="filename" placeholder="Filename (optional)"><br>
        <button type="submit">Generate QR Code</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/generate", methods=["POST"])
def generate_qr():
    data = request.form["data"].strip()
    filename = request.form["filename"].strip()

    if not filename:
        filename = "qrcode.png"
    else:
        # Ensure the filename ends with .png
        if not filename.lower().endswith(".png"):
            filename += ".png"

    # Generate QR code (your same logic)
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")

    # Save to in-memory buffer
    buf = io.BytesIO()
    image.save(buf)
    buf.seek(0)

    # Send file as attachment
    return send_file(
        buf,
        mimetype="image/png",
        as_attachment=True,
        download_name=filename
    )

if __name__ == "__main__":
    app.run(debug=True)
