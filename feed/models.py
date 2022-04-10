from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.text[0:100]

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
