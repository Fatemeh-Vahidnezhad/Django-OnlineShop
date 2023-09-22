# from django.db import models
# from django.contrib.auth import get_user_model
# from django.utils import timezone


from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('productdetail', args=[self.id,])


class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text










# class Product(models.Model):
#     list_size = (
#         ('S', '36'),
#         ('M', '38'),
#         ('L', '40'),
#         ('XL', '42'),
#         ('XXL', '44'),
#         ('X3L', '46'),
#         ('X4L', '48'),
#         ('X5L', '50'),
#         ('X6L', '52'),
#         ('X7L', '54'),
#     )
#     category_choice = (
#         ('W', 'Bride dress'),
#         ('M', 'Formal dress'),
#     )
#     title = models.CharField(max_length=200, verbose_name='name of product')
#     description = models.TextField()
#     datetime_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
#     datetime_modified = models.DateTimeField(auto_now=True, null=True)
#     price = models.PositiveIntegerField()
#     # image = models.ImageField(blank=True)
#     size = models.CharField(choices=list_size, max_length=3)
#     category = models.CharField(choices=category_choice)
#     available = models.BooleanField(default=1)
#     stock = models.PositiveIntegerField()
#     release = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.title

    # def get_absolute_url(self):
    #     return reverse()


# class Comment (models.Model):
#     star_choice = [
#         ('very bad', '1'),
#         ('bad', '2'),
#         ('usual', '3'),
#         ('good', '4'),
#         ('excellent', '5'),
#
#     ]
#     body = models.TextField(verbose_name='comment text')
#     datetime_created_comment = models.DateTimeField(auto_now_add=True)
#     product = models.ForeignKey(
#         Product,
#         related_name='comments',
#         on_delete=models.CASCADE,
#     )
#     user = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#         related_name='comments',
#         verbose_name='comment author',
#     )
#     recommend = models.BooleanField(default=True)
#     publish = models.BooleanField(default=True)
#     stars = models.CharField(choices=star_choice, max_length=9)
#
#     def __str__(self):
#         return self.body
#






