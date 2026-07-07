import glob
import re

def main():
    new_nl_btn = 'onclick="const inp=this.previousElementSibling; if(inp && inp.value && inp.value.includes(\'@\')){window.location.href=\'404.html\'}else{alert(\'Please enter a valid email address.\')}"'
    
    for filepath in glob.glob("*.html"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content

        # 1. Fix the chat button in user-dashboard.html
        if 'user-dashboard.html' in filepath:
            old_chat = '<a href="404.html" class="chat-snd" style="text-decoration: none; display: inline-block;">'
            new_chat = '<a href="404.html" class="chat-snd" style="text-decoration: none; display: flex;">'
            content = content.replace(old_chat, new_chat)

        # 2. Fix validateFooterNL
        old_nl_btn = 'onclick="validateFooterNL(this)"'
        content = content.replace(old_nl_btn, new_nl_btn)

        # 3. Fix subscribeNewsletter() and mainSubscribe() and bare Subscribe buttons
        content = re.sub(r'<button onclick="[^"]*">Subscribe</button>', f'<button {new_nl_btn}>Subscribe</button>', content)
        content = re.sub(r'<button>Subscribe</button>', f'<button {new_nl_btn}>Subscribe</button>', content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")

if __name__ == "__main__":
    main()
