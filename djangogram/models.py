from datetime import date
from itertools import count

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOISES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Ім'я користувача")
    full_name = models.CharField("Повне ім'я", blank=True, max_length=150)
    e_mail = models.EmailField("E-mail")
    birthday = models.DateField("Дата народження", default=date.today, blank=True)
    gender = models.CharField("Стать", choices=GENDER_CHOISES, max_length=6, blank=True, default=None)
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
    liked = models.ManyToManyField(User, verbose_name="Кількість лайків", default=None, blank=True, related_name='liked')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='post_tag', blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    @property
    def num_of_likes(self):
        return self.liked.all().count()


LIKE_CHOISES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Like(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOISES, verbose_name="Value", default='Like', max_length=6)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
