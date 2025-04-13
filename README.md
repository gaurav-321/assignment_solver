# Assignment Solver in Python

An assignment-solving program that converts text input into images that look handwritten.

## ✨ Description
This project aims to simplify the process of creating visually appealing assignments by converting plain text into high-quality, handwritten-style images. It supports custom fonts and notebook-style backgrounds, making it ideal for educational materials or creative projects.

## 🚀 Features
- Convert plain text to handwritten-style images
- Supports custom fonts and notebook-style backgrounds
- Format text with simple symbols:
  - `#` for black-colored lines
  - `##` for centered, black-colored headings
- Works with editable `.txt` input file

## 🛠️ Installation
Make sure Python 3 and `pip` are installed, then run:

```bash
pip3 install -r requirements.txt
```

## 📦 Usage
1. Open `input/document.txt`.
2. Write or paste your content using these rules:
   - Lines starting with `#` are black-colored
   - Lines starting with `##` are centered and black
   - All other lines are normal text
3. Save the file.
4. Run the program with:

```bash
python3 main.py
```

Images will be saved in the `output/` directory.

## 🔧 Configuration
The project uses OpenCV trackbars to configure spacing, font size, and more. You can adjust these settings during runtime by running the program.

## 🧳 Output Example

| Sample Outputs |
|----------------|
| ![First Image](output/0.png?raw=true) |
| ![Second Image](output/1.png?raw=true) |
| ![Third Image](output/2.png?raw=true) |

## 🔎 How It Works
The tool uses OpenCV and PIL to:
- Analyze a notebook-style background image
- Detect line positions automatically
- Overlay handwritten-style text using random fonts for a realistic feel

It supports configuration for spacing, font size, and more using OpenCV trackbars.

## 🌟 Contributing & Credits
This project was created as part of an open-source contribution effort.
If you find this project useful or use it in your work, kindly credit [Ordinary Pythoneer](https://github.com/Ordinary-Pythoneer).

[![Demo Video](https://img.youtube.com/vi/fRjA7gJhdGw/maxresdefault.jpg)](https://youtu.be/fRjA7gJhdGw)

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using Assignment Solver in Python! 😊