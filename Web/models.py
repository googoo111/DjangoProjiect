from django.db import models
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

class Department(models.Model):
    """学院表"""
    title = models.CharField(verbose_name='标题',max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """教师表"""
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    salary = models.DecimalField(verbose_name='薪水',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    # 无约束
    # dpart_id = models.BigIntegerField(verbose_name='部门ID')
    # 有约束
    # 生成depart_id
    # 级联删除
    # depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # 置空
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id",null=True,blank=True,on_delete=models.SET_NULL)

    # 在Django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name='号码',max_length=32)
    price = models.IntegerField(verbose_name='价格',default=0)
    level_choices = (
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4, '4级')
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices,default=1)

    status_choices = (
        (1,'已占用'),
        (2,'未占用'),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices,default=2)