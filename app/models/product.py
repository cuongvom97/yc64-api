from decimal import Decimal

from app.models.enum.product_type import ProductType
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Enum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"
    """
    Product Master

    Contains all products sold by YC64.

    Includes:
    - Veterinary medicine
    - Vaccine
    - Animal feed
    - Rice
    - Bran
    - Corn
    """

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    barcode: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="Restrict"),
        nullable=False,
    )

    category: Mapped["Category"] = relationship(
        back_populates="products",
    )

    unit_id: Mapped[int] = mapped_column(
        ForeignKey("units.id", ondelete="Restrict"),
        nullable=False,
    )

    unit: Mapped["Unit"] = relationship(
        back_populates="products",
    )

    supplier_id: Mapped[int] = mapped_column(
        ForeignKey("suppliers.id", ondelete="Restrict"),
        nullable=False,
    )

    supplier: Mapped["Supplier"] = relationship(
        back_populates="products",
    )

    product_type: Mapped[ProductType] = mapped_column(
        Enum(ProductType, name="product_type_enum"),
        nullable=False,
    )

    cost_price: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    sale_price: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    wholesale_price: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    dealer_price: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    min_stock: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    max_stock: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )
