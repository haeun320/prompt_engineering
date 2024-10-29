from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"))

# 프롬프트를 이용하여 모델 호출
def ask_openai(prompt):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ],
    temperature=0.7,
  )
  answer = response.choices[0].message.content
  
  # 응답 텍스트를 파일에 저장
  with open("response.txt", "w") as response_file:
    response_file.write(answer)

  return answer

# prompt.txt에서 프롬프트 텍스트 읽기
with open("prompt.txt", "r") as prompt_file:
  prompt_text = prompt_file.read().strip()

# 질문하고 결과 출력
result = ask_openai(prompt_text)
print(result)
