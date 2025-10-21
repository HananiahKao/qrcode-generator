# QR Code Generator

A tiny Python script to generate QR codes from URLs or text.

## Requirements
- Python 3.8+
- `qrcode` (install via `pip install qrcode[pil]`)

## Usage
```
python3 generate.py --type {url,text} "content"
```
Examples:
```
python3 generate.py --type url "https://example.com"
python3 generate.py --type text "Hello QR"
```

The script outputs a PNG file named `output.png` in the working directory.

## Notes
- `--type url` performs light normalization (trims whitespace). Both types are encoded identically.
- `output.png` is ignored by Git (see `.gitignore`).
