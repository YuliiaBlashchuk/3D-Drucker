# 3D Printer Order Management System

A web-based application for managing 3D printing orders and projects. The application provides an organized way to create print jobs, manage a queue, track printing time, and monitor the status of orders.

## Features

- **Create Projects:** Add new 3D printing projects.
- **Order Management:** Manage and organize incoming print orders.
- **Queue System:** Keep track of pending print jobs.
- **Printing Timer:** Track the estimated printing duration of projects.
- **Status Management:** Update the status of individual orders.
- **Completed Orders:** Manage and track finished printing jobs.

## Technologies Used

- **Python** – Backend programming
- **Flask** – Web framework
- **HTML** – Page structure
- **CSS** – Styling and user interface
- **JSON** – Data storage

## Project Structure

```text
3D-Drucker/
│
├── templates/
│   └── index.html
│
├── backend.py
├── main.py
├── tracker.json
├── users.json
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YuliiaBlashchuk/3D-Drucker.git
```

### 2. Navigate to the project directory

```bash
cd 3D-Drucker
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install Flask
```

### 5. Start the application

```bash
python main.py
```

Open your browser and navigate to the local address displayed in the terminal (usually `http://127.0.0.1:5000`).

## Data Storage

The application uses JSON files for simple data persistence:

- `tracker.json` – Stores project and order information.
- `users.json` – Stores user information and access permissions.

## Future Improvements

Potential improvements for future versions include:

- Database integration (e.g. SQLite or MySQL).
- User authentication and role management.
- Improved dashboard with statistics.
- Enhanced order tracking and notifications.

## Author

**Yuliia Blashchuk**

Developed as a Python and Flask project to practice backend development, web technologies, and application logic.
