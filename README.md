# 메디럭스 X 블루시그넘 기업프로젝트 3조

기업 프로젝트 프롬프트 엔지니어링
<br/><br/>

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

콘솔 입출력이 불편한 경우, `gui-version` 브랜치에서 실행해 채팅 인터페이스 사용 가능
