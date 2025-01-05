# Face Recognition Attendance Management System

## Overview

This project is a **Face Recognition Attendance Management System** developed using Python and OpenCV. It leverages facial recognition technology to record and manage attendance efficiently and automatically. This system replaces traditional methods of manual attendance marking, improving both accuracy and time efficiency.

## Features
- **Face Detection and Recognition:** Detects and identifies registered faces in real-time using OpenCV.
- **Database Integration:** Stores attendance records in a database for easy access and management.
- **Real-Time Attendance Marking:** Automatically marks attendance when a registered face is recognized.
- **User-Friendly Interface:** Provides an intuitive interface for registration and attendance management.
- **Face Registration:** Allows new users to register their faces.
- **Attendance Reports:** Generates and stores attendance logs for review.

## Requirements

### Dependencies
To run this project, ensure you have the following installed:
- Python 3.8 or later
- OpenCV
- NumPy
- Pandas
- SQLite3 (for database management)

Install dependencies using:
```bash
pip install opencv-python numpy pandas
```

## Setup and Usage

### Step 1: Clone the Repository
Clone this project repository to your local machine:
```bash
git clone <repository_url>
```

### Step 2: Navigate to the Project Directory
```bash
cd face-recognition-attendance
```

### Step 3: Register Faces
Run the face registration script to add new users:
```bash
python register_face.py
```
Follow the on-screen instructions to capture and store face data.

### Step 4: Start Attendance System
Launch the attendance system:
```bash
python attendance_system.py
```
The system will activate the webcam and begin recognizing faces in real time. Attendance will be marked for registered users.

### Step 5: View Attendance Logs
View or export attendance logs stored in the database using the following script:
```bash
python view_logs.py
```

## Project Structure

- `register_face.py`: Handles face registration and data storage.
- `attendance_system.py`: Main script for real-time face recognition and attendance marking.
- `view_logs.py`: Allows users to view or export attendance logs.
- `database/`: Contains SQLite database files.
- `assets/`: Stores face data and related assets.
- `README.md`: Project documentation.

## Notes
- Ensure proper lighting conditions for optimal face recognition.
- Use high-resolution images for better accuracy during face registration.
- Maintain the integrity of the `database/` and `assets/` folders for consistent functionality.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- OpenCV for providing robust computer vision capabilities.
- The Python community for powerful libraries like NumPy and Pandas.

---

Enjoy using the Face Recognition Attendance Management System!
