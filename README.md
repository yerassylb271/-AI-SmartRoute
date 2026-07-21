# AI SmartRoute

A Smart City Navigation Assistant that helps users compare transportation methods and receive an AI-powered recommendation based on travel time, cost, environmental impact, and weather conditions.

Developed as an MVP for the **TechVision Hackathon**.

---

## Overview

AI SmartRoute simplifies urban navigation by allowing users to search for locations or select them directly on an interactive map. The application compares multiple transportation methods and recommends the most suitable option using AI analysis.

The system combines modern routing services, weather information, and sustainability metrics to provide a smarter travel experience.

---

## Features

- Search locations by name (e.g. "Mega Silk Way")
- Select locations directly on the map
- Support for:
  - Car
  - Bicycle
  - Walking
- Automatic identification of:
  - Fastest route
  - Cheapest route
  - Most Eco-Friendly route
- AI-generated travel recommendation
- Current weather information for the destination
- Interactive map powered by Leaflet
- Responsive user interface
- GraphHopper route visualization

---

## Tech Stack

### Backend

- Python 3
- Flask
- Flask-CORS
- Requests
- Gunicorn

### Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)
- Leaflet.js

### APIs

- GraphHopper Routing API
- OpenStreetMap Nominatim API
- OpenWeather API
- Groq API

---

## Project Structure

```
AI-SmartRoute/
│
├── app.py
├── route_service.py
├── ai.py
├── weather.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    ├── js/
    │   └── script.js
    │
    └── images/
        └── eco-badge.png
```

---

## System Architecture

```
                 User
                   │
                   ▼
      HTML / CSS / JavaScript
                   │
             POST /build-route
                   │
                   ▼
              Flask Backend
                   │
     ┌─────────────┼─────────────┐
     │             │             │
     ▼             ▼             ▼
 Nominatim   GraphHopper   OpenWeather
 Geocoding      Routing         API
     │
     ▼
  Groq AI Recommendation
                   │
                   ▼
             JSON Response
                   │
                   ▼
     Leaflet Map + Route Cards
```

---

## Route Evaluation

Every available route is evaluated using:

- Travel time
- Distance
- Estimated travel cost
- CO₂ emissions

The application automatically determines:

- Fastest route
- Cheapest route
- Most Eco-Friendly route

An AI Smart Score is calculated for each transportation method, and the highest-rated option is highlighted as the recommended route.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-SmartRoute.git
```

Move into the project folder:

```bash
cd AI-SmartRoute
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
GRAPHHOPPER_API_KEY=your_graphhopper_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the development server:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Deployment

The application can be deployed using:

- Render
- Railway
- Fly.io
- Heroku
- VPS with Gunicorn

Example start command:

```bash
gunicorn app:app
```

---

## API Endpoint

### POST `/build-route`

Example request:

```json
{
  "start": "Mega Silk Way",
  "destination": "Capital Park"
}
```

Example response:

```json
{
  "success": true,
  "weather": {
    "temperature": 24,
    "condition": "Clear"
  },
  "routes": [],
  "ai": "The bicycle route is recommended because it offers the best balance between travel time, cost, and environmental impact."
}
```

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Flask | Backend framework |
| Leaflet | Interactive maps |
| GraphHopper | Route calculation |
| Nominatim | Location search |
| OpenWeather | Weather information |
| Groq | AI recommendation |
| HTML5 | Interface structure |
| CSS3 | Styling |
| JavaScript | Client-side functionality |
| Gunicorn | Production server |

---

## Future Improvements

- Public transportation routes
- Live traffic integration
- User authentication
- Favorite destinations
- Route history
- Real-time ETA updates
- Carbon footprint analytics
- Multi-language support
- Mobile application
- Offline route caching

---

## Authors

Developed by **Four Horsemen** for the **TechVision Hackathon**.

### Team Contributions

- Backend development
- Frontend development
- AI integration
- Route optimization
- UI/UX design
- Deployment and testing

---

## License

This project was created for educational and demonstration purposes as part of the **TechVision Hackathon**.
