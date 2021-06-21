from core.celery import app


@app.task
def find_provider_product_id(provider_product_id: int) -> int:
    return provider_product_id
