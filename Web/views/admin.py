from django.shortcuts import render,redirect
from django import forms
from Web import models
from django.core.exceptions import ValidationError
from Web.utils.pagination import Pagination
from Web.utils.boootstrap import BootStrapModelForm
from Web.utils.encrypt import md5

def admin_list(request):
    """管理员列表"""
    # 检查用户是否已登录 已登录，继续往下走，未登录，跳转回登录界面

    # 构造搜索条件
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_objict = Pagination(request,queryset)
    context = {
        'queryset': page_objict.page_queryset,
        'page_string':page_objict.html(),
        'search_data':search_data
    }
    return render(request, 'admin_list.html',context)

class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm

class AdminEditModelform(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['password','confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        # 去数据库校验当前密码与新输入密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能和以前密码相同")

        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm
def admin_add(request):
    """添加管理员"""
    tittle = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form":form, "tittle":tittle})

    form = AdminModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, "change.html", {"form":form, "tittle":tittle})

def admin_edit(request,nid):
    """编辑管理员"""
    # 对象 / None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    tittle = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelform(instance=row_object)
        return render(request, "change.html", {"form":form, "tittle":tittle})
    form = AdminEditModelform(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, "change.html", {"form": form, "tittle": tittle})
def admin_delete(request,nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def admin_reset(request,nid):
    """重置密码"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')

    tittle = "重置密码 -{}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "change.html", {"form":form, "tittle":tittle})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, "change.html", {"form":form, "tittle":tittle})