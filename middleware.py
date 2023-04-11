from typing import Callable
from flask import request
from pydantic import ValidationError
from schemas import SoupEntrySchema
from werkzeug.exceptions import BadRequest


def validate_request(f: Callable):
    """
    This decorator validates the request body to be a valid SoupEntrySchema
    if the request body is not valid, it returns a 406 response

    Args:
        f (Callable): The function to be decorated

    Returns:
        Callable: The decorated function
    """

    def wrapper(*args: tuple, **kwargs: dict):
        try:
            SoupEntrySchema(**request.get_json())
        except (ValidationError, TypeError) as e:
            return {
                "message": str(e),
                "code": "BR001",
                "success": False,
            }, 406

        return f(*args, **kwargs)

    return wrapper
