from django import forms

from .models import Post

#class PostForm(forms.Form):
#    title = forms.CharField()
#    description = forms.TextField()
#    image = forms.ImageField()
#    slug = forms.CharField()



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','slug']