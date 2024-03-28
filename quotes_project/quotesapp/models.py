from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=70, null=False, unique=True)
    birth_date = models.DateField(null=False)
    birth_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote} by {self.author}"
