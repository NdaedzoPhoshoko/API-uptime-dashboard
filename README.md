# API Uptime Dashboard

This project is a simple dashboard to monitor the uptime of an API. It displays the API uptime in minutes and shows a progress bar for a 20-minute cycle. If the API is down, it displays an error message.

## Features

- Displays API uptime in minutes.
- Shows a progress bar for a 20-minute cycle.
- Displays a success message when the API is up.
- Displays an error message when the API is down.

## Requirements

- Python 3.x
- Flask
- Requests

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/NdaedzoPhoshoko/API-uptime-dashboard.git
    cd api-uptime-dashboard
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install Flask
    pip install requests
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    python api.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to view the dashboard.

## Project Structure

- [api.py]: The main Flask application file that serves the dashboard and provides the API endpoint for uptime.
- [index.html]: The HTML template for the dashboard.
- [styles.css]: The CSS file for styling the dashboard.

## API Endpoint

- `/api/uptime`: Returns the API uptime in minutes and the progress percentage for the 20-minute cycle.

## Example Response

```json
{
    "minutes_online": 123,
    "progress": 15%
}