# Maths With Computer Vision

Maths With Computer Vision is a **computer vision–powered** project that helps students understand and interact with mathematical expressions directly from images or camera input.

---

## Features

- Detect and localize mathematical expressions from images or video frames using computer vision and OCR.
- Clean and parse recognized expressions into a symbolic math representation for further processing.
- Evaluate expressions and optionally generate **step-by-step explanations** using a math engine (e.g., SymPy).
- Draw visual overlays (bounding boxes, LaTeX rendering, plots, etc.) on top of the original image or live webcam feed.
- Modular design so different OCR, detection, and solver backends can be swapped easily.

---

## Tech Stack

- **Language:** Python
- **Computer Vision:** OpenCV (image processing, drawing overlays)
- **OCR / Detection:** Tesseract, EasyOCR, or a deep learning detector (e.g., YOLO)
- **Math Engine:** SymPy or a similar CAS for parsing and solving expressions
- **Visualization:** Matplotlib and OpenCV for displaying results

> Update this section to match your actual `requirements.txt` and code imports.

---

## Project Structure

Example structure (edit to match your repository):

```
Maths-WIth-Computer-Vision/
├── data/              # Sample images / videos
├── models/            # Trained weights / detection models
├── src/               # Core source code
│   ├── detection/     # CV & OCR pipeline
│   ├── parsing/       # Expression cleaning & parsing
│   ├── solving/       # Math solving / explanation
│   └── utils/         # Helper functions, configs, I/O
├── notebooks/         # Experiments and prototypes
├── requirements.txt   # Python dependencies
└── main.py            # Entry-point script
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/atharvamavle/Maths-WIth-Computer-Vision.git
cd Maths-WIth-Computer-Vision
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install OCR / CV Dependencies

- Install **Tesseract OCR** following your OS-specific instructions.
- Ensure the `tesseract` executable is available in your system `PATH`, or configure its path in the project settings.
- (Optional) Install CUDA and GPU drivers if using deep learning–based detectors.

---

## Usage

> Rename flags and arguments to match your actual CLI implementation.

### Run on a Single Image

```bash
python main.py --image path/to/image.png --output outputs/result.png
```

### Run on a Folder of Images

```bash
python main.py --input_dir data/ --output_dir outputs/
```

### Run in Webcam / Live Mode

```bash
python main.py --webcam
```

### Expected Behavior

1. The script loads the image or video stream.
2. Mathematical expressions are detected, recognized, and parsed.
3. Solutions and (optionally) step-by-step explanations are printed to the console and/or rendered back onto the image or video frame.

---

## Roadmap

Planned or potential improvements:

- Improve accuracy on handwritten equations using specialized training data.
- Add support for advanced topics such as calculus, linear algebra, and geometry diagrams.
- Build a simple web UI (Streamlit or Gradio) to make the tool more accessible to students and teachers.
- Export annotated outputs (PDFs, images) containing both the original problem and the worked solution.

---

## Contributing

Contributions are welcome!

- Open an issue for bugs, questions, or feature requests.
- Fork the repository and create a pull request with clear commit messages and a short description of your changes.

---

## License

Add your project license here (e.g., MIT, Apache 2.0).

