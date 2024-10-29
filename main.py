from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QFont
from openai import OpenAI
from dotenv import load_dotenv
import sys
import os
from datetime import datetime

class ChatWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initializeOpenAI()
    self.initUI()
    
  def initializeOpenAI(self):
    # .env 파일 로드
    load_dotenv()
    self.client = OpenAI(api_key=os.getenv("API_KEY"))
    
    # prompt.txt에서 초기 시스템 메시지 읽기
    with open("prompt.txt", "r") as prompt_file:
      initial_message = prompt_file.read().strip()
    
    # 초기 시스템 메시지 설정
    self.messages = [
      {"role": "system", "content": initial_message}
    ]
    
    # responses 폴더 및 파일 설정
    if not os.path.exists("responses"):
      os.makedirs("responses")
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    self.file_name = f"responses/response_{current_time}.txt"
    
    # 대화 내용 저장 파일 초기화
    with open(self.file_name, "w") as response_file:
      response_file.write("==================== Prompt ====================\n")
      response_file.write(f"{initial_message}\n\n")
      response_file.write("==================== Chat Log ====================\n")
  
  def initUI(self):
    # 메인 윈도우 설정
    self.setWindowTitle('OpenAI Chat')
    self.setGeometry(100, 100, 800, 600)
    
    # 중앙 위젯 생성
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    
    # 레이아웃 설정
    layout = QVBoxLayout(central_widget)
    
    # 채팅 표시 영역
    self.chat_display = QTextEdit()
    self.chat_display.setReadOnly(True)
    self.chat_display.setFont(QFont('Arial', 10))
    layout.addWidget(self.chat_display)
    
    # 입력 영역 컨테이너
    input_container = QWidget()
    input_layout = QHBoxLayout(input_container)
    
    # 메시지 입력 필드
    self.message_input = QLineEdit()
    self.message_input.setFont(QFont('Arial', 10))
    self.message_input.returnPressed.connect(self.send_message)
    input_layout.addWidget(self.message_input)
    
    # 버튼 컨테이너
    button_container = QWidget()
    button_layout = QHBoxLayout(button_container)
    
    # 전송 버튼
    send_button = QPushButton('Send')
    send_button.clicked.connect(self.send_message)
    button_layout.addWidget(send_button)
    
    # 종료 버튼
    exit_button = QPushButton('Exit')
    exit_button.clicked.connect(self.close_application)
    button_layout.addWidget(exit_button)
    
    input_layout.addWidget(button_container)
    layout.addWidget(input_container)
    
    # 초기 메시지 표시
    self.chat_display.append("채팅을 시작합니다. 메시지를 입력하세요.")
    self.chat_display.append("종료하려면 'exit' 또는 'quit'를 입력하거나 Exit 버튼을 클릭하세요.")
  
  @pyqtSlot()
  def send_message(self):
    user_message = self.message_input.text().strip()
    if not user_message:
      return
    
    # 종료 명령어 확인
    if user_message.lower() in ['exit', 'quit']:
      self.close_application()
      return
    
    # 사용자 메시지 표시 및 저장
    self.chat_display.append(f"\nUser: {user_message}")
    with open(self.file_name, "a") as response_file:
      response_file.write(f"User: {user_message}\n")
    
    # OpenAI에 메시지 전송
    self.messages.append({"role": "user", "content": user_message})
    
    # AI 응답 받기
    response = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=self.messages,
      temperature=0.7,
    )
    
    ai_message = response.choices[0].message.content
    
    # AI 응답 표시 및 저장
    self.chat_display.append(f"\nAI: {ai_message}")
    with open(self.file_name, "a") as response_file:
      response_file.write(f"AI: {ai_message}\n")
    
    # 메시지 기록 업데이트
    self.messages.append({"role": "assistant", "content": ai_message})
    
    # 입력 필드 초기화
    self.message_input.clear()
    
    # 스크롤을 항상 최하단으로
    self.chat_display.verticalScrollBar().setValue(
      self.chat_display.verticalScrollBar().maximum()
    )
  
  def close_application(self):
    # 종료 메시지를 파일에 저장
    with open(self.file_name, "a") as response_file:
      response_file.write("\n==================== Chat Ended ====================\n")
    # 애플리케이션 종료
    QApplication.quit()

def main():
  app = QApplication(sys.argv)
  chat_window = ChatWindow()
  chat_window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()