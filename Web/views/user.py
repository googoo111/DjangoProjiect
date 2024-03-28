from django.shortcuts import render,redirect
from Web import models
from Web.utils.pagination import Pagination
from Web.utils.form import UserModelform

def user_list(request):
    """用户管理"""
    queryset = models.UserInfo.objects.all()
    page_object = Pagination(request, queryset,page_size=10)
    context = {'queryset':page_object.page_queryset,
               'page_string':page_object.html()
               }
    return render(request,'user_list.html',context)

# ModelForm（）示例
def user_model_from_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == 'GET':
        form = UserModelform()
        return render(request,'user_model_form_add.html',{'form':form})

    # 校验数据 提交post数据
    form = UserModelform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    # 校验失败 ，在页面显示错误信息
    return render(request, 'user_model_form_add.html', {'form': form})
def user_edit(request, nid):
    """编辑用户"""
    # 根据ID去数据库获取相应的对象
    if request.method == 'GET':

        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelform(instance=row_object)
        return render(request,'user_edit.html',{'form':form})
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelform(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_edit.html', {'form':form})
def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')