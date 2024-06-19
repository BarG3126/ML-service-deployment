"""
This module defines the DB models using SQLAlchemy.

Includes model classes for different types od real-estate,
specially rental apartments. The module uses SQLAlchemy's
ORM capabilities to map pyhon classes into DB tables.
The structure and fields of the RentApartments class are
configured to match the corresponding DB for rental apartments.
"""

from sqlalchemy import INTEGER, REAL, VARCHAR
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from config import database_settings

# Base class for SQLAlchemy models.
base = declarative_base()


class RentApartments(base):
    """
    SQLAlchemy model for rental apartments.

    Attributes:
        address (str): Adress of apartment, PrmaryKey.
        area (float): Area of apartment on square meters.
        constraction_year (int): Year apartment was constructed.
        rooms (int): Number of rooms in the apartment.
        bedrooms (int): Number of bedrooms in the apartment.
        bathrooms (int): Number of bathrooms in the apartment.
        balcony (str): Information about balcony.
        storage (str): Information about storage space.
        parking (str): Information about parking availability.
        furnished (str): Indicated if the apartment in furnished.
        garage (str): Information about garage.
        garden (str): Information about garden.
        energy (str): Energy efficiency rating.
        facilities (str): Other available facilities.
        zip (str):  ZIP code of apartment location.
        neighborhood (str): Neighborhood the apartments is located in.
        rent (int): Monthly rent price.
    """

    __tablename__ = database_settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[str] = mapped_column(VARCHAR())
    neighborhood: Mapped[str] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
