from langchain_core.prompts import ChatPromptTemplate

def evaluation_prompt():

    return ChatPromptTemplate.from_template(
"""
You are a Senior Technical Interviewer.

Interview Conversation:

{history}

Evaluate the candidate.

Provide:

1. Technical Skills Score (0-10)
2. Communication Score (0-10)
3. Problem Solving Score (0-10)
4. Confidence Score (0-10)

5. Strengths
6. Weaknesses

7. Final Recommendation

Choose one:

- Strong Hire
- Hire
- Borderline
- Reject

Provide a detailed report.
"""
    )