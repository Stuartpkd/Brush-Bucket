from django.db import models


class ContactMessage(models.Model):
    """
    Model representing a contact message sent by a user.

    Attributes:
        name (models.CharField): The name of the person sending the message.
        email (models.EmailField): The email address of the sender.
        subject (models.CharField): The subject of the message.
        message (models.TextField): The content of the contact message.
        created_at (models.DateTimeField): The date and time when the message
                                           was created. Automatically set to
                                           the current date and time when the
                                           message is created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
