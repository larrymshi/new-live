import datetime

from django.db import models


# 敏感词词库
class SensitiveWords(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=20)
    # 区分关键词 0为系统敏感关键词 1为用户敏感关键词 2通用或其他敏感关键词
    word_type = models.SmallIntegerField(default=0)

    class Meta:
        db_table = "sensitive_words"


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(default=0)
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    describe = models.CharField(max_length=200, null=True)
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = "product_type"


class PublicDataSource(models.Model):
    id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    source_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = "public_data_source"

        # 公共图片库


class PublicImages(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=500)
    # 图片类型 1：海报  2：剧照
    img_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = "public_images"


class PublicDownloadAddress(models.Model):
    id = models.AutoField(primary_key=True)
    download_url = models.CharField(max_length=1000)
    download_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = "public_download_address"


# product_type & detail 获取实际数据类型
class ProductInfo(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType)
    source = models.ForeignKey(PublicDataSource)
    detail = models.IntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    order_index = models.IntegerField(null=True)

    class Meta:
        db_table = "product_info"


class ProductMovieDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_alias = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    rating_sum = models.IntegerField(default=0)
    release_time = models.DateField(null=True, blank=True, default=datetime.date.today())
    about = models.TextField(null=True)
    content = models.TextField(null=True)
    # tag = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    status = models.SmallIntegerField(default=1)

    def get_desc(self):
        return self.content[0:20] + "..."

    def datetime_format(self):
        return datetime.datetime.strftime(self.release_time, "%Y-%m-%d")

    class Meta:
        db_table = "product_movie_detail"


class ProductSubTypeDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductInfo)
    sub_type = models.ForeignKey(ProductType)

    class Meta:
        db_table = "product_sub_type_detail"


# 产品图片详情表
class ProductImagesDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductInfo)
    image = models.ForeignKey(PublicImages)

    class Meta:
        db_table = "product_images_detail"


class ProductDownloadDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductInfo)
    address = models.ForeignKey(PublicDownloadAddress)

    class Meta:
        db_table = "product_download_detail"
