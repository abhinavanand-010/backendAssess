# Multilingual FAQ System (Backend intern Asssessment Solution)

A Django-based multilingual FAQ system with REST API support, caching using Redis, and automatic translations via Google Translate.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Admin Panel](#admin-panel)
   - [API Endpoints](#api-endpoints)
4. [Caching](#caching)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Multilingual Support**: FAQs can be translated into multiple languages (e.g., Hindi, Bengali).
- **WYSIWYG Editor**: Use `django-ckeditor` for rich text formatting in answers.
- **REST API**: Fetch FAQs in different languages using query parameters.
- **Caching**: Improve performance with Redis caching.
- **Automatic Translations**: Use Google Translate API to automatically translate FAQs during creation.
- **Admin Panel**: Manage FAQs through a user-friendly Django admin interface.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Docker Desktop (for Redis and containerization)
- Git (optional, for cloning the repository)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/multilingual-faq.git
   cd multilingual-faq

   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate

   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

   ```

4. **Run Redis Using Docker**

   ```bash
   docker run --name redis-container -p 6379:6379 -d redis

   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate

   ```

6. **Create Superuser**(username: admin, password: admin)

   ```bash
   python manage.py createsuperuser

   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

**_ Usage _**
** Admin Panel **

1. Access the admin panel at http://127.0.0.1:8000/admin.
2. Log in with your superuser credentials.
3. Add FAQs under the "FAQs" section.

**_ API Endpoints _**

1.  **Default Language (English) :**

````bash
curl http://127.0.0.1:8000/api/faqs/

2.  **Hindi**
 ```bash
 curl http://127.0.0.1:8000/api/faqs/?lang=hi

3.  ** Bengali**
 ```bash
 curl http://127.0.0.1:8000/api/faqs/?lang=bn

** Response Example **
```json
[
  {
      "id": 1,
      "question": "What is Python?",
      "answer": "Python is a programming language."
  },
  {
      "id": 2,
      "question": "क्या है पायथन?",
      "answer": "पायथन एक प्रोग्रामिंग भाषा है।"
  }
]

***Caching***
Redis is used to cache translations for faster API responses. Cached data expires after 1 hour (timeout=3600).

*** Deployment***
Using Docker Compose

**Access the app at ** : <http://localhost:8000>


````
