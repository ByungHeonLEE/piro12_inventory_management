from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=30, verbose_name='거래처이름')
    telephone=models.CharField(max_length=13, verbose_name='전화번호')
    address=models.CharField(max_length=50, verbose_name='주소')

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name=models.CharField(max_length=20, verbose_name='상품명')
    image=models.ImageField(null=True, blank=True, upload_to='shop/images', verbose_name='제품사진')
    description=models.TextField(null=True, blank=True, verbose_name='상품설명')
    price=models.IntegerField(verbose_name='제품가격')
    left=models.IntegerField(verbose_name='남은수량')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='제품등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='업데이트일')

    def __str__(self):
        return self.product_name