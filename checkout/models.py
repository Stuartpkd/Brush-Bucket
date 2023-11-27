from django.db import models
from django.db.models import Sum
from brushes.models import Brush
from profiles.models import UserProfile
import uuid


class Order(models.Model):
    """
    Represents a customer's complete order, including all necessary details
    like order number, user profile, contact info, and total cost.

    Attributes:
        order_number (CharField): A unique identifier for the order,
        generated using UUID.
        user_profile (ForeignKey): Links to a user's profile,
        if they are logged in.
        full_name (CharField): The full name provided for the order.
        email (EmailField): The email address provided for the order.
        date (DateTimeField): The date and time when the order was created.
        order_total (DecimalField): The total cost of the order
        excluding any additional fees.
        grand_total (DecimalField): The final total cost of the order,
        including any additional fees.
        original_bag (TextField): A text representation of the user's
        bag at the time of the order.
        stripe_pid (CharField): Stripe payment ID for the transaction.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False, blank=False, default='')

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        recalculating the order total.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already and update the grand total.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0

        self.grand_total = self.order_total

        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    """
    Represents a single line item within an order.

    Attributes:
        order (ForeignKey): The order to which this line item belongs.
        product (ForeignKey): The specific brush being ordered.
        quantity (IntegerField): The quantity of the product ordered.
        lineitem_total (DecimalField): The total cost of the,
        line item (price * quantity).
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Brush, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to calculate the line item total
        based on product price and quantity.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the line item,
        showing its product ID and associated order number.
        """
        return f'SKU {self.product.id} on order {self.order.order_number}'
