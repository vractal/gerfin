from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(default="expense",max_length=40)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='entries')

    @property
    def get_amount(self):
        return "R$" + str(self.amount)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "entries"


class User(models.Model):
    name= models.CharField(default="robertinho", max_length=255)
    telegram_id = models.IntegerField()

    def __str__(self):
        return self.name


    def add_entry(self, amount,description='',type='expense'):
        Entry.objects.create(amount=amount,description=description, type=type, user=self)

    def get_entries(self):
        user = User.objects.get(telegram_id=self.telegram_id)
        return user.entries.all()

    @classmethod
    def get_user(cls,update):
        id =  update.effective_user.id
        try:
            user = cls.objects.get(telegram_id=id)
        except:
            if update.effective_user.username:
                username = update.effective_user.username
            else:
                username = update.effective_user.first_name

            user = cls.objects.create(telegram_id=id, name=username)

        return user
