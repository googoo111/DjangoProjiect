from django.shortcuts import render,redirect
from Web import models
from Web.utils.pagination import Pagination
def depart_list(request):
    """部门列表"""
    # 去数据库中获取所有部门列表
    queryset = models.Department.objects.all()
    page_object = Pagination(request, queryset, page_size=10)
    context = {'queryset': page_object.page_queryset,
               'page_string': page_object.html()
               }
    return render(request,'depart_list.html',context)

def depart_add(request):
    """添加部门"""
    if request.method == 'GET':
        return render(request,'depart_add.html')

    # 获取提交数据
    title = request.POST.get('title')
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回部门列表
    return redirect('/depart/list/')

def depart_delete(request):
    """删除部门"""
    # 获取ID
    nid = request.GET.get('nid')
    # 删除数据
    models.Department.objects.filter(id=nid).delete()
    # 跳转回部门列表
    return redirect('/depart/list/')

def depart_edit(request,nid):
    """修改部门"""
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id,row_object.title)

        return render(request,'depart_edit.html',{'row_object':row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list/')
