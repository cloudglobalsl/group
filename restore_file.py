
import os
import re

path = r'c:\Users\Suri\Desktop\Página CloudGlobal\globalcloudgroup.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore Dropdown
old_drop = '''        <li class="nav-item" id="dropCloud">
          <span class="nav-link" onclick="toggleDrop('dropCloud')">Cloud Soberana
            <svg class="nav-chevron" viewBox="0 0 12 12">
              <polyline points="2,4 6,8 10,4" />
            </svg>
          </span>
          <div class="nav-dropdown">
            <a href="#" onclick="navigate('home');return false">Cloud</a>
            <a href="#" onclick="navigate('home');return false">Nube Privada Empresarial</a>
          </div>
        </li>'''

new_drop_pattern = re.compile(r'<li class="nav-item" id="dropCloud">.*?</li>', re.DOTALL)
content = new_drop_pattern.sub(old_drop, content)

# 2. Fix CSS
css_pattern = re.compile(r'/\* RICH DROPDOWN \*/.*?</style>', re.DOTALL)
content = css_pattern.sub('</style>', content)

# 3. Restore Footer and Script
footer_marker = '<div class="footer-ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
break_marker = 'data-cfemail="82efe3ebeec2e1eeedf7e6e5eee'
footer_break_idx = content.find(break_marker)

