from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=100, default="Laiba Tanseer")
    title = models.CharField(max_length=150, default="Computer Science Undergraduate")
    profile_picture = models.ImageField(upload_to="bio/", blank=True, null=True)
    summary = models.TextField(help_text="Professional summary of the user.")
    cv = models.FileField(upload_to="cv/", blank=True, null=True, help_text="Upload CV document.")
    email = models.EmailField(default="laibtanser@gmail.com")
    linkedin = models.CharField(max_length=100, default="laiba-tanseer", help_text="LinkedIn profile username/slug")
    typing_roles = models.TextField(
        default="Computer Science Student, AI Enthusiast, Backend Developer, Problem Solver",
        help_text="Comma-separated values for the typing animation effect in the hero section."
    )

    class Meta:
        verbose_name = "Biography"
        verbose_name_plural = "Biography"

    def __str__(self):
        return f"{self.name} - {self.title}"

    def get_typing_roles_list(self):
        return [role.strip() for role in self.typing_roles.split(",") if role.strip()]
