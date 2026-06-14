import re
import glob

# 1. Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove data-text
html = re.sub(r'\sdata-text="\d+"', '', html)

# Remove Labore accusam
html = re.sub(r'<p>Labore accusam in modo compungi, iacentem substantiales um se sed esse haec\.</p>', '', html)

# Menu: Add LinkedIn under CV
# Find CV link:
# <li><a href="https://drive.google.com/file/d/1XrD2A0Etg42ohongGsYNEXFhg9dVApa6/view?usp=drive_link" target="_blank" class="nav-link">CV</a></li>
cv_link = '<li><a href="https://drive.google.com/file/d/1XrD2A0Etg42ohongGsYNEXFhg9dVApa6/view?usp=drive_link" target="_blank" class="nav-link">CV</a></li>'
linkedin_link = '<li><a href="https://www.linkedin.com/in/stayko-nenov/" target="_blank" class="nav-link">LinkedIn</a></li>'
if linkedin_link not in html:
    html = html.replace(cv_link, cv_link + '\n              ' + linkedin_link)

# Hero section restructuring
# We need to extract the Hero section and rebuild it.
hero_start = html.find('<section id="home"')
hero_end = html.find('</section>', hero_start) + len('</section>')
hero_html = html[hero_start:hero_end]

# Instead of complex parsing, let's just rebuild the inner HTML of the home section
new_hero = '''<section id="home" class="py-5 bg-text">
            <div class="row">
              <div class="col-lg-6 order-2 order-lg-1">         
                <div class="banner-content my-1 pt-1 my-lg-5 pt-lg-5 aos-init" data-aos="fade-up">
                  <h1 class="display-1 txt-fx slide-up"><span class="word"><span class="letter" style="transition-delay:100ms;">H</span><span class="letter" style="transition-delay:110ms;">i</span><span class="letter" style="transition-delay:120ms;">,</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:140ms;">I</span><span class="letter" style="transition-delay:150ms;">'</span><span class="letter" style="transition-delay:160ms;">m</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:180ms;">S</span><span class="letter" style="transition-delay:190ms;">t</span><span class="letter" style="transition-delay:200ms;">a</span><span class="letter" style="transition-delay:210ms;">y</span><span class="letter" style="transition-delay:220ms;">k</span><span class="letter" style="transition-delay:230ms;">o</span></span></h1>
                  <span class="text-muted d-block mb-3">Visual, UX/UI Designer</span>
                  <p class="text-start mb-4">With 3 years of experience crafting user-friendly and engaging digital products. I focus on web and mobile design, combining clean visuals with thoughtful user experiences. Currently based in Bangkok, Kuala Lumpur, Sofia Bulgaria.</p>
                  <a href="https://drive.google.com/file/d/1XrD2A0Etg42ohongGsYNEXFhg9dVApa6/view?usp=drive_link" target="_blank" class="btn btn-dark py-3 px-5 mt-2 aos-init" data-aos="fade-up" data-aos-delay="300">Download My CV</a>
                </div>
              </div>
              <div class="col-lg-6 order-1 order-lg-2">
                <div class="banner-image text-center aos-init" data-aos="fade-left">
                  <img src="assets/banner-image.png" alt="banner" class="img-fluid">
                </div>
              </div>
            </div>
          </section>'''

html = html[:hero_start] + new_hero + html[hero_end:]

# Portfolio Links
html = html.replace('href="https://staikone.github.io/Portfolio-V3-Anttigravity/case-studies/Project-1.html"', 'href="case-studies/Project-1.html"')
html = html.replace('href="https://staikone.github.io/Portfolio-V3-Anttigravity/case-studies/Project-2.html"', 'href="case-studies/Project-2.html"')
html = html.replace('href="https://staikone.github.io/Portfolio-V3-Anttigravity/case-studies/Project-3.html"', 'href="case-studies/Project-3.html"')

# About Section
about_start = html.find('<section id="about"')
about_end = html.find('</section>', about_start) + len('</section>')
new_about = '''<section id="about" class="my-5 py-5 bg-text">
            <div class="container text-center aos-init" data-aos="fade-up">
              <div class="row justify-content-center mb-5">
                <div class="col-lg-8 text-start">
                  <h2 class="display-1 txt-fx slide-up text-center">About Me</h2>
                  <span class="text-muted d-block mb-4 text-center">My introduction</span>
                  <p class="lead">I enjoy designing clean and user-friendly interfaces, with attention to both visuals and usability. Most of my experience comes from working on web and mobile projects in B2B e-commerce, where I aim to keep things as simple and intuitive as possible. I’m still growing as a designer and enjoy learning from every project I take on. Currently open to new opportunities and collaborations.</p>
                </div>
              </div>
              
              <div class="row justify-content-center mb-5">
                <div class="col-md-4 mb-4">
                  <div class="about-stat">
                    <h3 class="display-4 font-weight-bold">03</h3>
                    <p class="text-muted m-0">years UX/UI Focus</p>
                  </div>
                </div>
                <div class="col-md-4 mb-4">
                  <div class="about-stat">
                    <h3 class="display-4 font-weight-bold">20+</h3>
                    <p class="text-muted m-0">International Markets</p>
                  </div>
                </div>
                <div class="col-md-4 mb-4">
                  <div class="about-stat">
                    <h3 class="display-4 font-weight-bold">01</h3>
                    <p class="text-muted m-0">Large B2B Platform</p>
                  </div>
                </div>
              </div>

              <div class="row justify-content-center mt-5">
                <div class="col-auto">
                  <a href="https://drive.google.com/file/d/1XrD2A0Etg42ohongGsYNEXFhg9dVApa6/view?usp=drive_link" target="_blank" class="btn btn-dark py-3 px-5">Download My CV</a>
                </div>
              </div>
            </div>
          </section>'''

html = html[:about_start] + new_about + html[about_end:]

# Remove text-center from cards if there is any, and ensure captions are left aligned
# Actually cards are inside .portfolio-card or .contact-card
# We can just rely on standard bootstrap left alignment or explicit text-start
html = html.replace('text-uppercase', '')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully")
