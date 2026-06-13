from openai import OpenAI
import user_config

client = OpenAI(api_key=user_config.openai_key)

def ask_gpt(prompt):
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )
    return response.output_text
