# from django.shortcuts import render,redirect
# from Web import models
# from Web.utils.pagination import Pagination
# from Web.utils.form import PrettyModelForm,PrettyEditMOdelForm
#
# def prettynum_list(request):
#     """靓号列表"""
#
#     data_dict = {}
#     search_data =request.GET.get('q',"")
#     if search_data:
#         data_dict["mobile__contains"] = search_data
#
#     queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')
#     page_object = Pagination(request, queryset)
#
#     context = {
#         "search_data": search_data,
#
#         "queryset":page_object.page_queryset,  #分完页的数据
#
#         "page_string":page_object.html} #页码
#
#     return render(request,'prettynum_list.html',context)
# def prettynum_model_form_add(request):
#     """新建靓号"""
#     if request.method == 'GET':
#         form = PrettyModelForm()
#         return render(request,'prettynum_model_form_add.html',{'form':form})
#
#     # 校验数据 提交post数据
#     form = PrettyModelForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('/prettynum/list')
#     # 校验失败 ，在页面显示错误信息
#     return render(request, 'prettynum_model_form_add.html', {'form': form})
#
#
# def prettynum_edit(request,nid):
#     """编辑靓号"""
#     # 根据ID去数据库获取相应的对象
#     if request.method == 'GET':
#         row_object = models.PrettyNum.objects.filter(id=nid).first()
#         form = PrettyEditMOdelForm(instance=row_object)
#         return render(request,'prettynum_edit.html',{'form':form})
#     row_object = models.PrettyNum.objects.filter(id=nid).first()
#     form = PrettyEditMOdelForm(data=request.POST,instance=row_object)
#     if form.is_valid():
#         form.save()
#         return redirect('/prettynum/list/')
#
#     return render(request, 'prettynum_edit.html', {'form':form})
#
# def prettynum_delete(request,nid):
#     """删除号码"""
#     row_object = models.PrettyNum.objects.filter(id=nid).delete()
#     return redirect('/prettynum/list/')