with open("assets/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("text-align: center;", "text-align: left;")
# Wait, replacing all text-align: center is dangerous. Let's just do it cleanly.
css = css.replace(".contact-card {\n  padding: 50px 30px;\n  align-items: center;\n  text-align: center;\n  justify-content: center;\n}", ".contact-card {\n  padding: 50px 30px;\n  align-items: center;\n  text-align: left;\n  justify-content: center;\n}")

css += "\n.contact-card h3 {\n  text-align: center;\n}\n"
css += "\n.custom-card h3, .custom-card .title {\n  text-align: center;\n}\n"

with open("assets/style.css", "w", encoding="utf-8") as f:
    f.write(css)
