from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

def ask_openai(client, messages, file_name):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
  )
  answer = response.choices[0].message.content
  
  # 응답 텍스트를 파일에 저장
  with open(file_name, "a") as response_file:
    response_file.write(f"Lime AI: {answer}\n\n")
  
  return answer

def initialize_chat():
  # .env 파일 로드
  load_dotenv()
  client = OpenAI(api_key=os.getenv("API_KEY"))
  
  # prompt.txt에서 초기 시스템 메시지 읽기
  with open("prompt.txt", "r") as prompt_file:
    initial_message = prompt_file.read().strip()
  
  # 초기 시스템 메시지 설정
  messages = [
    {"role": "system", "content": initial_message},
    {"role": "assistant", "content": "안녕하세요, Lime AI에 오신 것을 환영합니다!"}
  ]
  
  # responses 폴더가 없으면 생성
  if not os.path.exists("responses"):
    os.makedirs("responses")
  
  # 파일 이름을 현재 날짜와 시간으로 설정
  current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
  file_name = f"responses/response_{current_time}.txt"
  
  # 대화 내용 저장 파일 초기화
  with open(file_name, "w") as response_file:
    response_file.write("==================== Prompt ====================\n")
    response_file.write(f"{initial_message}\n\n")
    response_file.write("==================== Chat Log ====================\n\n")
    response_file.write("Lime AI: 안녕하세요, Lime AI에 오신 것을 환영합니다!\n\n")
  return client, messages, file_name

def chat_loop(client, messages, file_name):
  # print("대화를 시작합니다. 종료하려면 'exit' 또는 'quit'를 입력하세요.\n")
  print("안녕하세요, Lime AI에 오신 것을 환영합니다!\n대화를 종료하려면 'exit' 또는 'quit'를 입력하세요\n")

  while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
      break

    # 유저 입력을 파일에 저장
    with open(file_name, "a") as response_file:
      response_file.write(f"User: {user_input}\n")
    
    messages.append({"role": "user", "content": user_input})
    
    answer = ask_openai(client, messages, file_name)
    print(f"\nLime AI: {answer}\n")
    
    messages.append({"role": "assistant", "content": answer})

def main():
  client, messages, file_name = initialize_chat()
  chat_loop(client, messages, file_name)

if __name__ == "__main__":
  main()