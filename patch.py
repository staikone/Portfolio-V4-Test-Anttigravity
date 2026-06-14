import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix Contact section leftover span
# I need to find the exact broken string and replace it.
broken_string = '''<span class="text-muted d-block mt-2">Get in touch</span>
                </div><span class="letter" style="transition-delay:110ms;">o</span><span class="letter" style="transition-delay:120ms;">n</span><span class="letter" style="transition-delay:130ms;">t</span><span class="letter" style="transition-delay:140ms;">a</span><span class="letter" style="transition-delay:150ms;">c</span><span class="letter" style="transition-delay:160ms;">t</span></span><span class="letter" style="transition-delay:100ms;">&nbsp;</span><span class="word"><span class="letter" style="transition-delay:180ms;">M</span><span class="letter" style="transition-delay:190ms;">e</span></span></h2>'''

fixed_string = '''<span class="text-muted d-block mt-2 text-center">Get in touch</span>
                </div>'''

if broken_string in html:
    html = html.replace(broken_string, fixed_string)
else:
    print("Could not find broken string in Contact section")

# Add text-center to col wrappers of the headers
html = html.replace('<div class="col-12 aos-init" data-aos="fade-up">', '<div class="col-12 text-center aos-init" data-aos="fade-up">')

# But wait, there might be other col-12 elements. Let's do it specifically for the ones with headers.
# I will reload HTML from scratch to be safe with standard replace.
