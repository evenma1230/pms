import code
from time import time
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pms import models
import requests,json

# Create your views here.



# retfail={
#         "code": "SUCCESS",
#         "message": "提交成功",
#         "retcode": "FAIL",
#         "retmsg": "查询不到商品促销数据"
#         }

# retsucess={
#     "code": "SUCCESS",
#     "message": "提交成功",
#     "result": [
#         {
#             "activityId": "15836",
#             "ruleEndDate": "2022-10-31 23:59:59",
#             "ruleList": [
#                 {
#                     "preferentialDescription": "满数量1.000特价11.000",
#                     "preferentialType": 1,
#                     "preferentialValue": 11.0,
#                     "triggerType": 1,
#                     "triggerValue": 1.0
#                 }
#             ],
#             "ruleStartDate": "2022-09-16 00:00:00",
#             "spuCode": "000001",
#             "templateId": "10016",
#             "templateName": "单品特价"
#         },
#         {
#             "activityId": "15834",
#             "memCode": "F2022041410004",
#             "memName": "NF普通会员线下",
#             "payinfo": [
#                 8
#             ],
#             "ruleEndDate": "2022-10-31 23:59:59",
#             "ruleList": [
#                 {
#                     "preferentialDescription": "满数量1.000折扣%(1~100)95.000",
#                     "preferentialType": 2,
#                     "preferentialValue": 95.0,
#                     "promotionType": 0,
#                     "triggerType": 1,
#                     "triggerValue": 1.0
#                 }
#             ],
#             "ruleStartDate": "2022-09-16 00:00:00",
#             "spuCode": "000001",
#             "templateId": "10049",
#             "templateName": "单品折扣（支付）"
#         }
#     ],
#     "retcode": "SUCCESS",
#     "retmsg": "查询成功"
# }




@csrf_exempt
def spucodequery(request):
    #获取参数
    if request.method=="POST":
        mockoption=models.MockOption.objects.filter(modulename="pms",stat=1).first()
        if not mockoption:
            return JsonResponse(
                {"code":101,"msg":"未启用"}
            )
        
        
        data_obj=models.ApiDetail.objects.filter(modulename="pms").first()
        if data_obj:
            retsuccess=json.loads(data_obj.retsuccess)
            retfail=json.loads(data_obj.retfail)
        
            spuCodeIN=json.loads(request.body.decode()).get("spuCodeIN")
            
            if spuCodeIN!=retsuccess.get("result")[0].get("spuCode"):
                import time
                res=requests.request(
                    method="post",
                    url=f"{data_obj.mkadrress}/lhpmslabels/spucodequeryV1",
                    data={
                        "storeNo":4846,
                        "spuCodeIN":spuCodeIN,
                        "requestId":915100001,
                        "timestamp":str(time.time())[:6]
                    }
                )
                return JsonResponse(res.json())

            return JsonResponse(retsuccess)
        else:
            return JsonResponse(
                {"code":"101","msg":"未配置参数"}
            )

    else:
        return JsonResponse([],safe=False)