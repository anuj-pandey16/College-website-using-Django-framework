from django.db import models

# Create Your Models Here.
class forms(models.Model):
    form_name = models.CharField(max_length=50)
    email = models.EmailField(default="Pics")
    phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    state = models.CharField(max_length=50)
    add = models.TextField()
    pincode = models.IntegerField()
    adm = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    def __str__(self):   
        return self.form_name

class pdf(models.Model):
    pdf_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='Pdf Folder',default="File")
    def __str__(self):
        return self.pdf_name

class media(models.Model):
    media = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Media',default="Pics")
    def __str__(self):
        return self.media
