import os
from pathlib import Path
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from core.config import settings
from db import init_tortoise
from api.v1.api import api_router


def create_app():
    app = FastAPI(title='The citybike Wien Importer',
                  middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=['*'],
                allow_credentials=True,
                allow_methods=['*'],
                allow_headers=['*'],
            )
        ],)

    Path("static/uploads").mkdir(parents=True, exist_ok=True)
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(settings.BASE_DIR, "static")),
        name="static",
    )

    init_tortoise(app)

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app
