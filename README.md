# NoFakeZone - Fake Profile Detector

## Overview
NoFakeZone is an AI-powered web application designed to detect fake profiles instantly. It utilizes machine learning algorithms to analyze user data and classify profiles as real or fake. The system aims to help users avoid online scams, impersonators, and fraudulent accounts.

## Features
- **AI-driven profile verification** - Uses trained machine learning models to classify profiles.
- **User-friendly interface** - Simple and clean UI for easy navigation.
- **Responsive design** - Optimized for both desktop and mobile devices.
- **Secure backend** - Flask-based API for handling requests.
- **Fast and efficient processing** - Quick analysis and results.
- **Multilingual support** - Supports multiple languages for wider accessibility.

## Tech Stack
- **Frontend:** HTML, CSS (TailwindCSS)
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn (for fake profile classification)
- **Hosting:** Planned for AWS/GCP deployment in future updates

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask
- Scikit-learn
- Virtual environment (venv or conda recommended)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/NoFakeZone.git
   cd NoFakeZone
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000/`.

## Project Structure
```
NoFakeZone/
│── data/
│── models/
│── scripts/
│   ├── preprocess.py
│   ├── test.py
│── static/
│   ├── css/
│   │   ├── styles.css
│   ├── images/
│   │   ├── about_bg.jpg
│   │   ├── background.jpg
│   │   ├── bg.png
│   │   ├── fake_user.gif
│   │   ├── icon.png
│   │   ├── real_user.gif
│── templates/
│   ├── index.html
│   ├── result.html
│   ├── about.html
│── app.py
│── requirements.txt
│── README.md
```

## Usage
1. Navigate to the homepage (`index.html`).
2. Enter profile details including follower count, friends count, and language.
3. Submit the form to check if the profile is fake or real.
4. View results on the `result.html` page with classification details.

## API Endpoints
- **POST `/predict`** - Accepts JSON input with profile details and returns classification results.
- **GET `/about`** - Provides information about the project and its creators.

## Contributing
Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch (`feature-branch` or `bugfix-branch`).
- Make your changes and test them.
- Submit a pull request with a clear description of your changes.

## Future Enhancements
- **Blockchain integration** - For decentralized profile verification.
- **Advanced ML models** - Incorporating deep learning for better accuracy.
- **Deployment on AWS/GCP** - Making the application accessible worldwide.
- **Integration with social media platforms** - To analyze real-time profiles.
- **Improved UI/UX** - More intuitive and interactive design.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact
For any questions or collaboration requests, feel free to reach out at `pathmhajam@gmail.com`. You can also open an issue in the repository.

---
Made with ❤️ by **SPECTERS**

