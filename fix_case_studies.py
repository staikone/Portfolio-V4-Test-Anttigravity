import glob

# Fix style.css padding for contact-card img
with open("assets/style.css", "r", encoding="utf-8") as f:
    css = f.read()

if ".contact-card img {" not in css:
    css += "\n.contact-card img {\n  padding-bottom: 20px;\n}\n"
    with open("assets/style.css", "w", encoding="utf-8") as f:
        f.write(css)

# Fix case studies
for filepath in glob.glob("case-studies/Project-*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check if <main> is missing
    if "<main class=" not in html:
        # insert <main class="col-lg-10 offset-lg-2" data-landmark-index="2"> after </header>
        # and </main> before <footer>
        html = html.replace('</header>', '</header>\n    <main class="col-lg-10 offset-lg-2">\n      <div class="container">\n        <div class="justify-content-center px-1 mx-1 px-xl-5 mx-xl-5">')
        html = html.replace('<footer', '        </div>\n      </div>\n    </main>\n    <footer')

    # Fix nav links
    html = html.replace('href="#home"', 'href="../index.html#home"')
    html = html.replace('href="#portfolio"', 'href="../index.html#portfolio"')
    html = html.replace('href="#about"', 'href="../index.html#about"')
    html = html.replace('href="#contact"', 'href="../index.html#contact"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Fixed case studies and style.css")
