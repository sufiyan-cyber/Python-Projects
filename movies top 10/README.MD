# 🎬 Movie Collection Manager (Flask + SQLAlchemy + TMDB API)

A full-stack Flask web application that lets users search real movies from The Movie Database (TMDB) API, add them into a personal database, review them, rank them automatically, and manage them with persistent storage using SQLAlchemy ORM.

This project focuses on backend engineering practices rather than UI complexity — emphasizing database modeling, safe API integration, and clean request lifecycle handling.


--------------------------------------------------------------------

## Why This Project Matters

This is not just a CRUD app.

The objective of this project was to demonstrate understanding of:

- ORM-based persistence (not raw SQL)
- External API orchestration
- Server-side form validation
- Stateful workflows across multiple routes
- Data integrity constraints
- Preventing duplicate records
- Dynamic ranking algorithm based on data ordering

The UI is intentionally simple so the backend system design is the primary highlight.


--------------------------------------------------------------------

## Tech Stack

Backend Framework: Flask  
Database: SQLite  
ORM: SQLAlchemy (Declarative Mapping)  
Forms & Validation: Flask-WTF / WTForms  
Styling: Bootstrap 5  
External API: TMDB (The Movie Database)  
Environment Management: python-dotenv  
HTTP Client: Requests


--------------------------------------------------------------------

## Core Features

### 1) Search Real Movies (Live API Integration)

Users type a movie name → app queries TMDB → displays multiple matches.

Flow:
User Input → Flask Route → TMDB Search Endpoint → JSON Parse → Select Movie Page

The app does not store fake/manual movie data — it pulls real metadata directly from TMDB.


--------------------------------------------------------------------

### 2) Two-Step Movie Addition (Important Design Decision)

Instead of directly inserting user input into the database:

1. User searches movie
2. User selects correct movie from results
3. App fetches official movie details
4. Then database insertion happens

This avoids:
- typos
- inconsistent titles
- fake data
- missing metadata

This mimics real production systems that rely on authoritative external data sources.


--------------------------------------------------------------------

### 3) Persistent Database Using SQLAlchemy ORM

The database model:

Movie:
- id
- title (unique)
- year
- description
- rating
- ranking
- review
- img_url

The project does NOT use raw SQL queries.

Instead it uses:
- Declarative Mapping
- Type annotated columns
- ORM session transactions
- Query abstraction

Example query:

db.session.execute(
    db.select(Movie).order_by(Movie.rating.desc())
)

This demonstrates:
- separation of database logic from application logic
- maintainable database operations
- database portability (SQLite → PostgreSQL migration possible)


--------------------------------------------------------------------

### 4) Automatic Ranking System

Ranking is dynamically computed every time the home page loads.

Algorithm:
1. Fetch all movies ordered by rating (descending)
2. Assign rank based on position

Highest rating → Rank 1  
Second → Rank 2  
...

This simulates a leaderboard system.


--------------------------------------------------------------------

### 5) Edit Review & Rating (Form Validation)

Users can:
- update rating
- add review

Implemented using Flask-WTF:
- CSRF protection
- server-side validation
- controlled submission


--------------------------------------------------------------------

### 6) Duplicate Prevention (Data Integrity)

Before inserting a movie, the app checks if it already exists.

If already exists → insertion blocked.

This prevents:
- duplicate rows
- broken rankings
- inconsistent database state


--------------------------------------------------------------------

### 7) Safe External API Handling

The app safely handles missing API fields:

Missing release date → defaults to 0  
Missing poster → empty string  
Missing description → fallback text

This prevents crashes from unpredictable API responses.


--------------------------------------------------------------------

### 8) Protected Delete

Movies are deleted only via POST request to prevent accidental deletion through URL visits.


--------------------------------------------------------------------

## Application Workflow

Search Movie → Select Movie → Insert Into Database → Edit Rating → Ranked Display

Routes:

/                → Show ranked movie list  
/add             → Search movie  
/find            → Fetch movie details from TMDB  
/edit/<id>       → Add rating & review  
/delete/<id>     → Remove movie


--------------------------------------------------------------------

## Database Design Choices

Key constraints used:

- title is UNIQUE → prevents duplicates
- rating NOT NULL → ranking always calculable
- img_url NOT NULL → UI consistency

Database validity does not rely on frontend checks.


--------------------------------------------------------------------

## Environment Variables

Create a `.env` file:

apikey=YOUR_TMDB_API_KEY


--------------------------------------------------------------------



--------------------------------------------------------------------

## What This Project Demonstrates

- REST API consumption
- server side rendering
- ORM based persistence
- transactional database operations
- request routing
- multi-step user workflows
- backend validation
- stateful web applications

Although visually simple, the architecture is similar to:
- review platforms
- catalog managers
- admin dashboards
- CMS backends


--------------------------------------------------------------------

## Possible Improvements

- User authentication
- PostgreSQL deployment
- Docker containerization
- AWS deployment
- Pagination
- Movie recommendations


--------------------------------------------------------------------

## Author

Sufiyan  
Information Science Engineering Student  
Backend / Cloud / Security Enthusiast
