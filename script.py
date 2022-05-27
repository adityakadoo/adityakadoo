tokyonight = {
    'title_color': "70a5fd",
    'icon_color': "bf91f3",
    'text_color': "38bdae",
    'bg_color': "1a1b27",
  }


code = f'''
# <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px"> Hi there, this is Aditya!

I am an undergrad from IIT Bombay majoring in Computer Science. I love coding things from scratch. I even enjoy the designing, documenting and decorating parts of programming to the point where it feels like an OCD. Anyways, I am keenly interest in Data Science and Web Development.

## Profiles

[![LinkedIn: adityakadoo](https://img.shields.io/badge/-LinkedIn-{tokyonight["icon_color"]}?style=for-the-badge&logo=linkedin&logoColor=fff&labelColor={tokyonight["bg_color"]}&link=https://www.linkedin.com/in/aditya-kadoo-513284222/)](https://www.linkedin.com/in/aditya-kadoo-513284222/)
[![Github: adityakadoo](https://img.shields.io/badge/-Github-{tokyonight["icon_color"]}?style=for-the-badge&logo=github&logoColor=fff&labelColor={tokyonight["bg_color"]}&link=https://www.github.com/adityakadoo/)](https://www.github.com/adityakadoo/)
[![Codeforces: adityakadoo](https://img.shields.io/badge/-Codeforces-{tokyonight["icon_color"]}?style=for-the-badge&logo=codeforces&logoColor=fff&labelColor={tokyonight["bg_color"]}&link=https://codeforces.com/profile/Addi.sama)](https://codeforces.com/profile/Addi.sama)
[![Codechef: adityakadoo](https://img.shields.io/badge/-Codechef-{tokyonight["icon_color"]}?style=for-the-badge&logo=codechef&logoColor=fff&labelColor={tokyonight["bg_color"]}&link=https://www.codechef.com/users/aditya_kadoo)](https://www.codechef.com/users/aditya_kadoo)
[![Mail: adityakadoo](https://img.shields.io/badge/-Mail-{tokyonight["icon_color"]}?style=for-the-badge&logo=gmail&logoColor=fff&labelColor={tokyonight["bg_color"]}&link=mailto:aditya1449kadoo@gmail.com)](mailto:aditya1449kadoo@gmail.com)


## Skills

<code>
<br>

<div align=center style="zoom: 1.5;">'''
# <div style="gap: 5px; display: flex; flex-wrap: row; justify-content: center;">'''
#   <img src="https://img.shields.io/badge/-HTML-c58545?style=for-the-badge&logo=html5&logoColor=c58545&labelColor=cde">
#   <img src="https://img.shields.io/badge/-CSS-d1a01f?style=for-the-badge&logo=css3&logoColor=d1a01f&labelColor=cde">
#   <img src="https://img.shields.io/badge/-python-98b982?style=for-the-badge&logo=python&logoColor=98b982&labelColor=cde">
#   <img src="https://img.shields.io/badge/-C++-8282b9?style=for-the-badge&logo=CPlusPlus&logoColor=8282b9&labelColor=cde">

badges = {
    # Languages
    'Python': ('3776AB', 'python'),
    'C++': ('00599C', 'cplusplus'),
    'C': ('A8B9CC', 'c'),
    'Java': ('007396', 'java'),
    # 'c sharp': ('239120', 'c-sharp'),
    'Assembly': ('007AAC', 'assemblyscript'),
    # Frameworks n Softwares
    'Git': ('F05032', 'git'),
    'VSCode': ('007ACC', 'visual-studio-code'),
    # '.net': ('512BD4', '.net'),
    'SFML': ('8CC445', 'sfml'),
    'Cmake': ('064F8C', 'cmake'),
    'Docker': ('2496ED', 'docker'),
    # Web Development
    'HTML': ('E34F26', 'html5'),
    'CSS': ('1572B6', 'css3'),
    'Javascript': ('F7DF1E', 'javascript'),
    'React': ('61DAFB', 'react'),
    'Django': ('092E20', 'django'),
    'Android Studio': ('3DDC84', 'android-studio'),
    'Fastapi': ('009688', 'fastapi'),
    'Node.Js': ('339933', 'node.js'),
    # 'npm': ('CB3837', 'npm'),
    'Webpack': ('8DD6F9', 'webpack'),
    # Data Science
    'Numpy': ('013243', 'numpy'),
    'Plotly': ('3F4F75', 'plotly'),
    'Scipy': ('8CAAE6', 'scipy'),
    'PyTorch': ('EE4C2C', 'pytorch'),
    'Tensorflow': ('FF6F00', 'tensorflow'),
    'Jupyter': ('F37626', 'jupyter'),
    'SpaCy': ('09A3D5', 'spacy'),
    'Colab': ('F9AB00', 'google-colab'),
    # Databases
    'SQLite': ('003B57', 'sqlite'),
    'PostgreSQL': ('4169E1', 'postgresql'),
    'Heroku': ('430098', 'heroku'),
    # Scripts
    'Bash': ('4EAA25', 'gnu-bash'),
    'LaTeX': ('008080', 'latex'),
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
    code += f'''\n<img src="https://img.shields.io/badge/-{skill}-{tokyonight["title_color"]}?style=flat&logo={info[1]}&logoColor={tokyonight["text_color"]}&labelColor={tokyonight["bg_color"]}">'''

code += f'''
</div>

<br>
</code>

## Statistics

<code>
<br/>
<p align="left">
  <img width="53.8%" src="https://github-readme-stats.vercel.app/api?username=adityakadoo&show_icons=true&hide_border=true&theme=tokyonight" />
    <img width="45.2%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=adityakadoo&layout=compact&hide_border=true&theme=tokyonight" />
</p>
</code>

![Activity Graph](https://activity-graph.herokuapp.com/graph?username=adityakadoo&custom_title=adityakadoo's%20Contribution%20Graph&theme=tokyonight&bg_color={tokyonight["bg_color"]}&hide_border=true&line={tokyonight["text_color"]}&point={tokyonight["icon_color"]}&color={tokyonight["title_color"]})
'''

print(code)
