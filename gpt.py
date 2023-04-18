import openai
import argparse

SYSTEM_MESSAGE = """
You're a mean, sassy and sarcastic assistant of a person who uses severe self deprecation as a way to get motivation. Don't be kind anywhere and at anytime. Answer accordingly. Add some emojis in the sentence as well.
"""

def main():
    
    print("Starting GPT Shell Assistant 💫")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs = "+", type = str, help = "Prompt for GPT-3 to complete") # we're showing python that there can be multiple inputs
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    
    print("Argument being passed:", args.prompt)
    print("Question:", prompt)

    chat_history = []

    ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)

    # creating a loop for that GPT keeps asking the user for inputs
    user_input = input("Ask your question please: ")
    while user_input != "":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input("Ask your question please: ")
    
    print("Have a good day. Ending session 👋") # displaying a message when the user presses enter and wants to end the session

def ask_gpt(prompt: str, chat_history: list, system_message: str):
    
    openai.api_key = "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" # my api key
    
    user_prompt = {"role": "user", "content": prompt} #user prompt being defined as a separate object

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": system_message},
            *chat_history,
            user_prompt
        ]
    )
    content = response["choices"][0]["message"]["content"] # getting the answer from chat gpt
    
    chat_history.append(user_prompt) # user prompt being added to the chat history
    chat_history.append({"role": "assistant", "content": content}) # GPT's response being added to the chat history

    print("\033[92m" + content + "\033[0m") # printing the answer from GPT in green color

    return content


if __name__ == "__main__":
    main()