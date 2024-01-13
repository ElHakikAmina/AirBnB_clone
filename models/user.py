#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): the email of the user.
        password (str): the password of the user.
        firstname2 (str): the first name of the user.
        last_name (str): the last name of the user.
    """

    email = ""
    password = ""
    firstname2 = ""
    last_name = ""
