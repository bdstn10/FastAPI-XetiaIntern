from httpx import AsyncClient, RequestError, HTTPStatusError
from fastapi import HTTPException, status
import ujson

from app.configs import config

client = AsyncClient()

# product api async client
async def get_purchase_finished(purchase_id, token, c = client):
    url = config.product_service_url + "/purchase/" + purchase_id
    headers = {
        "accept": "application/json",
        "locale": "en",
        "Authorization": "Bearer " + token
    }

    try:
        response = await c.get(url, headers=headers)
        response.raise_for_status()
    except RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"An error occurred while requesting {exc.request.url!r}."
        )
    except HTTPStatusError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        )

    # check if finished
    pay_status = ujson.load(response)['response']['status']
    if pay_status != 'finished':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Payment status is not finished",
        )

    total = ujson.load(response)['response']['total']
    currency = ujson.load(response)['response']['currency']


    return total, currency