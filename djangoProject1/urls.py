from django.urls import path
from Web.views import depart, user, pretty, admin, account

urlpatterns = [
    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/',depart.depart_add),
    path('depart/delete/',depart.depart_delete),
    path('depart/<int:nid>/edit/',depart.depart_edit),

    # 用户管理
    path('user/list/', user.user_list),
    # path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_from_add),
    path('user/<int:nid>/edit/',user.user_edit),
    path('user/<int:nid>/delete/',user.user_delete),

    # 靓号管理
    # path('prettynum/list/', pretty.prettynum_list),
    # path('prettynum/model/form/add/',pretty.prettynum_model_form_add),
    # path('prettynum/<int:nid>/edit/',pretty.prettynum_edit),
    # path('prettynum/<int:nid>/delete/',pretty.prettynum_delete),

    # 管理员的管理
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),
]
