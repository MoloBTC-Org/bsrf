# Portugal – Tax Framework

**Charging, Reporting, Capital-Flow Interface & Sui Generis Treatment**

**Bitcoin Sovereignty Research Framework (BSRF) — Tax Track**

**Prepared by** Jacques Strydom, PMP  
**In collaboration with** Grok (xAI)  
**Published by** MoloBTC  
**Updated:** 29 September 2026  
**License** Bitcoin Sovereign Open Source License (BSOL) v1.0

**Canonical Repository** https://github.com/MoloBTC-Org/bsrf

**Status** Research note. Not a filing. Does not amend the South African SARS letter of 31 August 2026 or the FinSurv Annexure A comment of 25 September 2026.

This is the Portugal nation file on the tax track. Instrument citations (CIRS Articles 10(19) and 10(20); AT Informação Vinculativa n.º 28969) live in the sections below. They are not the filename.

---

## 1. Purpose

This document records the domestic Portuguese personal-income-tax treatment of crypto-assets as it stands for BSRF comparative work, with particular attention to:

- the 365-day capital-gains exclusion in the Código do IRS (CIRS);
- the October 2025 Autoridade Tributária e Aduaneira (AT) binding information on an immediate “technical conversion” of a crypto-asset into a stablecoin immediately before a euro disposal (Processo / Informação Vinculativa n.º 28969);
- the territorial limitation that now conditions both the deferral and the long-term exclusion;
- what this regime does, and does not, supply for the *sui generis* / adjacent-currency thesis.

It is a factual companion to *Bitcoin_as_Sui_Generis_Bearer_Property_Tax_Implications_v0.1.md* and to *Global_CARF_History_Precedents_and_Governing_Bodies.md*. It is not Portuguese legal advice.

---

## 2. Statutory baseline (CIRS)

The 2023 State Budget (Lei n.º 24-D/2022) inserted a dedicated crypto-asset regime into the Personal Income Tax Code. The two provisions that matter for this note are:

- **Article 10(19) CIRS** — a capital gain on a crypto-asset held for 365 days or more is excluded from IRS, subject to the territorial condition described in section 4.
- **Article 10(20) CIRS** — a crypto-to-crypto exchange is not, of itself, a taxable disposal. The acquisition value of the asset delivered rolls into the asset received. Tax is deferred until a conversion into legal-tender currency, or into non-crypto goods, assets or services.

Those two articles already encode a realised-gains principle. Holding is not the event. A peer swap is not the event. The euro (or other fiat / non-crypto) interface is the event. That architecture is closer to the BSRF tax thesis than an undifferentiated “every token movement is a disposal” rule.

The 365-day clock is generally treated as restarting on an ordinary swap. Processo 28969 is the narrow administrative exception to that restart.

---

## 3. Binding information n.º 28969 (31 October 2025)

### 3.1 What was asked

A taxpayer who had held a crypto-asset for more than 365 days asked the AT how to treat a two-step cash-out:

1. conversion of that asset into a stablecoin (for example USDC) because the venue had no direct euro pair; and
2. immediate conversion of the stablecoin into euros.

The question was whether the long-term exclusion still attached to the final euro conversion, or whether the stablecoin leg reset the clock and crystallised a gain.

### 3.2 What the AT said

Secondary sources that have worked from the text of the information (including Cuatrecasas and subsequent practitioner notes) report the same holding:

- the intermediate conversion into the stablecoin, where it is **instrumental and immediate**, is a “technical conversion” with **no independent tax relevance**;
- the taxable event, if any, arises only on the final conversion into euros;
- if the original asset had already been held for 365 days or more, the gain on that final conversion remains excluded under Article 10(19);
- the AT treats the two legs as one continuous process of realisation.

The information does not rewrite Article 10. It reads a liquidity bridge as not being a separate disposal.

### 3.3 Limits of the instrument

A binding information answers the taxpayer who asked it and binds the AT to that taxpayer on those facts. It is not a statute. Practitioner commentary (Cuatrecasas, December 2025) records that “technical conversion” has no express hook in the CIRS and therefore remains open to later tightening or to a different reading on different facts.

Consequences for this file:

- do not cite Processo 28969 as if it were Article 10(21);
- do not treat a delayed or speculative stablecoin parking as covered;
- do not treat DeFi routing, lending, or yield as covered — those were not the facts.

---

## 4. Territorial condition

Both the crypto-to-crypto deferral and the 365-day exclusion are now read as applying only where the relevant counterparties (including the venue) are resident in:

- the European Union or the European Economic Area; or
- a jurisdiction with which Portugal has a double-tax treaty and/or a tax-information-exchange arrangement.

