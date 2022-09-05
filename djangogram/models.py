import uuid
from datetime import date
from PIL import Image as Im
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Profile(models.Model):

    def get_uniq_name(instance, filename):
        extension = filename.split('.')[-1]
        uniq_name = str(uuid.uuid4())[:8]
        return f'photos/users/{uniq_name}.{extension}'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Ім'я користувача")
    full_name = models.CharField("Повне ім'я", blank=True, max_length=150)
    e_mail = models.EmailField("E-mail", blank=True)
    birthday = models.DateField("Дата народження", default=date.today, blank=True)
    gender = models.CharField("Стать", choices=GENDER_CHOICES, max_length=6, blank=True, null=True)
    bio = models.TextField("Про себе", blank=True, null=True)
    photo = models.ImageField('Фото', upload_to=get_uniq_name, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


class Tag(models.Model):
    title = models.CharField('Tag', max_length=50, blank=True)
    url = models.SlugField(max_length=100, unique=True, blank=True)

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
    liked = models.ManyToManyField(User, verbose_name="Кількість лайків", default=None, blank=True,
                                   related_name='liked')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='posts', blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-updated_at']

    @property
    def num_of_likes(self):
        return self.liked.all().count()


LIKE_CHOISES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Image(models.Model):

    def get_uniq_name(instance, filename):
        extension = filename.split('.')[-1]
        uniq_name = str(uuid.uuid4())[:8]
        return f'photos/{uniq_name}.{extension}'

    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to=get_uniq_name, verbose_name='Фото', blank=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()
        img = Im.open(self.image.path)
        # resize
        output_size = (100, 100)
        img.thumbnail(output_size)
        img.save(self.image.path)

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
