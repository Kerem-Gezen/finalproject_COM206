# README:


# Digital Piggy Bank


### This README document provides an overview and setup instructions for the Digital Piggy Bank application. It is a desktop-based budget and piggy bank tool designed to track personal savings, allowing users to deposit and withdraw funds while maintaining real-time balance updates.


### This application is written purely in Python and utilizes the Qt framework (specifically PySide6) for its graphical user interface.


### Project Structure()
```text
finalproject_COM206/
├── .gitignore             # Filters unnecessary system files
├── README.md              # Project documentation
├── requirements.txt       # Required Python libraries (PySide6)
├── main.py                # The main code file of the application
├── pyproject.toml         # Qt project configuration file
├── Main.qml               # Main QML file for Qt Quick UI layout
└── qmldir                 # QML module configuration file
```


### Prerequisites & Requirements
To use and run this application on your local machine, the following software and libraries are required:


### Python 3.x (Python 3.8 or newer is recommended)


### PySide6 (The official Python module for Qt)


### Recommended IDEs


You can run or edit this project using any standard Integrated Development Environment (IDE). Popular choices include:

### Visual Studio Code (VS Code)

### PyCharm

### Spyder

### QtCreator

### Installation & Usage
Verify that Python is installed on your system by running python --version in your terminal or command prompt.

Install the required Qt framework library by running the following command:

### Bash
pip install PySide6
Execute the main Python script to launch the application:

### Bash
python main.py
Technologies Used
Core Language: Python 3

GUI Library: PySide6 (Qt for Python)

Methodologies & Approaches
Object-Oriented Programming (OOP): The application logic and UI components are encapsulated within class structures for code maintainability and scalability.

Event-Driven Programming: Utilizes Qt's Signal and Slot mechanisms to handle user interactions seamlessly.

Input Validation: Implements QIntValidator at the UI level to restrict user input to positive integers, ensuring data integrity and preventing runtime crash errors.

Dynamic Layout Management: Employs QVBoxLayout and QHBoxLayout to create a responsive, resolution-independent user interface that adapts to window resizing.
