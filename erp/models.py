from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class ProductModel(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    class Meta:
        db_table = 'product'
    codes = (
        ('hood-001', 'hood-001'),
        ('hood-002', 'hood-002'),
        ('hood-003', 'hood-003'),
        ('jean-001', 'jean-001'),
    )
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('X', 'XLarge'),
        ('F', 'Free'),
    )
    code = models.CharField(choices=codes, max_length=8)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default='상품설명 입력')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        new_stock = Inventory()
        new_stock.product = self
        new_stock.stock_count = 0
        new_stock.save()


class Inventory(models.Model):
    class Meta:
        db_table = 'inventory'
    """
	창고의 제품과 수량 정보를 담는 모델입니다.
	상품, 수량 필드를 작성합니다.
	작성한 Product 모델을 OneToOne 관계로 작성합시다.
	"""
    product = models.OneToOneField(
        ProductModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    stock_count = models.IntegerField(validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.code}-{self.product.name}-{self.product.size}'


class InBound(models.Model):
    """
    입고 모델입니다.
    상품코드, 수량, 날짜, 금액 필드를 가집니다.
    """
    class Meta:
        db_table = 'inbound'
    code_name_size = models.ForeignKey(Inventory, on_delete=models.CASCADE,)
    inbound_date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.code_name_size.stock_count += self.amount
        self.code_name_size.save()


class OutBound(models.Model):
    """
    출고 모델입니다.
    상품코드, 수량, 날짜, 금액 필드를 가집니다.
    """
    class Meta:
        db_table = 'outbound'
    code_name_size = models.ForeignKey(Inventory, on_delete=models.CASCADE,)
    outbound_date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.code_name_size.stock_count -= self.amount
        self.code_name_size.save()