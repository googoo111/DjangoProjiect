from Web import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from Web.utils.boootstrap import BootStrapModelForm

class UserModelform(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'})
       )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age','salary','create_time','gender','depart']

class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price','level','status']

    #   验证方法2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return txt_mobile

class PrettyEditMOdelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price','level','status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for mobile, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control','placeholder':field.label}
    #   验证:方法2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return txt_mobile