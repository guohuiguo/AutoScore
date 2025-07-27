import os
import qianfan

# 设置环境变量来初始化认证信息（确保替换为真实的 AK/SK）
os.environ["QIANFAN_ACCESS_KEY"] = "your own Qianfan Access Key"  # 替换为你的 Qianfan Access Key
os.environ["QIANFAN_SECRET_KEY"] = "your own Qianfan Secret Key"  # 替换为你的 Qianfan Secret Key

# 初始化 chat_comp
chat_comp = qianfan.ChatCompletion()


# 多轮对话评分
def chat(q, a):
    resp = chat_comp.do(model="ERNIE-Speed-Pro-128K", messages=[
        {"role": "user",
         "content": '老师会问一个问题，学生会回答一个答案，对学生的答案评分,你的回答格式只能是"评分："给出在0-10范围内的整数分数'},
        {"role": "user", "content": q},  # 问题
        {"role": "user", "content": a}  # 答案
    ])

    # 输出响应的评分结果
    print(resp["body"]['result'])
    return resp["body"]['result']  # 返回评分结果