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
## Example Usage

### Create Short URL
<img width="580" height="154" alt="create_url" src="https://github.com/user-attachments/assets/dc5ac30d-3941-4630-b8ae-5f38bc8f0dfc" />


### Redirect to Original URL
<img width="1286" height="896" alt="redirect" src="https://github.com/user-attachments/assets/9dfca4a1-8c62-4c3a-b26d-f44a30689927" />


### View Analytics
<img width="575" height="154" alt="stats" src="https://github.com/user-attachments/assets/49b92e16-e5ff-4e09-93ad-1d19cafe538b" />


