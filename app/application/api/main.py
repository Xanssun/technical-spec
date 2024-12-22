from application.api.v1.handlers import router
from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title = 'The tron network',
        docs_url = '/api/docs',
        description = 'api for information output from the tron network',
        debug = True,
    )

    app.include_router(router, prefix='/tron')

    return app
