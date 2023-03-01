from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "mikan0313@protonmail.com",
  "password": "WNy92dmmEUXDQkV"
})

digest_base_prompt = """# 命令書: あなたはプロの編集者です。以下の制約条件と入力文をもとに、最高の要約を出力してください。

# 制約条件:
・1行目に見出しを書き、2行目以降に要約を書く
・文字数は300文字程度。
・重要なキーワードを取り残さない。
・文章を簡潔に。

# 入力文: """

output_file = open("output.txt", "a")

with open("theme.txt") as f:
    for theme_text in f:
        print(theme_text)
        prev_text = ""
        for data in chatbot.ask(
            digest_base_prompt + theme_text,
        ):
            message = data["message"][len(prev_text) :]
            
            print(message, end="", flush=True)
            prev_text = data["message"]

        output_file.write(prev_text + "\n")
        output_file.flush()
        print("\n\n")

print()

output_file.close()