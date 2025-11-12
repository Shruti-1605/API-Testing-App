Overview

API Tester Pro provides a complete toolkit for testing RESTful APIs with ease. It supports multiple HTTP methods, automatic history tracking, response visualization, and performance metrics.

This application is ideal for developers, QA engineers, and anyone who wants to test and monitor APIs efficiently.

##Features

Professional UI: Modern card-based layout with Dark/Light themes.
HTTP Methods: Supports GET, POST, PUT, DELETE, and PATCH.
Request History: Automatically save and view previous requests.
Analytics Dashboard: Monitor performance metrics, success rates, and response times.
Response Charts: Visual graphs for analyzing API responses.
Quick Headers: Preset headers for JSON, XML, and Form Data.
Export Functionality: Save API responses and history for later reference.
Status Indicators: Color-coded visual cues for success, failure, or cleared requests.

##Installation
Clone the repository
git clone <repository-url>
cd api_tester
Install dependencies
pip install -r requirements.txt
Run the application
python main.py

##Usage
Enter the API endpoint in the input field.
Select the HTTP method: GET, POST, PUT, DELETE, PATCH.
Add headers manually or select Quick Headers presets.
Enter the request body for POST, PUT, or PATCH methods.
Click Send Request.
View the response panel for color-coded status and data.
Use the History, Dashboard, and Charts tabs for analytics.

Project Structure
api_tester/
├── main.py                 # Main application entry point
├── ui/
│   └── main_window.py      # UI components (modular design)
├── data/
│   └── history.json        # Request history storage
├── assets/
│   └── icons/              # Application icons
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Keyboard Shortcuts
Shortcut	Action
Ctrl + Enter / F5	Send Request
Ctrl + T	Toggle Dark/Light Theme
Ctrl + H	Show Request History
Ctrl + D	Show Analytics Dashboard

##Themes
Light Mode: Professional blue theme.
Dark Mode: Modern dark interface.
Toggle: Switch themes instantly with Ctrl + T.

##Analytics
Request History: View the last 50 API requests.
Response Charts: Visualize response times and trends.
Dashboard Metrics: Shows success rate, average response time, and total requests.
Status Indicators: Green (success), Red (failure), Yellow (cleared).

##Technical Details
Framework: CustomTkinter
Charts: Matplotlib
Data Storage: JSON files
HTTP Client: Requests library
UI Design: Card-based professional layout

##Requirements
Python 3.7+
CustomTkinter >= 5.2.0
Requests >= 2.31.0
Matplotlib >= 3.5.0
Future Enhancements
API Collections
Environment Variables
Request Templates
Export to Postman
API Documentation Generator
Performance Testing
Authentication Support

## 📸 Screenshots

### 🏠 Home Page
![Home Page](images/Screenshot%20%2866%29.png)

### ✅ Result Page
![Result Page](images/Screenshot%20%2868%29.png)

### 🤍 White Theme UI
![White Theme](images/Screenshot%20%2867%29.png)

### 📊 Charts
![Charts](images/Screenshot%20%2869%29.png)

### 🧭 Dashboard
![Dashboard](images/Screenshot%20%2870%29.png)

### 🕓 History API
![History API](images/Screenshot%20%2871%29.png)

### 💾 Save
![Save](images/Screenshot%20%2872%29.png)



## 🎬 Project Demo video 

[Watch Demo]([![Watch Demo](images/Screenshot%20(66).png)](Video/Screen%20Recording%202025-11-12%20122945.mp4)
##The project won’t open directly. You’ll have to go to **View Raw**, download it, and then you can watch the full video.##



