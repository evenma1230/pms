from venv import create
from django.db import models

# Create your models here.



class MockOption(models.Model):
    stat_choices=[
        (0,"启用"),
        (1,"禁止")
    ]
    modulename=models.CharField(max_length=128,help_text='配置项目名称')
    stat=models.SmallIntegerField(choices=stat_choices,help_text="是否启用mock功能")
    createtime=models.DateTimeField( auto_now=False, auto_now_add=True)
    lstuptime=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    class Meta:
        db_table = 'MockOption'
        verbose_name = 'MockOption'
        verbose_name_plural = 'MockOption'
        
    def __str__(self) -> str:
        return self.modulename


class ApiDetail(models.Model):
    modulename=models.CharField(max_length=50,blank=False)
    modeleapi=models.CharField(max_length=128,blank=False)
    mkadrress=models.CharField(max_length=128,blank=False)
    retsuccess=models.TextField(help_text="success数据")
    retfail=models.TextField(help_text="失败数据",null=True)
    createtime=models.DateTimeField(auto_now=False, auto_now_add=True)
    lstuptime=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.modulename
    
    
    
    class Meta:
        db_table = 'ApiDetail'
        verbose_name = 'pms'
        verbose_name_plural = 'ModelNames'