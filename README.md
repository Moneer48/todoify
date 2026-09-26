# ToDoify

A task management web application built to help users manage their daily tasks, set priorities, and track progress effectively.

🎥 [**Watch the Video Demo**](https://youtu.be/pOmRGbHebSw?utm_source=gemini)

## Overview

ToDoify is designed for individuals who want to enhance their productivity through organized task management. Built with **Flask** and **SQLite**, it provides an intuitive web interface for managing task lifecycles, due dates, priority flagging, and user accounts.

## Features

* **Minimalist Design:** Clean interface built with Bootstrap and custom CSS.

* **User Authentication:** Secure registration, login, logout, password updates, and account deletion.

* **Task Management:** Create tasks with title, description, due date, and due time. View tasks separated into *Pending* and *Completed* views.

* **Priority & Starred Tasks:** Flag crucial tasks to display them on a dedicated *Important Tasks* page.

* **Time Zone Support:** Users select their region during registration so creation dates match their local time zone.

* **Completion Tracking:** Easily toggle tasks between complete and incomplete states to track progress.

## Tech Stack

* **Backend:** Python, Flask, Jinja2

* **Database:** SQLite3

* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5

## Database & Architecture

The application manages two core SQLite tables:

* `users`: Stores user IDs, usernames, hashed passwords, and local time zones.

* `info`: Stores individual tasks linked by user ID, including titles, descriptions, creation timestamps, due dates, completion status, and star flags.

Routes are secured using session-based authentication helpers (`login_required`), ensuring user privacy and data separation.

## Setup & Running Locally

1. Clone the repository:

   ```
   git clone https://github.com/Moneer48/todoify.git
   cd todoify
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   flask run
   ```

4. Open `http://127.0.0.1:5000` in your web browser.
