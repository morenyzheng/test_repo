import os
from dashscope import Application
from dotenv import load_dotenv

load_dotenv()

response = Application.call(
    api_key=os.environ['DASHSCOPE_API_KEY'],
    app_id='08cd879c956b4752916c1f38349bae49',
    prompt='用遗传规划来挖掘选股因子需要在什么地方改进'
)
print(response.output.text)