if footer_break_idx != -1:
    # Find the beginning of that footer info block
    block_start = content.rfind(footer_marker, 0, footer_break_idx)
    if block_start != -1:
        tail = '''<div class="footer-ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                <polyline points="22,6 12,13 2,6" />
              </svg><span><a href="/cdn-cgi/l/email-protection" class="__cf_email__"
                  data-cfemail="82efe3ebeec2e1eeedf7e6e5eeede0e3eeace7f1">[email&#160;protected]</a></span></div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Global Cloud Group. Todos los derechos reservados.</span>
        <span>Málaga, España</span>
      </div>
    </footer>
  </div>
  <button id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})" title="Volver arriba"><svg width="16"
      height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
      <polyline points="18 15 12 9 6 15" />
    </svg></button>
  <script>
    function navigate(page) {
      document.querySelectorAll('.page').forEach(function (p) { p.classList.remove('active'); });
      var target = document.getElementById('page-' + page);
      if (target) { target.classList.add('active'); window.scrollTo(0, 0); }
      document.querySelectorAll('.nav-item').forEach(function (i) { i.classList.remove('open'); });
      var menu = document.getElementById('navMenu');
      if (menu) menu.classList.remove('open');
      setActiveNav(page);
    }

    function toggleDrop(id) {
      var el = document.getElementById(id);
      var was = el.classList.contains('open');
      document.querySelectorAll('.nav-item').forEach(function (i) { i.classList.remove('open'); });
      if (!was) el.classList.add('open');
    }

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-item')) {
        document.querySelectorAll('.nav-item').forEach(function (i) { i.classList.remove('open'); });
      }
    });

    function toggleMobile() {
      document.getElementById('navMenu').classList.toggle('open');
    }

    function toggleTheme() {
      var root = document.documentElement;
      var dark = root.getAttribute('data-theme') === 'dark';
      root.setAttribute('data-theme', dark ? 'light' : 'dark');
      document.getElementById('themeLabel').textContent = dark ? 'Modo oscuro' : 'Modo claro';
      var icon = document.getElementById('themeIcon');
      icon.innerHTML = dark
        ? '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>'
        : '<path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/>';
    }

    var NAV_MAP = {
      home: "Inicio", suscripciones: "Suscripciones", hosting: "Hosting Web",
      planes: "Hosting Web", "alquiler-tec": "Alquiler Tecnológico",
      alquiler: "Suscripciones", correo: "Suscripciones", daas: "Suscripciones",
      "bare-metal": "Servicios Bare Metal", productos: "Productos",
      partners: "Partners", digital: "Digital Transformation", contacto: "Contactar"
    };

    function setActiveNav(page) {
      document.querySelectorAll(".nav-link").forEach(function (l) { l.classList.remove("current"); });
      var label = NAV_MAP[page];
      if (!label) return;
      document.querySelectorAll(".nav-link").forEach(function (l) {
        var txt = l.textContent.replace(/\\s+/g, " ").trim();
        if (txt === label) l.classList.add("current");
      });
    }

    window.addEventListener("scroll", function () {
      var b = document.getElementById("backToTop");
      if (b) b.classList.toggle("visible", window.scrollY > 280);
    });

    var T = {
      es: {
        nav: ["Inicio", "Suscripciones", "Hosting Web", "Alquiler Tecnológico", "Servicios Bare Metal", "Productos", "Partners", "Digital Transformation", "Cloud Soberana"],
        contact: "Contactar", sl1: "Clientes Activos", sl2: "Uptime Garantizado", sl3: "Soporte Técnico", sl4: "Años de Experiencia",
        htitle: "Soluciones IT para<br/>empresas <em>que avanzan</em>",
        hsub: "Infraestructura cloud soberana, ciberseguridad avanzada y servicios gestionados para organizaciones que exigen fiabilidad y rendimiento real.",
        hb1: "Explorar servicios", hb2: "Hablar con un experto"
      },
      en: {
        nav: ["Home", "Subscriptions", "Web Hosting", "Tech Rental", "Bare Metal Servers", "Products", "Partners", "Digital Transformation", "Sovereign Cloud"],
        contact: "Contact", sl1: "Active Clients", sl2: "Guaranteed Uptime", sl3: "Tech Support", sl4: "Years of Experience",
        htitle: "IT Solutions for<br/>businesses <em>that grow</em>",
        hsub: "Sovereign cloud infrastructure, advanced cybersecurity and managed services for organizations that demand reliability and real performance.",
        hb1: "Explore services", hb2: "Talk to an expert"
      },
      fr: {
        nav: ["Accueil", "Abonnements", "Hébergement Web", "Location Tech", "Serveurs Bare Metal", "Produits", "Partenaires", "Transformation Digitale", "Cloud Souverain"],
        contact: "Contact", sl1: "Clients Actifs", sl2: "Disponibilidad Garantie", sl3: "Support Technique", sl4: "Ans d'Expérience",
        htitle: "Solutions IT pour<br/>les empresas <em>qui avancent</em>",
        hsub: "Infrastructure cloud souveraine, cybersécurité avancée et services gérés para las organizaciones que exigen fiabilidad y rendement réelle.",
        hb1: "Explorer les services", hb2: "Parler à un expert"
      }
    };
    function setLang(lang) {
      var t = T[lang];
      document.querySelectorAll(".lang-btn").forEach(function (b) {
        b.classList.toggle("active", b.textContent.trim().toLowerCase() === lang);
      });
      var links = document.querySelectorAll(".nav-menu .nav-link");
      var ni = 0;
      links.forEach(function (l) {
        var node = l.childNodes[0];
        if (node && node.nodeType === 3 && node.textContent.trim().length > 1) {
          if (t.nav[ni] !== undefined) { node.textContent = t.nav[ni] + " "; ni++; }
        }
      });
      var cb = document.getElementById("btn-contact");
      if (cb) cb.textContent = t.contact;
      var sl1 = document.getElementById("sl1"), sl2 = document.getElementById("sl2"),
        sl3 = document.getElementById("sl3"), sl4 = document.getElementById("sl4");
      if (sl1) sl1.textContent = t.sl1; if (sl2) sl2.textContent = t.sl2;
      if (sl3) sl3.textContent = t.sl3; if (sl4) sl4.textContent = t.sl4;
      var ht = document.querySelector("#page-home .display-title");
      if (ht) ht.innerHTML = t.htitle;
      var hs = document.querySelector("#page-home .lead");
      if (hs) hs.textContent = t.hsub;
      var btns = document.querySelectorAll("#page-home .hero-btns span");
      if (btns[0]) btns[0].textContent = t.hb1;
      if (btns[1]) btns[1].textContent = t.hb2;
    }
    setActiveNav("home");
  </script>
</body>
</html>'''
        content = content[:block_start] + tail

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Restoration successful")
