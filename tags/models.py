from django.db import models
from django.utils.text import Truncator
from django.utils.html import format_html

class Tag(models.Model):
    TAG_TYPES = (
        ('badge-default', 'badge-default'),
        ('badge-primary', 'badge-primary'),
        ('badge-secondary', 'badge-secondary'),
        ('badge-success', 'badge-success'),
        ('badge-danger', 'badge-danger'),
        ('badge-warning', 'badge-warning'),
        ('badge-info', 'badge-info'),
        ('badge-light', 'badge-light'),
        ('badge-dark', 'badge-dark'),
    )
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=TAG_TYPES, help_text='''
        <font size='5em'><span class="badge badge-pill badge-default" style="margin-left: -10px">Default</span></font>
    ''')
    detail = models.TextField(max_length=1025)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.name

    def short_detail(self):
        return Truncator(self.detail).chars(30)

    short_detail.admin_order_field = 'detail'
    short_detail.short_description = 'detail'

    def preview(self):
        return format_html('<span class="badge badge-pill %s">%s</span>' % (self.type, self.name))
    
    preview.admin_order_field = 'type'
    preview.short_description = 'preview'
