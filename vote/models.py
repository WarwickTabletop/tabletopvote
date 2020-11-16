import uuid
from django.db import models


class Election(models.Model):
    name = models.CharField(max_length=30)
    max_votes = models.PositiveSmallIntegerField()
    active = models.BooleanField()
    intro = models.TextField(blank=True, help_text="The text to display at the top of the election. HTML enabled")

    def __str__(self):
        return self.name


class Option(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=50)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def formid(self):
        return "option_" + str(self.election.id) + "_" + str(self.id)

    def __str__(self):
        return self.text

    def votes(self):
        return self.vote_set.count()


# Create your models here.
class Vote(models.Model):
    ip = models.GenericIPAddressField(editable=False)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    selections = models.ManyToManyField(Option)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)
