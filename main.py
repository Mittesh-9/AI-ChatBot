import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role" : "user", "content" : prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ =="__main__":
    while True :
        user_input = input("You:")