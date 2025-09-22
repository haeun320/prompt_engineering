# 메디럭스 X 블루시그넘 기업프로젝트 3조

기업 프로젝트 프롬프트 엔지니어링

- 프로젝트 기간: 2024.10.26 ~ 2024.11.2
- **‘산후 우울증 또는 우울감을 겪고 있는 30대 초반’** 을 마이크로 타겟팅해서, 상담이 원활히 이루어지는 프롬프트를 도출
- 심리상담에서 사용하는 ‘ABC 프레임워크’를 통한 문제 분석 및 감정 탐색이 가능한 AI 상담사 만들기

<br/>

| 프로젝트 개요 |
|:-------------:|
| ![프로젝트 3조 최종_pages-to-jpg-0001](https://github.com/user-attachments/assets/528abfd5-b39d-416c-8cd7-f7e874cb046f) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0002](https://github.com/user-attachments/assets/516cd3b0-43b7-4459-8e9b-070ecbbe4201) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0003](https://github.com/user-attachments/assets/63b5c509-5908-475f-b3e8-fe9b08df307a) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0013](https://github.com/user-attachments/assets/9918f220-85fc-4ea8-8c62-7fb6a1d37f94) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0019](https://github.com/user-attachments/assets/71c4c6e4-6a31-4195-a5c0-ff47fd2ba4bb) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0020](https://github.com/user-attachments/assets/8dc1f184-5726-4929-9d65-84717b0cbcc9) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0021](https://github.com/user-attachments/assets/351bac72-16a8-4f92-a384-610e125f949a) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0022](https://github.com/user-attachments/assets/05004d7a-cc0b-4eaa-ab28-1a8446166fd6) |
| ![블루시그넘 X 메디럭스 기업 프로젝트 3조 최종_pages-to-jpg-0023](https://github.com/user-attachments/assets/bff5c000-458e-4df3-83f6-78d07b419437) |


## ⚙️ 설정

1. 깃 클론

2. 라이브러리 설치

- OpenAI API

```
pip install openai
```

- python-dotenv

```
pip install python-dotenv
```

3. 프로젝트 폴더에 `.env` 파일 생성

4. `.env` 파일에 api key 저장

```
API_KEY=받은 api key
```

<br/>

## 🤖 프롬프트 엔지니어링

1. `prompt.txt` 에 프롬프트 입력

2. `main.py` 실행
3. 콘솔 입력을 통해 대화 시작
4. `quit` 또는 `exit`를 입력해 대화 종료
5. `response.txt`에 대화 내역 저장

콘솔 입출력이 불편한 경우, `gui-version` 브랜치에서 실행해 **채팅 인터페이스** 사용 가능
