from django import forms
from django.conf import settings


class MultiSelectWidget(forms.SelectMultiple):
    css_class = 'multiselect'

    class Media:
        css = {
            'all': (
                # settings.MEDIA_URL + 'css/themes/smoothness/jquery-ui-1.7.1.custom.css',
                settings.MEDIA_URL + 'multiselect/css/ui.multiselect.css',
            )
        }
        js = (
            # 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
            # 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js',
            settings.MEDIA_URL + 'multiselect/js/ui.multiselect.js',
        )

    def add_css_class(self, attrs):
        attrs = attrs or {}
        if 'class' in attrs:
            attrs['class'] += " %s" % self.css_class
        else:
            attrs['class'] = self.css_class
        return attrs

    def __init__(self, attrs=None):
        attrs = self.add_css_class(attrs)
        super(MultiSelectWidget, self).__init__(attrs=attrs)
