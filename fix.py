import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Contact broken span removal
broken_contact = '''<span class="text-muted d-block mt-2">Get in touch</span>
                </div><span class="letter" style="transition-delay:110ms;">o</span><span class="letter" style="transition-delay:120ms;">n</span><span class="letter" style="transition-delay:130ms;">t</span><span class="letter" style="transition-delay:140ms;">a</span><span class="letter" style="transition-delay:150ms;">c</span><span class="letter" style="transition-delay:160ms;">t</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:180ms;">M</span><span class="letter" style="transition-delay:190ms;">e</span></span></h2>'''

fixed_contact = '''<span class="text-muted d-block mt-2 text-center">Get in touch</span>
                </div>'''
html = html.replace(broken_contact, fixed_contact)

# Contact needs text-center on col-12
html = html.replace(
'''<section id="contact" class="my-5 py-5 bg-text">
            <div class="container">
              <div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">''',
'''<section id="contact" class="my-5 py-5 bg-text">
            <div class="container">
              <div class="row justify-content-center mb-5">
                <div class="col-12 text-center aos-init" data-aos="fade-up">'''
)

# 2. Line-through in Home section
html = html.replace('Currently based in Bangkok, Kuala Lumpur, Sofia Bulgaria.', 'Currently based in <span style="text-decoration: line-through;">Bangkok, Kuala Lumpur</span>, Sofia Bulgaria.')

# 3. Projects section centering
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">P</span><span class="letter" style="transition-delay:190ms;">r</span><span class="letter" style="transition-delay:200ms;">o</span><span class="letter" style="transition-delay:210ms;">j</span><span class="letter" style="transition-delay:220ms;">e</span><span class="letter" style="transition-delay:230ms;">c</span><span class="word"><span class="letter" style="transition-delay:250ms;">t</span><span class="letter" style="transition-delay:260ms;">s</span></span></h2><span class="text-muted">Most recent work</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 text-center aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">P</span><span class="letter" style="transition-delay:190ms;">r</span><span class="letter" style="transition-delay:200ms;">o</span><span class="letter" style="transition-delay:210ms;">j</span><span class="letter" style="transition-delay:220ms;">e</span><span class="letter" style="transition-delay:230ms;">c</span><span class="word"><span class="letter" style="transition-delay:250ms;">t</span><span class="letter" style="transition-delay:260ms;">s</span></span></h2><span class="text-muted text-center d-block">Most recent work</span>'''
)

# 4. About section centering
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-12 text-start">
                  <h2 class="display-1 txt-fx slide-up text-center">About Me</h2>
                  <span class="text-muted d-block mb-4 text-start">My introduction</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 text-center">
                  <h2 class="display-1 txt-fx slide-up text-center">About Me</h2>
                  <span class="text-muted d-block mb-4 text-center">My introduction</span>'''
)

# 5. Tools section centering
html = html.replace(
'''<div class="row justify-content-center mb-5">
                <div class="col-12 aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">D</span><span class="letter" style="transition-delay:190ms;">e</span><span class="letter" style="transition-delay:200ms;">s</span><span class="letter" style="transition-delay:210ms;">i</span><span class="letter" style="transition-delay:220ms;">g</span><span class="letter" style="transition-delay:230ms;">n</span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:250ms;">t</span><span class="letter" style="transition-delay:260ms;">o</span><span class="letter" style="transition-delay:270ms;">o</span><span class="letter" style="transition-delay:280ms;">l</span><span class="letter" style="transition-delay:290ms;">s</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:310ms;">I</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:330ms;">u</span><span class="letter" style="transition-delay:340ms;">s</span><span class="letter" style="transition-delay:350ms;">e</span></span></h2><span class="text-muted">My primary design tools.</span>''',
'''<div class="row justify-content-center mb-5">
                <div class="col-12 text-center aos-init" data-aos="fade-up">
                  
                  <h2 class="display-1 txt-fx slide-up"><span class="letter" style="transition-delay:180ms;">D</span><span class="letter" style="transition-delay:190ms;">e</span><span class="letter" style="transition-delay:200ms;">s</span><span class="letter" style="transition-delay:210ms;">i</span><span class="letter" style="transition-delay:220ms;">g</span><span class="letter" style="transition-delay:230ms;">n</span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:250ms;">t</span><span class="letter" style="transition-delay:260ms;">o</span><span class="letter" style="transition-delay:270ms;">o</span><span class="letter" style="transition-delay:280ms;">l</span><span class="letter" style="transition-delay:290ms;">s</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:310ms;">I</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:330ms;">u</span><span class="letter" style="transition-delay:340ms;">s</span><span class="letter" style="transition-delay:350ms;">e</span></span></h2><span class="text-muted text-center d-block">My primary design tools.</span>'''
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("assets/style.css", "a", encoding="utf-8") as f:
    f.write("\n.banner-image img {\n  max-width: 80% !important;\n}\n")

print("Done")
