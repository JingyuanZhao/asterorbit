
# 修复HTML实体编码问题

files = ['digest2_gui.py', 'digest2_gui_en.py']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换 &amp; 为 &amp;
    content = content.replace('&amp;', '&amp;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Fixed {file}')