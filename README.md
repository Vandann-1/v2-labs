# V2 Labs Backend

Django + Django REST Framework backend for V2 Labs lead capture and notification workflows.

## Local setup

1. Create `.env` from [`.env.example`](C:/Users/User/Desktop/v2labs/v2labs%20backend/v2-labs/.env.example:1).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the server:

```bash
python manage.py runserver
```

## Deployment on Render

- Python version is pinned in [runtime.txt](C:/Users/User/Desktop/v2labs/v2labs%20backend/v2-labs/runtime.txt:1)
- Render blueprint config is in [render.yaml](C:/Users/User/Desktop/v2labs/v2labs%20backend/v2-labs/render.yaml:1)
- Build script is in [build.sh](C:/Users/User/Desktop/v2labs/v2labs%20backend/v2-labs/build.sh:1)

### Required environment variables

- `DJANGO_ENV=production`
- `DJANGO_SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CORS_ALLOWED_ORIGINS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `LEAD_NOTIFICATION_RECIPIENTS`
- `V2_LABS_FRONTEND_URL`

## Lead notifications

Lead submissions from `/api/contact/` trigger:

- lead persistence
- IP / user-agent / source-page capture
- premium HTML email notification
- plain-text fallback email
