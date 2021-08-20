from core.celery import app


@app.task
def find_id_from_provider_product(provider_product_id: int) -> int:
    return provider_product_id
