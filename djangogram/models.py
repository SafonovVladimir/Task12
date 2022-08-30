from datetime import date
from django.db import models
from django.contrib.auth.models import User


# Расширюємо User Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Ім'я користувача")
    full_name = models.CharField("Повне ім'я", blank=True, max_length=150)
    e_mail = models.EmailField("E-mail")
    birthday = models.DateField("Дата народження", default=date.today, blank=True)
    gender = models.CharField("Стать", max_length=5, blank=True)
    bio = models.TextField("Про себе", blank=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


class Tag(models.Model):
    title = models.CharField('Назва', max_length=50)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    content = models.TextField("Що у вас нового", blank=True)
    likes = models.PositiveSmallIntegerField("Кількість лайків", default=0)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='post_tag')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Like(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
