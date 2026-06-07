from langchain_core.prompts import ChatPromptTemplate

def get_evaluation_prompt():

        return ChatPromptTemplate.from_template(
            """
You are a senior interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate:

1. Technical Accuracy (1-10)
2. Communication (1-10)
3. Confidence (1-10)

Provide feedback.

            """



        )




