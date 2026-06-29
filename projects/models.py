from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True, help_text="Upload project screenshot.")
    technologies = models.CharField(
        max_length=250, 
        help_text="Comma-separated list of technologies used (e.g., Django, Python, SQLite)"
    )
    github_link = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    live_link = models.URLField(blank=True, null=True, help_text="Live project demo URL")
    order = models.IntegerField(default=0, help_text="Sort order (ascending)")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(",") if tech.strip()]
