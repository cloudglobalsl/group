
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** Página CloudGlobal
- **Date:** 2026-05-28
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001 Open the landing page and see the main site sections
- **Test Code:** [TC001_Open_the_landing_page_and_see_the_main_site_sections.py](./TC001_Open_the_landing_page_and_see_the_main_site_sections.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/38c58735-d50e-4825-a89a-7eb567f7e3d1
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002 Jump from the header to the Home section
- **Test Code:** [TC002_Jump_from_the_header_to_the_Home_section.py](./TC002_Jump_from_the_header_to_the_Home_section.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/dc234c4b-1600-4958-aef5-0095c3a224a4
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003 Jump from the header to the Subscriptions section
- **Test Code:** [TC003_Jump_from_the_header_to_the_Subscriptions_section.py](./TC003_Jump_from_the_header_to_the_Subscriptions_section.py)
- **Test Error:** TEST FAILURE

The Subscriptions navigation link or section is not present on the site header or page, so the user cannot reach a Subscriptions section via header navigation.

Observations:
- The header contains links: Inicio, Soluciones, Servicios, Industrias, Nosotros, Partners, Acceso Clientes, Contacto
- No link or page section labeled 'Subscriptions' or 'Suscripciones' was found on the current page
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/da5c2066-98b6-4847-a59f-0e5816c68d76
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC004 Jump from the header to the Hosting section
- **Test Code:** [TC004_Jump_from_the_header_to_the_Hosting_section.py](./TC004_Jump_from_the_header_to_the_Hosting_section.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/2be0c4a5-2123-489c-a582-94a4a4e4e6af
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005 Jump from the header to the Products section
- **Test Code:** [TC005_Jump_from_the_header_to_the_Products_section.py](./TC005_Jump_from_the_header_to_the_Products_section.py)
- **Test Error:** TEST BLOCKED

The Products section could not be reached — no header navigation link labelled 'Products' or 'Productos' was found on the homepage.

Observations:
- The header navigation contains: Inicio, Soluciones, Servicios, Industrias, Nosotros, Partners, Acceso Clientes, Contacto.
- No 'Products' or 'Productos' link is present in the header navigation.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/18842e52-9869-4b61-b6c7-5690af023274
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC006 Change the site language to English
- **Test Code:** [TC006_Change_the_site_language_to_English.py](./TC006_Change_the_site_language_to_English.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/28e59620-e1a5-4eb7-b344-b201512d420c
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC007 Switch to dark mode and see the page update
- **Test Code:** [TC007_Switch_to_dark_mode_and_see_the_page_update.py](./TC007_Switch_to_dark_mode_and_see_the_page_update.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/5493a877-bd2e-488e-8c41-8149a32f0db9
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC008 Change the site language to French
- **Test Code:** [TC008_Change_the_site_language_to_French.py](./TC008_Change_the_site_language_to_French.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/dae9de39-707a-4ed0-ab04-b5d95d32ae9d
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009 Return to light mode after toggling theme
- **Test Code:** [TC009_Return_to_light_mode_after_toggling_theme.py](./TC009_Return_to_light_mode_after_toggling_theme.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/6bb8284a-f958-460f-9169-66e4d682fd07
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010 Move between multiple sections in one visit
- **Test Code:** [TC010_Move_between_multiple_sections_in_one_visit.py](./TC010_Move_between_multiple_sections_in_one_visit.py)
- **Test Error:** TEST BLOCKED

The Products section or a "Productos" header link is not present on the site, so the test cannot reach or verify the Products functionality.

Observations:
- The header navigation is visible and contains the links: Inicio, Soluciones, Servicios, Industrias, Nosotros, Partners, Acceso Clientes, Contacto, but no "Productos" link was found.
- The Servicios section content is displayed (navigation clicks to Inicio, Soluciones, Servicios succeeded), confirming navigation works for existing sections.

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/8fef7c39-2d32-4617-a4d6-3b1be2a869a9
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC011 Use navigation, language, and theme controls together
- **Test Code:** [TC011_Use_navigation_language_and_theme_controls_together.py](./TC011_Use_navigation_language_and_theme_controls_together.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/2635f67e-aac8-4dde-b0a0-2ddbc113b522
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC012 Switch languages multiple times in one session
- **Test Code:** [TC012_Switch_languages_multiple_times_in_one_session.py](./TC012_Switch_languages_multiple_times_in_one_session.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/356eaa29-58aa-460c-847d-8dbadb6ac299
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC013 Keep theme changes consistent while browsing sections
- **Test Code:** [TC013_Keep_theme_changes_consistent_while_browsing_sections.py](./TC013_Keep_theme_changes_consistent_while_browsing_sections.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/348c64fd-5fd8-4cb7-bd57-eb5eaa117e57
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC014 Browse sections after changing the language
- **Test Code:** [TC014_Browse_sections_after_changing_the_language.py](./TC014_Browse_sections_after_changing_the_language.py)
- **Test Error:** TEST BLOCKED

The test could not be run — the expected header navigation links for 'Subscriptions' and 'Hosting' are not present on the site, so navigation and label-consistency verification cannot be performed.

Observations:
- The page is displayed in French after selecting the FR button: header labels include 'Accueil', 'Solutions', 'Services', 'Industries', 'À propos', 'Partenaires', 'Espace Clients', 'Contact'.
- No header links labeled 'Subscriptions' / 'Abonnements' or 'Hosting' / 'Hébergement' were found in the visible header interactive elements.

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/3a4838c3-b95f-4b5f-9698-da3b131aeb3a/2e89ed8d-7cb4-4357-841a-c8a77372ec4a
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **71.43** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---