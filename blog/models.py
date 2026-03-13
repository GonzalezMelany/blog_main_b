from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_lengh=225)

    class Meta:
        ordering = ('title')
        verbose_name_plural = 'Categorias'

        def _str_(self):
            return self.title
        
class Post(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = {
        (ACTIVE, 'Active'),
        (DRAFT, 'Draf')
    }

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class comment (models.Model):
    post  = models.ForeignKey(Post, related_name='Comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
