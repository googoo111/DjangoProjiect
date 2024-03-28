from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除不需要登录就能访问的页面
        # request.path_info
        if request.path_info in ['/login/', '/image/code/']:
            return
        # 1.读取当前访问的用户session信息，如果能读取到，说明已登录
        info_dict = request.session.get("info")
        if info_dict:
            return
        return redirect("/login/")