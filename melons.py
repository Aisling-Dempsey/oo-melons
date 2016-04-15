"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """All melon orders"""

    
    def __init__(self,species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price."""
        base_price = 5
        
        # Evaluates if melon is "Christmas Melon" and updates base price accordingly
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    
    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    
    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        
        total_price = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total_price += 3
        print "hi!"
        return total_price

        
    # if qty < 10
    #     def get_total(self):
    #         base_price = 5
        
    #         total = (1 + self.tax) * self.qty * base_price + 3
    #         return total
    # else:
    #     
