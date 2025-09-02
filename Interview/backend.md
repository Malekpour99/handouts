# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Backend](#backend)
    - [Authentication Vs. Authorization](#authentication-vs-authorization)
    - [Stateful Vs. Stateless](#stateful-vs-stateless)
    - [JWT](#jwt)
    - [MVT in Django - MVT vs. MVC](#mvt-in-django---mvt-vs-mvc)
    - [Django Request-Response Lifecycle](#django-request-response-lifecycle)
    - [Design Patterns Used in Django](#design-patterns-used-in-django)
    - [Django Lazy Queries](#django-lazy-queries)
    - [N + 1 Problem](#n--1-problem)
    - [Select-Related \& Prefetch-Related in Django](#select-related--prefetch-related-in-django)
    - [When would you prefer prefetch_related over select_related, even if a JOIN is possible?](#when-would-you-prefer-prefetch_related-over-select_related-even-if-a-join-is-possible)
    - [Atomic Transactions in Django](#atomic-transactions-in-django)
    - [Handling Race Conditions in Django](#handling-race-conditions-in-django)

## Backend

### Authentication Vs. Authorization

**Authentication**: The process of verifying who the user is. It’s about **identity verification**.

**Authorization**: The process of verifying what the authenticated user can do. It’s about **permissions and access control**. Usually happens after authentication.

---

### Stateful Vs. Stateless

| Aspect            | Stateless                           | Stateful                                       |
| ----------------- | ----------------------------------- | ---------------------------------------------- |
| **Server Memory** | Doesn’t store client state          | Stores client state (sessions, context)        |
| **Scaling**       | Easy (any server can serve request) | Harder (needs sticky sessions or shared state) |
| **Failure**       | Recover easily (no session loss)    | Session loss if server crashes                 |
| **Example**       | REST API, DNS, HTTP itself          | WebSockets, FTP, server-side sessions          |

### JWT

**JWT (JSON Web Token)** is a compact, URL-safe, self-contained token used to securely transmit information between parties.
Commonly used for **authentication and authorization** in **stateless** systems.
Instead of storing sessions on the server, the server issues a signed token to the client.

A JWT consists of three parts separated by dots (.): `header.payload.signature`

- **Header** → metadata about the token (e.g., type = JWT, signing algorithm = HS256 or RS256).

```json
{ "alg": "HS256", "typ": "JWT" }
```

- **Payload** → contains claims (statements about the user or context).

  - Registered claims: iss (issuer), exp (expiration), sub (subject), aud (audience).
  - Public claims: app-defined (like role).
  - Private claims: agreed upon between parties.

```json
{ "sub": "123456", "name": "Alice", "role": "admin", "exp": 1735647390 }
```

- **Signature** → ensures integrity.

```
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

---

### MVT in Django - MVT vs. MVC

**MVC** stands for **Model-View-Controller**. It's a software design pattern used for developing user interfaces.

**MVT** stands for **Model-View-Template**, and it's Django's variant of the MVC architecture.

- **Model**:

  - Defines the data structure.
  - Interacts with the database.
  - Written in `models.py`.

- **View**:

  - Contains the business logic. (Better to decouple business logic using **services**)
  - Fetches data from the model and sends it to the template.
  - Written in `views.py`.

- **Template**:
  - Handles the presentation layer (HTML, CSS).
  - Receives data from the view and renders the final page.

| Concept        | MVC                                       | Django (MVT)                       |
| -------------- | ----------------------------------------- | ---------------------------------- |
| **Model**      | Manages the data and logic                | Same                               |
| **View**       | Handles presentation/UI                   | Called a **Template** in Django    |
| **Controller** | Handles user input and updates model/view | **View** in Django (handles logic) |
| **Template**   | Optional layer                            | Explicit layer for HTML rendering  |

User -> Controller -> Model -> View -> User

User -> Django (Controller) -> View -> Model -> Template -> User

---

### Django Request-Response Lifecycle

**Browser -> WSGI/ASGI Server (e.g., Gunicorn, Uvicorn) -> Django Middleware (Request Phase) -> URL Dispatcher (urls.py) -> View (views.py) -> Models (if needed) -> Templates (if needed) -> Django Middleware (Response Phase) -> WSGI/ASGI Server -> Browser (Rendered Response)**

**- Browser Sends a Request**

- A user initiates an HTTP request by entering a URL or submitting a form.
- This request is received by Django's WSGI-compatible web server (e.g., Gunicorn, uWSGI).

**- WSGI/ASGI Server Passes Request to Django**

- The WSGI/ASGI server passes the request to Django via a callable interface defined in `wsgi.py` or `asgi.py`.
- Django initializes necessary components to handle the request.

**- Middleware Processing (Request Phase)**

- The request passes through **middleware** defined in `MIDDLEWARE` setting.
- Middleware are Python classes that WWcan:
  - Modify the request.
  - Block the request.
  - Add metadata.
  - Perform authentication or logging.

**- URL Routing**

- Django uses urls.py to match the request path with a corresponding view function.
- It checks from top to bottom until it finds a match using path() or re_path().

**- View Execution**

- The matched view function or class-based view (CBV) is called.
- This view:
  - May fetch data from the model.
  - Passes data to a template.
  - Returns an HttpResponse object.

**- Template Rendering (Optional)**

- If the view uses render(), Django:
  - Loads the template (.html file).
  - Renders it with the context data.
  - Produces HTML output.

**- Middleware Processing (Response Phase)**

- Before the final response is returned to the browser, it passes back through middleware (in reverse order).
- Middleware can:
  - Modify the response.
  - Add headers.
  - Compress or encrypt content.

**- Response Sent to Client**

- Django returns the final Response object (HTML, JSON, file, etc.).
- The WSGI/ASGI server sends it back to the client (browser or API consumer).

---

### Design Patterns Used in Django

- MVT is a variation of **MVC** pattern
- ORM implements the **Active Record** pattern
  - Each model class maps to a database table
  - Each instance maps to a row
  - CRUD operations are methods on the model itself
- Model managers implement **Factory** pattern for generating querysets
- Settings implement **Singleton** pattern (single global instance)
- Database connections implement **Singleton** pattern (one per thread/request)
- DTL (Django Template Language) implements **Template** pattern
- Django signals implement **Observer/Signal** pattern
- Middlewares implement **Chain of Responsibility** pattern
- authentication and authorization uses **decorator** patterns (`@login_required, @csrf_exempt`)

---

### Django Lazy Queries

The SQL only runs when you actually **need the data**. This is what "lazy evaluation" means.

Django creates a QuerySet object — a _representation_ of the query, but not the results. A QuerySet **executes at the point you require concrete results**.

Query executes at:

- Iteration
- Slicing (with materialization)
- Casting to list
- Calling methods that return results (e.g. `get(), first(), last(), count(), exists(), aggregate(), values()`)

---

### N + 1 Problem

The N+1 problem happens when you run 1 query to fetch a list of records (N records), and then for each record, you run an additional query to fetch related data.

- Total queries = 1 (initial fetch) + N (per record) = N+1 queries.
- This quickly becomes inefficient at scale, especially with large datasets.

In Django

- Use `select_related` for **one-to-one** or **foreign key** relationships.
- Use `prefetch_related` for **many-to-many** or **reverse** relationships.

In Go (GORM)

- Use **eager loading** (`Preload`).

---

### Select-Related & Prefetch-Related in Django

`select_related` in Django:

- Purpose: Optimizes access to single-valued relationships (ForeignKey, OneToOneField).
- Mechanism: Generates a **SQL JOIN** to fetch related objects in the same query.
- Type of JOIN: Django uses **INNER JOIN** by default, but it switches to **LEFT OUTER JOIN** if the relation is **nullable** (so you don’t lose rows when the related object doesn’t exist).

`prefetch_related` in Django

- Purpose: Optimizes access to multi-valued relationships (reverse foreign key, many-to-many).
- Mechanism: Executes two separate queries and then does the **“join” in Python**, not SQL.
  - Query 1: Fetch base objects.
  - Query 2: Fetch related objects with an IN (...) filter.
- Type of JOIN: None at SQL level (Django does a “manual join” in memory).

---

### When would you prefer prefetch_related over select_related, even if a JOIN is possible?

1. Risk of Row Explosion

   - If I use select_related (JOIN), the result set size can blow up when one parent has many children.
   - Example: A User with 10,000 Posts.
   - select_related with a JOIN → returns 10,000 rows for 1 user, duplicating user fields in each row.
   - That wastes network bandwidth, memory, and ORM processing time.

   - prefetch_related avoids this by fetching:
   - 1 row for the user
   - 10,000 rows for posts (separate query)
   - Then Django associates them in Python.

2. Better Query Planner Performance

   - A huge JOIN with multiple relations can confuse the database’s query planner, leading to slow execution.
   - With prefetch_related, you keep queries simpler (SELECT ... WHERE id IN (...)) and let Django’s Python layer do the merge.
   - This is often faster in real-world apps where relations are 1-to-many or many-to-many.

3. Memory Efficiency in Python

   - With JOINs (select_related), Django has to hydrate a model instance per duplicate row — even though most fields are identical.
   - With prefetch_related, the base objects (User) are hydrated once, and the children (Posts) are hydrated separately and attached.

4. Database Load Balancing

   - In some setups (read replicas, sharded DBs), it’s useful to keep queries smaller and more cache-friendly.
   - prefetch_related queries (WHERE ... IN (...)) can be batched or routed independently, while a giant JOIN can’t.

---

### Atomic Transactions in Django

In Django, an atomic transaction ensures that a block of database operations is treated as a single unit of work:

- Either all of the operations succeed → commit.
- Or if an error occurs → all are rolled back.

This ensures **data consistency** and prevents partial writes.

Django provides `transaction.atomic()` as a context manager or decorator.

---

### Handling Race Conditions in Django

You can handle race condition by combining:

- `transaction.atomic()` ensures all-or-nothing.
- `select_for_update()` locks the row until the transaction completes → prevents others from reading stale data.
- Example:

```python
from django.db import transaction

def book_ticket(user, event):
    with transaction.atomic():
        ticket = Ticket.objects.select_for_update().get(event=event)
        if ticket.remaining > 0:
            ticket.remaining -= 1
            ticket.save()
        else:
            raise Exception("Sold out")
```

- `F()` expressions (avoid race conditions on updates)
- Example:

```python
from django.db.models import F

def increment_likes(post_id):
    Post.objects.filter(id=post_id).update(likes=F('likes') + 1)
```

---
