"""
LLM Cocktail 테스트용 샘플 앱
------------------------------
3개의 서로 다른 LLM API를 사용해 간단한 문서 처리 파이프라인을 구현한다.

이 스크립트는 LLM Cocktail의 "코드 자동 감지" 기능을 테스트하기 위한 용도로,
실제 서비스 로직이 아니라 각 API 호출 패턴을 최소한으로 보여주는 예제다.

필요한 환경변수:
  OPENAI_API_KEY
  ANTHROPIC_API_KEY
  GEMINI_API_KEY (또는 GOOGLE_API_KEY)
"""

import os

from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai


# ---------------------------------------------------------------------------
# 1. OpenAI - 문서 분류
# ---------------------------------------------------------------------------
def classify_document(text: str) -> str:
    """gpt-4o-mini를 사용해 문서를 카테고리로 분류한다."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "다음 문서를 '계약서', '보고서', '이메일', '기타' 중 하나로 분류하고 "
                "카테고리 이름만 출력해줘.",
            },
            {"role": "user", "content": text},
        ],
        max_tokens=20,
    )
    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# 2. Anthropic - 요약/추출
# ---------------------------------------------------------------------------
def summarize_document(text: str) -> str:
    """claude-3-5-sonnet을 사용해 문서를 3줄로 요약한다."""
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=200,
        messages=[
            {
                "role": "user",
                "content": f"다음 문서를 3줄로 요약해줘:\n\n{text}",
            }
        ],
    )
    return response.content[0].text.strip()


# ---------------------------------------------------------------------------
# 3. Google Gemini - 질의응답 (RAG QA)
# ---------------------------------------------------------------------------
def answer_question(context: str, question: str) -> str:
    """gemini-1.5-flash를 사용해 주어진 컨텍스트 기반으로 질문에 답한다."""
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY") or os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"다음 컨텍스트를 참고해서 질문에 답해줘.\n\n컨텍스트: {context}\n\n질문: {question}"
    response = model.generate_content(prompt)
    return response.text.strip()


# ---------------------------------------------------------------------------
# 실행 예시
# ---------------------------------------------------------------------------
def main():
    sample_doc = (
        "본 계약은 2026년 7월 6일 WVB와 협력사 간에 체결되었으며, "
        "AI 컨설팅 서비스 제공 조건과 비용 지급 일정을 규정한다."
    )

    print("=== 1. 문서 분류 (OpenAI gpt-4o-mini) ===")
    category = classify_document(sample_doc)
    print(f"분류 결과: {category}\n")

    print("=== 2. 문서 요약 (Anthropic claude-3-5-sonnet) ===")
    summary = summarize_document(sample_doc)
    print(f"요약 결과:\n{summary}\n")

    print("=== 3. 질의응답 (Google Gemini gemini-1.5-flash) ===")
    answer = answer_question(sample_doc, "이 문서는 언제 체결되었나?")
    print(f"답변: {answer}")


if __name__ == "__main__":
    main()
