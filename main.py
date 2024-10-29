from openai import OpenAI
from dotenv import load_dotenv
import os

def ask_openai(client, messages):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
  )
  answer = response.choices[0].message.content
  
  # 응답 텍스트를 파일에 저장
  with open("response.txt", "a") as response_file:
    response_file.write(f"AI: {answer}\n")
  
  return answer

def initialize_chat():
  # .env 파일 로드
  load_dotenv()
  client = OpenAI(api_key=os.getenv("API_KEY"))
  
  # prompt.txt에서 초기 시스템 메시지 읽기
  with open("prompt.txt", "r") as prompt_file:
    initial_message = prompt_file.readline().strip()
  
  # 초기 시스템 메시지 설정
  messages = [
    {"role": "system", "content": initial_message}
  ]
  
  # 대화 내용 저장 파일 초기화
  with open("response.txt", "w") as response_file:
    response_file.write("Conversation Log\n")
  
  return client, messages

def chat_loop(client, messages):
  print("대화를 시작합니다. 종료하려면 'exit' 또는 'quit'를 입력하세요.")
  
  while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
      break
    
    # 유저 입력을 파일에 저장
    with open("response.txt", "a") as response_file:
      response_file.write(f"User: {user_input}\n")
    
    messages.append({"role": "user", "content": user_input})
    
    answer = ask_openai(client, messages)
    print(f"AI: {answer}")
    
    messages.append({"role": "assistant", "content": answer})

def main():
  client, messages = initialize_chat()
  chat_loop(client, messages)

if __name__ == "__main__":
  main()