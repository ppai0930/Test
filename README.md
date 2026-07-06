# LLM Cocktail 테스트용 샘플 앱

LLM Cocktail의 "코드 자동 감지" 기능을 테스트하기 위한 최소 예제입니다.
서로 다른 3개 제공사의 LLM API를 각각 다른 작업에 사용합니다.

| 작업 | 제공사 | 모델 |
|---|---|---|
| 문서 분류 | OpenAI | `gpt-4o-mini` |
| 문서 요약 | Anthropic | `claude-3-5-sonnet-20241022` |
| 질의응답 (RAG QA) | Google Gemini | `gemini-1.5-flash` |

## 설치

```bash
pip install -r requirements.txt
```

## 환경변수

```bash
export OPENAI_API_KEY="..."
export ANTHROPIC_API_KEY="..."
export GEMINI_API_KEY="..."   # 또는 GOOGLE_API_KEY
```

## 실행

```bash
python main.py
```

## 용도

이 repo(또는 폴더)를 LLM Cocktail에 등록할 때 GitHub 링크를 넣으면,
`main.py` 안의 `gpt-4o-mini`, `claude-3-5-sonnet-20241022`, `gemini-1.5-flash`
세 모델이 자동으로 감지되어 "현재 사용 모델"로 등록되는지 확인할 수 있습니다.
