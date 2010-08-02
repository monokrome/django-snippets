from django.db import models
from django.template.defaultfilters import slugify

class Snippet(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    code = models.TextField()
    slug = models.SlugField(blank=True)
    created_on = models.DateTimeField()

    @models.permalink
    def get_absolute_url(self):
        return ('snippet', [str(self.id)])

    def save(self, force_insert=False, force_update=False):
        if not self.created_on:
            self.created_on = datetime.now()

        self.slug = slugify(self.title)

        super(Snippet,self).save(force_insert, force_update)

    def __unicode__(self):
        return self.title

