from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=200, default="University of Management and Technology (UMT)")
    degree = models.CharField(max_length=200, default="Bachelor of Computer Science")
    status = models.CharField(max_length=100, default="Undergraduate")
    start_year = models.IntegerField(default=2022)
    end_year = models.IntegerField(null=True, blank=True, help_text="Leave blank if currently pursuing")
    description = models.TextField(blank=True, help_text="Optional description of key courses or achievements.")
    order = models.IntegerField(default=0, help_text="Sort order (ascending)")

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education Records"
        ordering = ['order', '-start_year']

    def __str__(self):
        return f"{self.degree} at {self.institution}"
