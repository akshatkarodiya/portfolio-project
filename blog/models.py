from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField('images/')



# title
#pub_date
# body
# images

# add the blog app to the setting
# create a migration
# migrate
# add to the the admin
