from pydantic import BaseModel, validator


class SoupEntrySchema(BaseModel):
    """
    Model for the resolve endpoint soup
    """

    entrypoint: list[list]
    words: list[str]

    @validator("*")
    def validate_instance(cls, v):
        if not isinstance(v, list):
            raise TypeError("Must be a list")
        return v
