<template>
  <main>
    <h1 class="text-4xl pb-4">The Standard</h1>
    <p>The Geochemistry Data Exchange Standard is a data model with supporting vocabularies (codelists), validation tools and Excel templates created by the <a href="https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq">Geological Survey of Queensland</a>.</p>
    <p>It is intended for use by companies supplying data to GSQ and perhaps later for the supply and exchange of geochemistry data throughout Australia.</p>
    <p>The Standard has a <a href="https://linked.data.gov.au/def/geochem/spec">formal Specification</a> as well as an <a href="https://linked.data.gov.au/def/geochem/overview">Overview document</a> as well as two <RouterLink to="/profiles">Profiles</RouterLink> of it.</p>
    <p>One of those Profiles - the <a href="http://linked.data.gov.au/def/geochem#_gsq_profile" target="_blank">GSQ Profile <i class="pi pi-external-link"></i></a> - also specifies codelist or vocabularies for use for particular reference values for units of measure, sample properties and so on.</p>
    <h3 class="text-base">If you don't know where to start, start with the <a href="https://linked.data.gov.au/def/geochem/overview">Overview document</a>!</h3>
    <h3 class="text-base">If you're ready to go, download the Excel Template from the <RouterLink to="/">Home Page of this Portal</RouterLink> and start loading data into it!</h3>
    <h3 class="text-base">If you want to produce data meeting this Standard directly from a database, see the <a href="https://kurrawong.github.io/gsq-geochem/spec.html#_model">Data Model Definition</a> and start producing JSON or RDF data.</h3>
  </main>
</template>
