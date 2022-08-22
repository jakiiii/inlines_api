from django.db import models


class Author(models.Model):
    author = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Author"


class Books(models.Model):
    name = models.CharField(
        max_length=255
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='book'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
