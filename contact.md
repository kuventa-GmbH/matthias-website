---
title: "Kontakt"
description: "Kontakt zu Matthias Kühnlein für Beratung, Interim-Mandate und Projektanfragen in IT Compliance, IAM/PAM und Informationssicherheit."
meta_title: "Kontakt | Matthias Kühnlein IT Security Consultant"
meta_description: "Jetzt unverbindlich anfragen: Kontaktformular, Telefon, E-Mail und LinkedIn."
permalink: /kontakt/
nav_order: 5
---

<section class="section contact-page">
  <div class="container">
    <h1 class="center sec-heading js-anim" data-anim="animate__fadeInLeft" data-once="true">Kontakt</h1>
    <p class="center js-anim" data-anim="animate__fadeIn" data-once="true">Für Projektanfragen, Beratungsmandate und Interim-Unterstützung in großen Unternehmensumfeldern.</p>

    <div class="contact-direct js-anim" data-anim="animate__fadeInUp" data-once="true">
      <article class="contact-direct__item">
        <span class="contact-direct__label">E-Mail</span>
        <span class="contact-direct__value">{{ site.email }}</span>
        <div class="contact-direct__actions">
          <a class="contact-direct__btn contact-direct__btn--primary" href="mailto:{{ site.email }}">E-Mail senden</a>
        </div>
      </article>
      <article class="contact-direct__item">
        <span class="contact-direct__label">Telefon</span>
        <span class="contact-direct__value">{{ site.phone_display }}</span>
        <div class="contact-direct__actions">
          <a class="contact-direct__btn contact-direct__btn--primary" href="tel:{{ site.phone_href }}">Anrufen</a>
        </div>
      </article>
    </div>
  </div>
</section>
