from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200, default="Personal Projects Experience")
    description = models.TextField(help_text="Detailed text or bullet points explaining projects/academic experience.")
    order = models.IntegerField(default=0, help_text="Sort order (ascending)")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience Records"
        ordering = ['order']

    def __str__(self):
        return self.title
