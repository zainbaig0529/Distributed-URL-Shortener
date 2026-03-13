## Distributed URL Shortener

A backend system that generates shortened URLs and redirects users efficiently using caching and persistent storage.

### Features

* Generate shortened URLs
* Redirect short links to original URLs
* Redis caching for fast lookups
* PostgreSQL persistent storage
* Click analytics tracking
* Custom alias support
* URL expiration support
* Docker containerized services

### Tech Stack

Backend:

* Python
* Flask
* SQLAlchemy

Infrastructure:

* Redis (caching layer)
* PostgreSQL (database)
* Docker Compose (service orchestration)

### Architecture

Client Request
↓
Flask API (URL Shortener Service)
↓
Redis Cache → Fast redirect lookup
↓
PostgreSQL → Persistent storage and analytics

### API Endpoints

POST /shorten
Creates a shortened URL.

GET /<short_code>
Redirects the user to the original URL.

GET /stats/<short_code>
Returns analytics information about a short link.

### Running the Project

```bash
docker compose up --build
```

