import glob

linkedin_link = '<li><a href="https://www.linkedin.com/in/stayko-nenov/" target="_blank" class="nav-link">LinkedIn</a></li>'

for filepath in glob.glob("case-studies/Project-*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 1. Menu: Add LinkedIn
    # The case studies have CV link but with href="../assets/..."? No, it has href="https://drive..."
    cv_link = '<li><a href="https://drive.google.com/file/d/1XrD2A0Etg42ohongGsYNEXFhg9dVApa6/view?usp=drive_link" target="_blank" class="nav-link">CV</a></li>'
    if linkedin_link not in html:
        html = html.replace(cv_link, cv_link + '\n              ' + linkedin_link)
        
    # 2. Top Alignment: remove mt-5 pt-5
    html = html.replace('<div class="container mt-5 pt-5 aos-init" data-aos="fade-up">', '<div class="container aos-init" data-aos="fade-up">')
    html = html.replace('<section class="my-5 py-5 bg-text">', '<section class="my-5 bg-text">') # remove py-5 to push it up
    
    # 3. Remove text-uppercase
    html = html.replace('text-uppercase', '')
    
    # 4. Text align left
    # Actually, the texts inside case study are default left-aligned since we didn't add text-center.
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Case studies updated successfully")
