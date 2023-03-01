from revChatGPT.V1 import Chatbot
import config

chatbot = Chatbot(config=config.config)

digest_base_prompt = """# 命令書: あなたはプロの編集者です。以下の制約条件と複数人が話す会議の入力文をもとに、最高の要約とその見出しを、出力文の例に従って出力してください。

# 制約条件:
・重要なキーワードを取り残さない。
・文章を簡潔に。
・どんな文章であっても要約を行う。
・要約の文字数は400文字程度。

# 入力文: {0}

# 出力文の例: 
要約: 
見出し: 「」"""

output_file = open("output.txt", "a")

with open("theme.txt") as f:
    for theme_text in f:
        print(theme_text)
        prev_text = ""
        for data in chatbot.ask(
            digest_base_prompt.format(theme_text),
        ):
            message = data["message"][len(prev_text) :]
            
            print(message, end="", flush=True)
            prev_text = data["message"]

        output_file.write(prev_text + "\n")
        output_file.flush()
        print("\n\n")

print()

output_file.close()