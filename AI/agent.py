from openai import OpenAI

SYSTEM_PROMPT = (
    "You are an assistant specialized in AWS certifications and related cloud technologies "
    "(EC2, S3, IAM, Lambda, RDS, VPC, networking, security, DevOps, serverless, etc.).\n\n"
    "Your goals are:\n"
    "- Answer questions clearly, concisely, and in a didactic way.\n"
    "- Use simple examples whenever possible.\n"
    "- Avoid unnecessary filler text.\n"
    "- If the question is not related to AWS or cloud, politely redirect the user back to the main topic.\n"
)


class Agent:
    def __init__(self):
        self.client = OpenAI()

    def get_response(self, user_message: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",  # mais barato e rápido, pode trocar por gpt-4.1 se quiser
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.4,   # respostas mais consistentes
            max_tokens=500     # evita estourar em tokens
        )
        return response.choices[0].message.content
