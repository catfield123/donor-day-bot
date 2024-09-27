import re

def escape_markdown_v2(text: str) -> str:
    markdown_v2_special_chars = r'_*[]()~`>#+-=|{}.!-'
    
    return re.sub(r'([%s])' % re.escape(markdown_v2_special_chars), r'\\\1', text)