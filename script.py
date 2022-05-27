from random import shuffle


code = '''
<h1 align="center">
  <b>Aditya Kadoo</b>
</h1>

<br>

<div align=center style="zoom: 1.2;">'''
# <div style="gap: 5px; display: flex; flex-wrap: row; justify-content: center;">'''
#   <img src="https://img.shields.io/badge/-HTML-c58545?style=for-the-badge&logo=html5&logoColor=c58545&labelColor=cde">
#   <img src="https://img.shields.io/badge/-CSS-d1a01f?style=for-the-badge&logo=css3&logoColor=d1a01f&labelColor=cde">
#   <img src="https://img.shields.io/badge/-python-98b982?style=for-the-badge&logo=python&logoColor=98b982&labelColor=cde">
#   <img src="https://img.shields.io/badge/-C++-8282b9?style=for-the-badge&logo=CPlusPlus&logoColor=8282b9&labelColor=cde">

badges = {
    # Languages
    'python': ('3776AB', 'python'),
    'c++': ('00599C', 'cplusplus'),
    'c': ('A8B9CC', 'c'),
    'java': ('007396', 'java'),
    # 'c sharp': ('239120', 'c-sharp'),
    'assembly': ('007AAC', 'assemblyscript'),
    # Frameworks n Softwares
    'git': ('F05032', 'git'),
    'vscode': ('007ACC', 'visual-studio-code'),
    # '.net': ('512BD4', '.net'),
    'sfml': ('8CC445', 'sfml'),
    'cmake': ('064F8C', 'cmake'),
    'docker': ('2496ED', 'docker'),
    # Web Development
    'html': ('E34F26', 'html5'),
    'css': ('1572B6', 'css3'),
    'javascript': ('F7DF1E', 'javascript'),
    'react': ('61DAFB', 'react'),
    'django': ('092E20', 'django'),
    'android studio': ('3DDC84', 'android-studio'),
    'fastapi': ('009688', 'fastapi'),
    'node.js': ('339933', 'node.js'),
    'npm': ('CB3837', 'npm'),
    'webpack': ('8DD6F9', 'webpack'),
    # Data Science
    'numpy': ('013243', 'numpy'),
    'plotly': ('3F4F75', 'plotly'),
    'scipy': ('8CAAE6', 'scipy'),
    'pytorch': ('EE4C2C', 'pytorch'),
    'tensorflow': ('FF6F00', 'tensorflow'),
    'jupyter': ('F37626', 'jupyter'),
    'spacy': ('09A3D5', 'spacy'),
    'colab': ('F9AB00', 'google-colab'),
    # Databases
    'sqlite': ('003B57', 'sqlite'),
    'postgresql': ('4169E1', 'postgresql'),
    'heroku': ('430098', 'heroku'),
    # Scripts
    'bash': ('4EAA25', 'gnu-bash'),
    'latex': ('008080', 'latex'),
    # Social
    # 'github': ('181717', 'github'),
    # 'codeforces': ('1F8ACB', 'codeforces'),
    # 'codechef': ('5B4638', 'codechef'),
    # 'hackerrank': ('00EA64', 'hackerrank'),
}

items = list(badges.items())
n = len(items)

for index, item in enumerate(items):
    skill, info = item
    # if index % 4 == 0:
    #     code += '''\n</div>\n<div style="display: flex; flex-wrap: row; justify-content: center;">'''
    code += f'''\n<img src="https://img.shields.io/badge/-{skill.capitalize()}-{info[0]}?style=for-the-badge&logo={info[1]}&logoColor={info[0]}&labelColor=fff">'''

code += '''
</div>

## My Statistics

[![Aditya's GitHub stats](https://github-readme-stats.vercel.app/api?username=adityakadoo&theme=cobalt)](https://github.com/anuraghazra/github-readme-stats)
'''

print(code)
