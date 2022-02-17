"""Classes for melon orders."""
class AbstractMelonOrder:
    """ A melon order abstract class"""

    tax = 0

    def __init__(self, species, qty, country_code):
        """A melon order """ 
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"    
    tax = 0.08

    def __init__(self, species, qty):
        super().__init__(species, qty, country_code = 'None')


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
        
    def get_total(self):    
        """Calculate price, including tax."""

        total = super().get_total()
        
        if self.qty < 10:
            total = total + 3
        
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """ A government melon order"""

    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, country_code = 'None')

    def mark_inspection(self, passed):
        """ Update whether or not the melon passed inspection"""

        self.passed_inspection = passed
