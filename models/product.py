#!/usr/bin/env python3
from models.base_model import BaseModel


class Product(BaseModel):
    """The product class, holding info about a produts"""
    vendor_id = ''
    user_id = ''
    name =''
    description = ''
    number_in_stock = 0

    
    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.product_id == self.id:
                review_list.append(review)
        return review_list