A technical swap executed on a venue that fails that test is outside the protection described in section 3. DAC8 / CRS reporting from 1 January 2026 makes that geography visible to the AT whether or not the taxpayer volunteers it.

---

## 5. What the Portuguese regime does not do

The CIRS and Processo 28969 do **not**:

- declare Bitcoin legal tender, or make the Banco de Portugal a guarantor;
- treat a fiat-referenced stablecoin as Bitcoin, as *sui generis* bearer property, or as an adjacent currency — a USD-referenced stablecoin remains an issued token and a central-bank-proxy instrument;
- put self-custody or personal node operation outside Portuguese criminal or tax law;
- exempt professional / Category B activity, staking characterised as Category E, or mining characterised under the simplified regime;
- create a South African (or any other) election form, nomination, or “medium swap” statute.

The 365-day exclusion is a **holding-period filter on a realised fiat interface**. It is not a statement that the unit is cash, and it is not a statement that mere possession is untaxable in every other jurisdiction.

---

## 6. Relevance to the BSRF tax thesis

Portugal is useful to the track for three reasons, and dangerous if over-read.

**Useful.** Article 10(20) already separates the swap from the tax event. Processo 28969 then refuses to let a liquidity-bridge stablecoin manufacture a second event. That is the same distinction the South African SARS letter asked for in principle: tax realised local activity, not the intermediate rail. It is also consistent with the FinSurv comment’s refusal to treat every token movement as an export.

**Limited.** The Portuguese exclusion is time-based (365 days) and geographically conditioned. BSRF’s *sui generis* claim is character-based (no issuer, title follows the key, holding and self-custody are not events). A 365-day holiday is a policy concession, not a recognition of bearer-protocol character. Do not collapse the two.

**Stablecoins.** The ruling uses a stablecoin as a technical bridge. It does not reclassify that token as Bitcoin. The issued-asset / central-bank-proxy sentence already in the South African FinSurv comment remains the correct genus split.

---

## 7. Reporting overlay (DAC8)

Portugal applies the EU DAC8 crypto-asset reporting framework from 1 January 2026. Reporting Crypto-Asset Service Providers collect identity and transaction data for automatic exchange. Self-custody users are not themselves DAC8 reporters. Intermediary contact remains the reporting surface, as under CARF in other jurisdictions.

DAC8 does not change the CIRS charging provisions. It changes what the AT can see.

---

## 8. Sources and portal position

Primary instrument:

- Autoridade Tributária e Aduaneira, Informação Vinculativa / Processo n.º 28969, despacho of 31 October 2025.

The full text is not published as an open PDF on [portaldasfinancas.gov.pt](https://www.portaldasfinancas.gov.pt) in the same way a circular is. Binding information is typically released to the requesting taxpayer and then circulated through practitioner channels. This file therefore relies on:

- Cuatrecasas, “Personal income tax cryptoassets ‘technical conversion’” / “IRS e Criptoativos: A ‘Conversão Técnica’” (10 December 2025), citing Binding ruling no. 28969 of 31 October 2025;
- subsequent practitioner notes that reproduce the same holding (GoalSeek; DAX Digital Assets Explorer);
- the CIRS text of Articles 10(19) and 10(20) as described in AT’s own crypto-asset folheto and in the 2023 Budget statute.

If the AT later publishes the information on the Portal das Finanças, the official URL should replace the secondary citations in a dated research revision of this file. Until then, do not pretend a portal PDF exists.

Official orientation material (not the ruling itself):

- AT folheto *Criptoativos* — [info.portaldasfinancas.gov.pt](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/Criptoativos.pdf)

---

## 9. Cross-references

- Normative foundations: *Bitcoin_as_Sui_Generis_Bearer_Property_Tax_Implications_v0.1.md*
- International reporting history: *Global_CARF_History_Precedents_and_Governing_Bodies.md*
- South Africa CARF companion: *South_Africa_CARF_Implementation_Status.md*
- Formal SARS submission (context only): *Objection_and_Recommendations_SARS_Draft_Guide_Taxation_Crypto_Assets_2026.md*
- FinSurv Annexure A comment (context only; filed text dated 25 September 2026): *draft_manual/Annexure_A_Comments_Draft_Crypto_Asset_Manual_Cross_Border_2026.pdf*

---

## 10. Repo placement

Upload path on the canonical repository:

`tax_track/jurisdictions/Portugal/Portugal.md`

Do not place this file under South Africa. Do not attach it to the FinSurv covering email. Do not treat it as an amendment of any filed South African instrument.

---

**Prepared by** Jacques Strydom, PMP  
**Published by** MoloBTC  
**License** BSOL v1.0
