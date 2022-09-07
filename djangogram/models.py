import uuid
from datetime import date
from PIL import Image as Im
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    content = models.TextField("Що у вас нового", blank=True)
    liked = models.ManyToManyField(User, verbose_name="Кількість лайків", default=None, blank=True,
                                   related_name='liked')
    tags = TaggableManager()

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


#
# class UserFollowing(models.Model):
#     user_id = models.ForeignKey("User", related_name="following", on_delete=models.PROTECT())
#     following_user_id = models.ForeignKey("User", related_name="followers")
#     created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
