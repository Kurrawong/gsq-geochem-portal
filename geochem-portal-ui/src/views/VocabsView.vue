<template>
  <main>
    <h1 class="text-4xl pb-4">Vocabularies</h1>
    <h2>GSQ Profile Vocabularies</h2>
    <p>The GSQ <RouterLink to="/profiles">Profile</RouterLink> requires that particular code values for many properties come from a controlled set of vocabularies. The vocabularies are for suvey types, drill diameters, sample material, units of measure and so on.</p>
    <p>These vocabularies are published by GSQ and are able to be extended with codes from industry and elsewhere.</p>
    <h3 class="text-base">Use in Excel templates</h3>
    <p>All the codes in vocabularies allowed for use are supplied within the <a href="https://github.com/Kurrawong/gsq-geochem/raw/main/profiles/gsq/templates/GeochemXL-v3.0.xlsx" target="_blank">GeochemXL Template v3.0 <i class="pi pi-external-link"></i></a>. For example, the vocab for <em>Soil Colour</em> is:</p>
    <ul>
      <li>BLACK</li>
      <li>BLUE</li>
      <li>BROWN</li>
      <li>...etc</li>
    </ul>
    <p>These codes are available as drop-down values in the appropriate place in the GeochemXL Template v3.0 and must be used when the template is used.</p>
    <p>If the code you want is not already present in the Excel Template, you are allowed to add it, but you must define it. Instructions for this are contained within the Template itself.</p>
    <h3 class="text-base">Use in data</h3>
    <p>If you wish to use the vocab values in something other than the Excel template, for example in direct JSON or RDF data production according to this model, you will need not the short code for the vocab term such as <code>BLACK</code> as in the list above, but the full <em>IRI</em>, or persistent web identifier, of the term. For <code>BLACK</code> that is:</p>
      <p><code><a href="https://linked.data.gov.au/def/gsq-geochem/soil-colour/black">https://linked.data.gov.au/def/gsq-geochem/soil-colour/black</a></code></p>
    <p>The vocabularies are listed in the <a href="http://linked.data.gov.au/def/geochem#_gsq_profile">GSQ Profile of the Standard</a> and are also browsable online at the:</p>
    <ul>
      <li><a href="https://vocabs.gsq.digital/v" target="_blank">GSQ vocabulary server <i class="pi pi-external-link"></i></a></li>
    </ul>
    <p><em><strong>NOTE:</strong> A dedicated listing of the geochemistry vocabs will soon be made on that system!</em></p>
  </main>
</template>
