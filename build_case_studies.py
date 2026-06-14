import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace assets/ with ../assets/
html = html.replace('src="assets/', 'src="../assets/')
html = html.replace("href='assets/", "href='../assets/")
html = html.replace('href="assets/', 'href="../assets/')

# Also update the CSS paths if they are in there
html = html.replace('url("assets/', 'url("../assets/')
html = html.replace("url('assets/", "url('../assets/")

# Now remove main sections.
# Sections: <section id="home">, <section id="portfolio">, <section id="about">, <section id="Tools">, <section id="contact">
# Let's just find the start of the <main> or the first <section> and remove up to the footer.
# The layout has <header id="header-nav" ...> ... </header>
# Then sections.
header_end = html.find('</header>') + len('</header>')
footer_start = html.find('<footer')
if footer_start == -1:
    footer_start = html.find('<section id="footer">') # fallback
if footer_start == -1:
    # Look for the last section end
    footer_start = html.rfind('</section>') + len('</section>')

top = html[:header_end]
bottom = html[footer_start:]

def create_case_study(filename, title, subtitle, texts):
    content = f'''
    <section class="my-5 py-5 bg-text">
      <div class="container mt-5 pt-5 aos-init" data-aos="fade-up">
        <div class="row justify-content-center">
          <div class="col-lg-10">
            <h1 class="display-4 font-weight-bold mb-3">{title}</h1>
            <p class="lead text-muted mb-5">{subtitle}</p>
            <div class="case-study-content">
              {texts}
            </div>
            <div class="text-center mt-5 pt-5">
              <a href="../index.html#portfolio" class="btn btn-dark text-uppercase py-3 px-5">Back to Projects</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    with open(f"case-studies/{filename}", "w", encoding="utf-8") as f:
        f.write(top + content + bottom)

# Case Study 1
p1_text = """
<h2 class="mb-3">Overview</h2>
<p class="mb-4">Due to NDA constraints, visuals are recreated as a fictional B2B catalog preserving the original UX logic. In a B2B automotive parts catalog, promotional campaigns by quantity were hidden or confusing. The goal was to redesign how promotions are displayed on product listing pages (PLP) and product detail pages (PDP), so that users can quickly discover applicable offers and make informed purchasing decisions. I led UX + UI design, aligning with design systems and accessibility standards.</p>

<h2 class="mb-3">Problem</h2>
<p class="mb-4">Users often missed active promotions or didn’t understand tiered discounts. The original interface lacked clear visual cues, making it hard to compare discounted prices or know when a promotion applies. This ambiguity reduced conversion and hurt discoverability of offers.</p>

<h2 class="mb-3">Process</h2>
<p class="mb-4">I followed a user-centered design workflow to create the promotion visibility feature:</p>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2"><strong>Research & Audit:</strong> Reviewed existing catalog UX, analyzed user pain points via support tickets, and benchmarked similar e-commerce systems.</li>
  <li class="mb-2"><strong>Wireframes & Ideation:</strong> Sketched multiple layouts showing promotion badges next to prices and "Add to Cart" buttons, both for list and detail pages.</li>
  <li class="mb-2"><strong>Design Iterations:</strong> Created high-fidelity mockups in desktop, tablet, and mobile views. Conducted stakeholder reviews to validate clarity.</li>
  <li class="mb-2"><strong>Usability Refinement:</strong> Tested hover tooltips and modals for campaigns with many tiers; adjusted interactions to ensure clarity and responsiveness.</li>
  <li class="mb-2"><strong>Localization Flexibility:</strong> Built optional custom fields for legal/regional campaign notes to adapt across markets.</li>
</ul>

<h2 class="mb-3">Solution</h2>
<p class="mb-4">The final design adds a campaign icon next to product price & “Add to cart.” On desktop, hovering reveals details via a tooltip; for many promotions, a “Show all” modal appears. On mobile, tapping the icon opens a full-screen modal with campaign tiers and pricing. Visual badge, modal design, and interactions were designed to balance richness with speed.</p>

<h2 class="mb-3">Results</h2>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2">Reported improvement in conversion in markets where the feature was deployed within 3 months.</li>
  <li class="mb-2">Internal operators reported processing orders more quickly and accurately thanks to clearer promotional visibility.</li>
  <li class="mb-2">Positive user feedback: users reported better clarity in understanding discounts.</li>
</ul>

<h2 class="mb-3">Learnings</h2>
<p class="mb-4">I'd integrate A/B testing earlier and capture quantitative metrics — click-through, engagement — during pilot rollout rather than relying on qualitative feedback alone. Documenting these metrics as part of design deliverables would strengthen both credibility and future iterations.</p>
"""
create_case_study("Project-1.html", "Enhancing Promotion Visibility in B2B Catalog", "Improving how discounts and quantity-based promotions are shown in product listings and product pages", p1_text)

# Case Study 2
p2_text = """
<h2 class="mb-3">Overview</h2>
<p class="mb-4">In a large B2B e-commerce platform for automotive parts, the tools category lacked an intuitive quick search page. My goal was to design and implement this page to improve discoverability, streamline navigation among categories, and ultimately boost tool-related sales. I held full UX/UI responsibility, created custom icons, implemented responsiveness, and ensured accessibility.</p>

<h2 class="mb-3">Problem</h2>
<p class="mb-4">The existing interface made it difficult for users to find tools by category. Navigation was unclear, icons were missing or generic, and mobile usability suffered. Many potential customers dropped off or failed to locate the parts they needed, hurting conversion and sales in the tools section.</p>

<h2 class="mb-3">Process</h2>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2"><strong>Audit & Research:</strong> Reviewed existing catalog page analytics and user behavior in tools section.</li>
  <li class="mb-2"><strong>Category Mapping & Icon Design:</strong> Created 12 tool categories and designed custom icons/pictograms for better visual differentiation.</li>
  <li class="mb-2"><strong>Wireframing & Prototyping:</strong> Developed layout sketches and interactive navigation flows for both desktop and mobile.</li>
  <li class="mb-2"><strong>Responsiveness & Breakpoints:</strong> Ensured 2 items per row on tablet, 1 per row on mobile; navigation collapses into hamburger menu.</li>
  <li class="mb-2"><strong>Iteration & Feedback:</strong> Conducted internal reviews, usability feedback from operators, and refined icon sizes, hover states, touch targets.</li>
</ul>

<h2 class="mb-3">Solution</h2>
<p class="mb-4">The final design features a sticky navigation bar for tool categories, custom icons for visual clarity, and responsive grids tuned for desktop, tablet, and mobile. Hover and click states improve discoverability. For markets with multiple languages, labels and tooltips adjust dynamically. The interface is also built with accessibility compliance in mind.</p>

<h2 class="mb-3">Results</h2>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2">Reported improvement in tool category conversion in pilot markets within 3 months of launch.</li>
  <li class="mb-2">Positive feedback from both operators and end-users on navigation clarity</li>
  <li class="mb-2">The Quick Search page was selected as a template for other catalog sections</li>
  <li class="mb-2">Performance and usability were improved without sacrificing load speed</li>
</ul>

<h2 class="mb-3">Learnings</h2>
<p class="mb-4">Collaborating with product managers specialized in garage equipment gave me domain knowledge I couldn't have gained independently — it directly shaped category structure and icon decisions. Working across multiple markets also taught me to design for requirements I hadn't anticipated upfront; country-specific needs are best gathered before wireframing, not during iteration.</p>
"""
create_case_study("Project-2.html", "Quick Search Page for Vehicle Repair Tools", "Redesigning navigation and category clarity for B2B automotive tools catalog", p2_text)

# Case Study 3
p3_text = """
<h2 class="mb-3">Overview</h2>
<p class="mb-4">In a B2B web platform for automotive aftermarket and OEM parts across multiple segments (light & heavy vehicles, marine, agricultural), the “Quick Search” landing page listing product categories was underperforming. The original layout wasted space and limited click targets. My role was to redesign the UI component from scratch, integrate it into the design system, and ensure accessibility across markets.</p>

<h2 class="mb-3">Problem</h2>
<p class="mb-4">The existing quick search categories interface forced users to hunt for clickable zones—only parts of each category tile were clickable, and visual feedback was minimal. On narrower screens, the layout broke or became clumsy. This ambiguity reduced usability and slowed navigation in a complex catalog.</p>

<h2 class="mb-3">Process</h2>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2"><strong>Audit & Usability Review:</strong> Evaluated current quick search layout, measured click zones, collected pain points from support logs and user feedback.</li>
  <li class="mb-2"><strong>Concept & Wireframes:</strong> Created multiple layout options showing full-tile click behavior, hover feedback, and adaptive grid systems.</li>
  <li class="mb-2"><strong>Mockups & Specification:</strong> Designed clean visuals with retouched images, border cues, and hover expansion. Documented spacing, states, and interactions.</li>
  <li class="mb-2"><strong>Responsive Adjustments:</strong> Defined behavior across desktop (up to 5 columns), tablet (2 columns), and mobile (single column) with touch-friendly zones.</li>
  <li class="mb-2"><strong>Localization & Edge Cases:</strong> Tested dynamic text lengths, category variations across 22 markets, and adaptive behavior in different languages and contexts.</li>
  <li class="mb-2"><strong>Iteration & Feedback:</strong> Gathered stakeholder and user feedback, refined hover feedback, border expansion, and touch interactions.</li>
</ul>

<h2 class="mb-3">Solution</h2>
<p class="mb-4">The redesigned quick search component displays category tiles that are fully clickable (not just the label). Each tile includes a crisp product image and clear title, enclosed by a border that expands by 3px on hover (desktop) to give visual feedback. On mobile/tablet, taps open a modal with full category information. The interface is integrated into the existing design system and styled to accommodate localization and accessibility.</p>

<h2 class="mb-3">Results</h2>
<ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
  <li class="mb-2">✅ Positive qualitative feedback from users across 22 markets.</li>
  <li class="mb-2">✅ Faster navigation to key categories by reducing cognitive friction.</li>
  <li class="mb-2">✅ Improved visual hierarchy and clarity in the catalog UI.</li>
  <li class="mb-2">✅ The redesign was adopted as a pattern for similar category pages.</li>
</ul>

<h2 class="mb-3">Learnings</h2>
<p class="mb-4">The biggest constraint came from the content team, who could only work with HTML and CSS. This required close collaboration to ensure the design was implementable within their limitations — and taught me to validate technical feasibility earlier with all stakeholders, not just the main dev team. It also meant helping them navigate the design system we were building in parallel, which reinforced the value of clear documentation alongside design deliverables.</p>
"""
create_case_study("Project-3.html", "Quick Search Categories Redesign", "Improving usability, layout, and visual feedback for a B2B parts catalog", p3_text)

print("Created case studies successfully.")
