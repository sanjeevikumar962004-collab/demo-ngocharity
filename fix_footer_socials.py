import glob
import re

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # 1. Update FontAwesome CDN to 6.6.0 to support fa-x-twitter
    content = content.replace(
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"
    )

    # 2. Update X brand color in CSS to white (instead of Twitter blue)
    content = content.replace(".soc-card.tw i{color:#1da1f2}", ".soc-card.tw i{color:#fff}")
    content = content.replace(".soc-card.tw i { color: #1da1f2; }", ".soc-card.tw i { color: #fff; }")
    content = content.replace(".soc-card.tw i{color: #1da1f2}", ".soc-card.tw i{color: #fff}")

    # 3. Update footer grid column layouts (removing the 4th column from grid template)
    content = content.replace("grid-template-columns: 1.2fr 1fr 1fr 1.2fr;", "grid-template-columns: 1.2fr 1fr 1fr;")
    content = content.replace("grid-template-columns:1.2fr 1fr 1fr 1.2fr;", "grid-template-columns:1.2fr 1fr 1fr;")
    content = content.replace("grid-template-columns: 1.2fr 1fr 1fr 1.2fr", "grid-template-columns: 1.2fr 1fr 1fr")

    # 4. Remove the Recent News column from the footer
    # Using re.sub to match across lines resiliently
    news_pattern = r'<div class="footer-col">\s*<h4>Recent News\s*:\s*</h4>.*?</div>\s*</div>\s*(?=\s*<div class="footer-bottom">|\s*</footer>)'
    content = re.sub(news_pattern, '</div>\n', content, flags=re.DOTALL)

    # 5. Locate and update the social links in the footer.
    # We want to replace the entire <ul class="social-links">...</ul> block with updated links to 404.html including X and Threads.
    new_social_links = """<ul class="social-links">
    <li>
        <a href="404.html">
            <i class="fa-brands fa-facebook-f"></i> Facebook
        </a>
    </li>

    <li>
        <a href="404.html">
            <i class="fa-brands fa-instagram"></i> Instagram
        </a>
    </li>

    <li>
        <a href="404.html">
            <i class="fa-brands fa-linkedin-in"></i> LinkedIn
        </a>
    </li>

    <li>
        <a href="404.html">
            <i class="fa-brands fa-youtube"></i> YouTube
        </a>
    </li>

    <li>
        <a href="404.html">
            <i class="fa-brands fa-x-twitter"></i> X
        </a>
    </li>

    <li>
        <a href="404.html">
            <i class="fa-brands fa-threads"></i> Threads
        </a>
    </li>
</ul>"""

    social_pattern = r'<ul class="social-links">.*?</ul>'
    content = re.sub(social_pattern, new_social_links, content, flags=re.DOTALL)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")

def main():
    for filepath in glob.glob("*.html"):
        update_html_file(filepath)

if __name__ == "__main__":
    main()
