from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80, help_text="Enter percentage from 0 to 100")
    category = models.CharField(
        max_length=50, 
        default="Technical", 
        help_text="Category of the skill (e.g. Languages, Frameworks, AI, Databases)"
    )
    order = models.IntegerField(default=0, help_text="Sort order (ascending)")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"
