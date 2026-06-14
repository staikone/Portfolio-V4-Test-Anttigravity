import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix 1: Make headers full width by replacing col-lg-6 and col-lg-8 in header rows with col-12
# Portfolio section
html = html.replace(
    '<section id="portfolio" class="my-5 py-5 bg-text">',
    '<section id="portfolio" class="my-5 py-5 bg-text">' # Just to find it
)
# We can find all <div class="col-lg-6 aos-init" data-aos="fade-up"> that are parents of section headers
# Portfolio: <div class="col-lg-6 aos-init" data-aos="fade-up">\n                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">P</span>...
# Actually let's just do a string replacement for the specific sections
# Portfolio Header
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-lg-6 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">P</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">P</span>'''
)

# Tools Header
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-lg-6 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">D</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">D</span>'''
)

# Contact Header
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-lg-6 aos-init" data-aos="fade-up">
                  <span class="text-muted ">Personal Info</span>
                  <h2 class="display-1 txt-fx slide-up"><span class="word"><span class="letter" style="transition-delay:100ms;">C</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">
                  <h2 class="display-1 txt-fx slide-up"><span class="word"><span class="letter" style="transition-delay:100ms;">C</span><span class="letter" style="transition-delay:110ms;">o</span><span class="letter" style="transition-delay:120ms;">n</span><span class="letter" style="transition-delay:130ms;">t</span><span class="letter" style="transition-delay:140ms;">a</span><span class="letter" style="transition-delay:150ms;">c</span><span class="letter" style="transition-delay:160ms;">t</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:180ms;">M</span><span class="letter" style="transition-delay:190ms;">e</span></span></h2>
                  <span class="text-muted d-block mt-2">Get in touch</span>
                </div>'''
) # Moved the span below h2, changed text to "Get in touch"

# About Header and Text
html = html.replace(
'''<div class="col-lg-8 text-start">
                  <h2 class="display-1 txt-fx slide-up text-center">About Me</h2>
                  <span class="text-muted d-block mb-4 text-center">My introduction</span>
                  <p class="lead">''',
'''<div class="col-12 text-start">
                  <h2 class="display-1 txt-fx slide-up text-center">About Me</h2>
                  <span class="text-muted d-block mb-4 text-start">My introduction</span>
                  <p class="mb-4">'''
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html headers and About section")
