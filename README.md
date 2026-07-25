# 🚀 Page Pulse

Page Pulse is a lightweight web application that audits any website URL and provides useful SEO and accessibility information.

## Features

- HTTP Status Code
- Response Time
- Page Title
- Meta Description
- H1 Count
- Images Missing Alt Text
- Approximate Word Count
- Error Handling

---

## Installation

Clone the repository

```bash
git clone https://github.com/Farsana2222/page-pulse.git
```

Go into the project

```bash
cd page-pulse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## API Contract

### Endpoint

```
POST /analyze
```

### Request

```json
{
    "url":"https://python.org"
}
```

### Success Response

```json
{
    "status":200,
    "response_time":230,
    "title":"Welcome to Python.org",
    "meta_description":"The official home of Python",
    "h1_count":5,
    "missing_alt":0,
    "word_count":1131
}
```

### Error Response

```json
{
    "error":"Invalid URL"
}
```

---

## Tests

Run tests using

```bash
pytest
```

---

## Design Decisions

### 1. Flask

Flask was chosen because it is lightweight, simple, and suitable for small REST APIs.

### 2. BeautifulSoup

BeautifulSoup makes HTML parsing reliable and easy for extracting titles, headings, metadata, and images.

### 3. Graceful Error Handling

Instead of crashing when a URL is invalid, times out, or is not HTML, the application returns meaningful error messages to improve reliability and user experience.

---

## Live Demo

https://page-pulse-bi20.onrender.com

---

Built for **Digital Heroes Training Task**