from fastapi import FastAPI
from cities.routers import router as city_router

app = FastAPI()

# Include the city router
app.include_router(city_router, tags=["cities"])
