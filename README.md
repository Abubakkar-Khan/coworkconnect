# CoWorkConnect

CoWorkConnect is a web-based coworking space management and professional networking platform. The system is designed to help users discover coworking spaces, book workspaces, create community posts, join discussion groups, exchange group messages, and register for professional events. It also provides an admin-side workflow for managing workspace inventory.

This project is suitable for a final year project or thesis because it combines user management, role-based authorization, booking workflows, community interaction, event management, file uploads, database design, and a complete web interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Main Modules](#main-modules)
  - [1. Authentication Module](#1-authentication-module)
  - [2. User Profile Module](#2-user-profile-module)
  - [3. Space Management Module](#3-space-management-module)
  - [4. Booking Module](#4-booking-module)
  - [5. Community Posts Module](#5-community-posts-module)
  - [6. Groups and Messaging Module](#6-groups-and-messaging-module)
  - [7. Events Module](#7-events-module)
- [Database Design](#database-design)
- [Authentication and Authorization](#authentication-and-authorization)
- [API Summary](#api-summary)
- [Setup Instructions](#setup-instructions)
- [Deployment on Vercel](#deployment-on-vercel)
- [User Interface Pages](#user-interface-pages)
- [Testing and Validation](#testing-and-validation)
- [Security Features](#security-features)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

## Project Overview

The main purpose of CoWorkConnect is to provide a centralized digital platform for coworking users, space owners, freelancers, startups, and remote professionals. Instead of using separate tools for workspace booking, event discovery, and community communication, CoWorkConnect brings these features into one integrated system.

The platform supports two main user roles:

- `user`: A normal member who can browse spaces, book spaces, create posts, join groups, send messages, and register for events.
- `admin`: A privileged user who can manage coworking spaces and view or update booking records.

## Problem Statement

Many coworking spaces rely on manual communication, social media pages, or disconnected tools for bookings, member interaction, and event promotion. This creates problems such as duplicate bookings, limited visibility of available spaces, weak community engagement, and inefficient administration.

CoWorkConnect addresses these issues by providing a single web application where users can:

- Search and view available coworking spaces.
- Book a workspace for a selected date.
- Manage their profile.
- Share posts and interact with community content.
- Join discussion groups and communicate with members.
- Discover and register for coworking-related events.
- Allow administrators to manage available workspace resources.

## Objectives

The key objectives of the project are:

- To design and develop a coworking space management system.
- To implement secure user registration and login using JWT authentication.
- To provide role-based access control for users and administrators.
- To allow users to browse, filter, and book coworking spaces.
- To support community engagement through posts, comments, likes, and groups.
- To provide event creation and registration functionality.
- To store all important system data in a MySQL relational database.
- To create a responsive frontend using HTML, CSS, and JavaScript.
- To implement the backend using Django and Python.

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| Frontend | HTML, CSS, JavaScript |
| Backend | Django, Python |
| Database | MySQL |
| Authentication | JWT, bcrypt password hashing |
| File Uploads | Django file handling |
| API Style | REST-style JSON endpoints |
| Server | Django development server |

The current project does not use Node.js. The frontend is plain HTML, CSS, and JavaScript, while the backend is Django.

## System Architecture

CoWorkConnect follows a client-server architecture.

```mermaid
flowchart TD
    A[Browser UI<br/>HTML, CSS, JavaScript] -->|"fetch() API requests"| B[Django Backend<br/>REST APIs]
    B -->|"SQL Queries"| C[(MySQL Database)]
    B -->|"File I/O"| D[Local File System<br/>Uploads Directory]
```

The frontend pages are stored in the `ui/` directory. These pages communicate with the backend through `/api/...` endpoints using JavaScript `fetch()` requests. The Django backend receives the requests, validates input, checks authentication where required, performs database operations, and returns JSON responses.

## Project Structure

```text
coworkconnect/
  api/
    management/
      commands/
        seed.py
    apps.py
    middleware.py
    schema.py
    urls.py
    utils.py
    views.py
  coworkconnect/
    asgi.py
    settings.py
    urls.py
    wsgi.py
  ui/
    admin.html
    app.js
    community.html
# CoWorkConnect

CoWorkConnect is a web-based coworking space management, social networking, and community collaboration platform. The system helps users discover coworking spaces, book workspaces, create community posts, join discussion groups (Circles), exchange group messages, manage Facebook-style friend connections, showcase GitHub & LinkedIn portfolios, and register for professional events with compulsory Google Form verification.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features & Modules](#key-features--modules)
  - [1. User Profile & Public Portfolios](#1-user-profile--public-portfolios)
  - [2. Facebook-Style Friends System](#2-facebook-style-friends-system)
  - [3. LinkedIn-Style User Activity & Networking Feed](#3-linkedin-style-user-activity--networking-feed)
  - [4. Dual-Layer Image Compression Engine](#4-dual-layer-image-compression-engine)
  - [5. Space Discovery & Workspace Bookings](#5-space-discovery--workspace-bookings)
  - [6. Circles & Group Messaging](#6-circles--group-messaging)
  - [7. Events Management & Verification Center](#7-events-management--verification-center)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Database Schema](#database-schema)
- [API Endpoints Reference](#api-endpoints-reference)
- [Setup & Local Development](#setup--local-development)

---

## Project Overview

CoWorkConnect brings together space reservation, social networking, event hosting, and team collaboration into a single, unified web platform.

### User Roles:
- **Member (`user`)**: Browse and book spaces, publish posts, connect with friends, join Circles, send chat messages, and attend events.
- **Administrator (`admin`)**: Manage space listings, edit/delete any community content, approve/reject event registrations, and review system logs.

---

## Key Features & Modules

### 1. User Profile & Public Portfolios (`profile.html` & `user-profile.html`)
- **Public Member Profile Page (`user-profile.html?id=X`)**: Clicking any user avatar or name across Circles, Network posts, or Event hosts opens their dedicated public profile page.
- **Professional Headline & Bio**: Users can add a professional headline (e.g. *"Software Engineer @ TechCorp | Open to Collab"*) and catchy bio.
- **GitHub 💻 & LinkedIn 💼 Links**: Interactive social badges on user profiles for instant portfolio viewing.
- **Navbar Profile Avatar**: The top-right navbar profile button renders the user's actual uploaded avatar image across all pages.

### 2. Facebook-Style Friends System (`friendships`)
- **Friend Requests Lifecycle**:
  - `+ Add Friend`: Sends a friend request.
  - `⏳ Request Sent`: Displays pending outgoing request status.
  - `✓ Accept Friend Request`: Accepts incoming friend requests.
  - `Friends ✓ (Unfriend)`: Allows managing or removing friends.
- **My Friends Grid**: Dedicated card on `profile.html` and `user-profile.html` displaying accepted friends.

### 3. LinkedIn-Style User Activity & Networking Feed (`community.html`)
- **Full Feed Filtering**: Filter posts by `#hashtags`, Latest, Top, Questions, and Collaborations.
- **User Activity Filter (`community.html?user_id=X`)**: Filter the entire networking feed specifically for posts authored by a single user, complete with likes, nested comments, and sharing.
- **Text Wrapping Protection**: Line-wrapping CSS (`white-space: pre-wrap; word-break: break-word;`) prevents long text or URLs from distorting card layouts.

### 4. Dual-Layer Image Compression Engine
- **Frontend Compression (`compressImageFile`)**: HTML5 Canvas resizes large uploads (max 1200x1200) and compresses blobs before network transmission.
- **Backend Optimization (`save_upload`)**: Pillow/PIL resizes and saves images with JPEG `quality=82` and optimization flags.

### 5. Space Discovery & Workspace Bookings (`spaces.html` & `spaces-details.html`)
- **Workspace Filtering**: Search desks, private offices, meeting rooms, and virtual offices.
- **Interactive Reservations**: Reserve spaces for selected dates with real-time price calculations and booking history on `my-bookings.html`.

### 6. Circles & Group Messaging (`groups.html`)
- **Discussion Circles**: Join or create public/private co-working circles.
- **Group Chat & Media Attachments**: Send real-time group messages with image attachments.
- **Circle Roster & Roles**: Manage member roles (Host, Co-Admin, Member) and click member rows to view profiles.

### 7. Events Management & Verification Center (`events.html` & `event-details.html`)
- **Compulsory Google Form Links**: Hosts must provide a valid Google Form registration URL when creating an event.
- **Embedded Form Modal**: Participants fill out the Google Form directly inside an interactive iframe modal.
- **Host Manual Verification Center**: Hosts review responses via direct Google Sheets links and approve/reject participant registration statuses (`pending`, `approved`, `rejected`).
- **In-Page Host Controls**: Edit Event and Delete Event buttons with red confirmation modals sit directly in the event page header.

---

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, Vanilla CSS, JavaScript (ES6+) |
| **Backend** | Python, Django, ASGI / Daphne |
| **Database** | PostgreSQL / SQLite / MySQL |
| **Authentication** | JWT (JSON Web Tokens), bcrypt hashing |
| **Icons & Typography** | Lucide Icons, Google Fonts (Outfit) |

---

## Database Schema

```sql
-- Users Table
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('user', 'admin') DEFAULT 'user',
  status VARCHAR(50) DEFAULT 'Available',
  bio TEXT,
  headline VARCHAR(255),
  avatar_url VARCHAR(255),
  github_url VARCHAR(255),
  linkedin_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Friendships Table
CREATE TABLE friendships (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  friend_id INT NOT NULL,
  status VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (user_id, friend_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (friend_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Events Table
CREATE TABLE events (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(150) NOT NULL,
  event_type VARCHAR(50) NOT NULL,
  city VARCHAR(50) NOT NULL,
  location VARCHAR(150) NOT NULL,
  event_date DATETIME NOT NULL,
  end_time DATETIME,
  description TEXT NOT NULL,
  google_form_url VARCHAR(500) NOT NULL,
  image_url VARCHAR(255),
  created_by INT NOT NULL
);

-- Event Registrations Table
CREATE TABLE event_registrations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  event_id INT NOT NULL,
  user_id INT NOT NULL,
  status VARCHAR(50) DEFAULT 'pending',
  registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (event_id, user_id)
);
```

---

## API Endpoints Reference

### Authentication & Users
- `POST /api/auth/register` — Register a new account.
- `POST /api/auth/login` — Sign in and receive JWT token.
- `GET /api/users/profile` — Fetch current user profile.
- `PUT /api/users/profile` — Update name, bio, headline, GitHub/LinkedIn links, status.
- `POST /api/users/profile/avatar` — Upload and compress profile avatar image.
- `GET /api/users/<user_id>` — Fetch public user profile, headline, social links & friendship status.

### Friends System
- `GET /api/friends` — List accepted friends and pending requests.
- `GET /api/users/<user_id>/friends` — List accepted friends for target user.
- `POST /api/friends/request` — Send friend request to `friend_id`.
- `PUT /api/friends/respond` — Accept, decline, or unfriend (`action`: `'accept'` | `'decline'` | `'unfriend'`).

### Community Posts & Activity
- `GET /api/posts` — Fetch community feed (supports optional `?tag=X` or `?user_id=X`).
- `POST /api/posts` — Create a new post with text, tags, and compressed image.
- `POST /api/posts/<post_id>/like` — Toggle post like.
- `POST /api/posts/<post_id>/comments` — Add comment or nested reply.

### Events & Host Control
- `GET /api/events` — List upcoming events.
- `POST /api/events` — Create event (enforces compulsory Google Form URL).
- `GET /api/events/<event_id>` — Single event details.
- `PUT /api/events/<event_id>` — Update event details (Host/Admin only).
- `DELETE /api/events/<event_id>` — Delete event (Host/Admin only).
- `POST /api/events/<event_id>/register` — Register for event (status defaults to `pending`).
- `PUT /api/events/<event_id>/participants/<target_user_id>/status` — Update participant status (`approved`, `rejected`, `pending`).

---

## Setup & Local Development

1. **Clone & Install Dependencies**:
   ```bash
   python -m pip install django daphne pillow pyjwt bcrypt cloudinary
   ```
2. **Run Migrations & Start Development Server**:
   ```bash
   python manage.py migrate
   python manage.py runserver 5000
   ```
3. **Access Application**:
   Open `http://127.0.0.1:5000/` in your web browser.
    event-details.html
    events.html
    groups.html
    index.html
    profile.html
    register.html
    spaces.html
    style.css
  uploads/
  api_documentation.md
  manage.py
  README.md
  requirements.txt
```

## Main Modules

### 1. Authentication Module

The authentication module allows users to register and log in. Passwords are hashed using bcrypt before being stored in the database. After login, the backend returns a JWT token. This token is stored by the frontend and sent in the `Authorization` header for protected routes.

```mermaid
sequenceDiagram
    participant User as Frontend (Browser)
    participant API as Django Backend
    participant DB as MySQL Database

    User->>API: POST /api/auth/login (email, password)
    API->>DB: Query User by email
    DB-->>API: Return User Record (with Hashed Password)
    API->>API: Verify password with bcrypt
    API-->>User: Return JWT Token
```

Main features:
- User registration
- User login
- Password hashing
- JWT token generation
- Protected API access

### 2. User Profile Module

The profile module allows authenticated users to view and update their personal information.

Main features:
- View profile
- Update name, email, status, and bio
- Change password
- Search user profiles

### 3. Space Management Module

The space management module handles coworking space records.

Main features:
- View all available spaces
- Filter spaces by location, type, and price
- View details of one space
- Create, update, and delete spaces as an admin

### 4. Booking Module

The booking module allows users to reserve coworking spaces.

Main features:
- Create a booking for a selected space and date
- Prevent duplicate active bookings for the same space and date
- View current user's bookings
- Admin can view all bookings
- Admin can update booking status
- User or admin can cancel a booking

### 5. Community Posts Module

The community module allows users to share posts and interact with other members.

Main features:
- View community feed with paginated lazy loading
- In-app photo editor card (zoom, rotate, aspect ratio crop)
- Like or unlike posts with 0ms optimistic UI
- Comment on posts with collapsed comment hierarchy
- Delete own posts

### 6. Groups and Messaging Module (WhatsApp Web Layout)

The groups module provides a full-page (100vh) WhatsApp Web interface for community discussion circles.

Main features:
- Full-page WhatsApp Web 100vh chat layout
- Group Header Bar with active group image, name, member count, and action controls
- User profile avatars and role badges (`Admin`, `Co-Admin`, `Member`) on every message bubble
- Direct file upload for group pictures
- Drag & Drop and Clipboard Image Paste (`Ctrl+V`) into message composer
- Member drawer with role management (Promote to Co-Admin, Remove Member, Add Member via search)
- Admin group deletion with confirmation popup modal
- Request debouncing to eliminate multi-group creation on rapid clicks

### 7. Dual-Layer Image Compression Engine

CoWorkConnect includes an automatic dual-layer image compression pipeline across the whole website:
1. **Client-Side Canvas Compression (`ui/app.js`)**: High-resolution camera photos (3MB–10MB+) are compressed using an HTML5 Canvas pipeline (`compressImageFile`) down to max 1920x1920 resolution at ~82% quality before transmitting over the network.
2. **Server-Side Pillow Optimization (`api/utils.py`)**: The backend processes all uploaded raster images using Pillow (`PIL.Image` & `ImageOps.exif_transpose`), auto-orients smartphone camera photos, resizes oversized dimensions, and outputs optimized JPEGs/WebPs at ~82% quality.

### 8. Events Module

The events module allows users to create and register for professional events.

Main features:
- View all events
- Create events
- Upload optional event image
- Register for events
- View event participants

## Database Design

The system uses a MySQL relational database. The database name is configured through the `.env` file. Django automatically creates the required database and tables when the application starts.

### Tables

| Table | Purpose |
| :--- | :--- |
| `users` | Stores user accounts, roles, profile information, and hashed passwords |
| `spaces` | Stores coworking space information |
| `bookings` | Stores workspace booking records |
| `posts` | Stores community posts |
| `comments` | Stores comments on posts |
| `post_likes` | Stores post like records |
| `community_groups` | Stores discussion groups |
| `group_members` | Stores group membership records |
| `messages` | Stores group messages |
| `events` | Stores event details |
| `event_registrations` | Stores event participant registrations |

### Important Relationships

```mermaid
erDiagram
    USERS ||--o{ BOOKINGS : "creates"
    SPACES ||--o{ BOOKINGS : "receives"
    USERS ||--o{ POSTS : "creates"
    POSTS ||--o{ COMMENTS : "has"
    POSTS ||--o{ POST_LIKES : "has"
    USERS ||--o{ COMMUNITY_GROUPS : "creates"
    COMMUNITY_GROUPS ||--o{ GROUP_MEMBERS : "has"
    COMMUNITY_GROUPS ||--o{ MESSAGES : "has"
    USERS ||--o{ EVENTS : "creates"
    EVENTS ||--o{ EVENT_REGISTRATIONS : "has"
```

## Authentication and Authorization

Protected routes require a JWT token in the request header:

```text
Authorization: Bearer <token>
```

Role-based authorization is used for admin operations. For example, only users with the `admin` role can create, update, or delete coworking spaces.

## API Summary

Base URL:

```text
http://localhost:5000
```

### Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Login and receive JWT token |

### Spaces

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/spaces` | List spaces |
| GET | `/api/spaces/:id` | View one space |
| POST | `/api/spaces` | Create space, admin only |
| PUT | `/api/spaces/:id` | Update space, admin only |
| DELETE | `/api/spaces/:id` | Delete space, admin only |

### Bookings

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/bookings` | Create booking |
| GET | `/api/bookings/my` | View current user's bookings |
| GET | `/api/bookings` | View all bookings, admin only |
| PUT | `/api/bookings/:id` | Update booking status, admin only |
| DELETE | `/api/bookings/:id` | Cancel booking |

### Users

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/users/profile` | View current profile |
| PUT | `/api/users/profile` | Update current profile |
| PUT | `/api/users/updatepassword` | Change password |
| GET | `/api/users/search?query=...` | Search users |

### Community Posts

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/posts` | View community feed |
| POST | `/api/posts` | Create post |
| POST | `/api/posts/:id/like` | Toggle like |
| POST | `/api/posts/:id/comments` | Add comment |
| DELETE | `/api/posts/:id` | Delete post |

### Groups

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/groups` | View groups |
| POST | `/api/groups` | Create group |
| POST | `/api/groups/:id/join` | Join group |
| GET | `/api/groups/:id/messages` | View group messages |
| POST | `/api/groups/:id/messages` | Send group message |

### Events

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/events` | View events |
| POST | `/api/events` | Create event |
| POST | `/api/events/:id/register` | Register for event |
| GET | `/api/events/:id/participants` | View participants |

## Setup Instructions

### 1. Install Python Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create or update the `.env` file in the project root. The Django settings load this file automatically during local development.

```text
DEBUG=true
DJANGO_SECRET_KEY=use_a_long_random_secret_here
JWT_SECRET=use_a_long_random_secret_here
JWT_EXPIRE=30d

# Recommended for Supabase/Postgres:
DATABASE_URL=postgresql://USER:PASSWORD@HOST:6543/postgres?sslmode=require
DB_SSL=true

# Optional local MySQL fallback:
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=coworkconnect
DB_SSL=false
```

### 3. Start MySQL

Make sure the MySQL server is running on your machine. The application will create the configured database and tables automatically.

### 4. Run the Django Server

```powershell
python manage.py runserver 5000
```

Open the application in the browser:

```text
http://localhost:5000
```

## Deployment on Vercel

The project includes Vercel deployment support through:

- `vercel.json`
- root-level `wsgi.py`
- `.python-version`
- `requirements.txt`

Important: Vercel cannot connect to the MySQL database running on your laptop through `localhost`. For a real deployed backend, use an external database. Supabase is recommended because it provides a hosted PostgreSQL database with a connection URL that works well with Vercel.

### Recommended: Supabase Database

1. Create a Supabase project.
2. Open the Supabase dashboard.
3. Go to Project Settings > Database.
4. Copy the pooled connection string.
5. Add it to Vercel as `DATABASE_URL`.

Supabase connection string example:

```text
DATABASE_URL=postgresql://postgres.xxx:password@aws-0-region.pooler.supabase.com:6543/postgres?sslmode=require
```

The backend supports Supabase/PostgreSQL, hosted MySQL, and a temporary SQLite fallback for Vercel deployments without database variables. The SQLite fallback is only for basic testing because serverless storage is not permanent.

Set these environment variables in the Vercel project dashboard:

```text
DEBUG=false
DJANGO_SECRET_KEY=your_long_random_secret
JWT_SECRET=your_long_random_secret
JWT_EXPIRE=30d
DATABASE_URL=your_supabase_or_external_database_url
```

Hosted MySQL can still be configured with individual DB variables:

```text
DB_ENGINE=mysql
DB_HOST=your_external_mysql_host
DB_PORT=3306
DB_USER=your_external_mysql_user
DB_PASSWORD=your_external_mysql_password
DB_NAME=coworkconnect
DB_SSL=true
```

After saving the environment variables, redeploy the Vercel project. The Django backend will create the required tables automatically on the first request.

Note: Vercel serverless storage is not persistent. Uploaded files may not remain permanently unless external file storage is added later, such as Vercel Blob, S3, or Cloudinary.

### 5. Optional Seed Data

After registering at least one user, run:

```powershell
python manage.py seed
```

This adds sample event data for testing.

## User Interface Pages

| Page | Purpose |
| :--- | :--- |
| `index.html` | Landing/home page |
| `register.html` | User registration |
| `spaces.html` | Browse coworking spaces |
| `profile.html` | User profile management |
| `community.html` | Community posts and inline sign in when needed |
| `groups.html` | Discussion groups, messaging, and inline sign in when needed |
| `events.html` | Event listing and creation |
| `event-details.html` | Event details and registration |
| `admin.html` | Admin space management |

## Testing and Validation

The project can be tested using:

- Browser testing for frontend pages.
- API testing through Postman or similar tools.
- Django system check:

```powershell
python manage.py check
```

Important test scenarios:

- Register a new user.
- Login and receive a JWT token.
- Access protected routes with and without a token.
- Create and filter coworking spaces.
- Create a booking and verify duplicate booking prevention.
- Create posts, comments, and likes.
- Create and join groups.
- Send and retrieve group messages.
- Create and register for events.
- Verify admin-only endpoints reject normal users.

## Security Features

- Passwords are stored as bcrypt hashes.
- JWT authentication is used for protected routes.
- Role-based authorization protects admin functionality.
- SQL queries use parameterized values to reduce SQL injection risk.
- File uploads are stored in the `uploads/` directory.

## Limitations

The current system is functional for academic and prototype use, but some limitations remain:

- Group messaging uses polling instead of real-time WebSocket communication.
- The admin panel focuses mainly on space management.
- No online payment integration is included.
- No email verification or password reset workflow is included.
- File upload validation can be expanded further.
- The project currently uses manually defined SQL tables instead of Django ORM models.

## Future Enhancements

Future versions of CoWorkConnect can include:

- Real-time chat using Django Channels.
- Online payment gateway integration.
- Email verification and password reset.
- Advanced admin dashboard with analytics.
- Booking calendar view.
- Reviews and ratings for coworking spaces.
- Notification system.
- Space owner role separate from admin.
- Better search and recommendation features.
- Deployment on a cloud server.

## Conclusion

CoWorkConnect demonstrates how a coworking management system can combine workspace booking, community networking, group communication, and event participation into a single platform. The project uses a simple HTML, CSS, and JavaScript frontend with a Django and MySQL backend, making it understandable, extensible, and suitable for academic documentation and thesis presentation.
