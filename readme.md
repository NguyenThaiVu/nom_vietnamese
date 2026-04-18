# 𡨸喃 (Hán-Nôm) to Vietnamese Converter

A specialized Streamlit application designed to bridge the gap between historical Hán-Nôm script and modern Vietnamese (Quốc ngữ). This tool allows users to select predefined Nôm character strings and view their modern equivalents.

## 🚀 Live Demo


## 🖼️ Application Overview
The application features a clean, user-friendly interface built with Streamlit. It includes a filtered selection system to ensure only valid, renderable Unicode characters are processed.

![Application Overview](assets/app_overview.png)
*Figure 1: The main interface showing the selection and translation section.*

## ⚙️ Architecture
The project follows a modular Python-based architecture, utilizing Streamlit for the frontend and a dictionary-based mapping system for character conversion.

![Project Architecture](assets/pipeline.pdf)
*Figure 2: Data flow from raw input through the filtering logic to the UI.*

## ✨ Features
- **Smart Filtering:** Automatically removes unsupported or broken Unicode characters (like 𫯲) to ensure a clean UI.
- **Predefined Inputs:** Prevents user error by providing a curated list of Nôm strings.
- **Instant Translation:** Real-time conversion from Hán-Nôm to modern Vietnamese.
- **Mobile Friendly:** Responsive design accessible via any web browser.

## 🛠️ Installation & Local Development
If you want to run this project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name