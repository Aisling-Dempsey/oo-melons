"""This file should have our order classes in it."""
from random import randint
class AbstractMelonOrder(object):
    """All melon orders"""

    def __init__(self,species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = randint(5,9)


    def get_base_price(self):
        """determines base price of melon order"""
        # Evaluates if melon is "Christmas Melon" and updates base price accordingly
        if self.species == "Christmas Melon":
            self.base_price = self.base_price * 1.5
        return self.base_price


    def get_total(self):
        """Calculate price."""

        total = (1 + self.tax) * self.qty * self.get_base_price()
        return total

    
    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        
        total_price = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total_price += 3
        return total_price

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Orders (no tax)"""

    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):
        """Set passed_inspection to True"""
        if passed:
            self.passed_inspection = True