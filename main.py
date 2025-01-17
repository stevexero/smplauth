from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from settings import settings

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    contact={
        "name": settings.contact_name,
        "url": settings.contact_url,
        "email": settings.contact_email,
    },
    license_info={
        "name": settings.license_name,
        "url": settings.license_url,
    },
)


@app.get("/")
async def hello():
    return RedirectResponse(url=settings.redirect_url)