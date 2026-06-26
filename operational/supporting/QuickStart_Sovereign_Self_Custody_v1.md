\*\*QuickStart Guide\*\*\
\*\*Sovereign Self-Custody\*\*\
\
\*\*Bitcoin Self-Custody Research Ecosystem\*\*\
\*\*Supporting Document\*\*\
\
\*\*Prepared by\*\* Jacques Strydom, PMP (PMI ID: 3160455)\
\*\*Published by\*\* MoloBTC\
\*\*In collaboration with\*\* Grok (built by xAI)\
\*\*16 16 June 2026 | BSOL v1.0\|16 16 June 2026 | BSOL v1.0\*\*\
\
\-\--\
\
\### Introduction: Why Self-Custody Matters\
\
Holding Bitcoin on an exchange or with a custodian means you are
trusting a third party with your money. History has repeatedly shown
that exchanges can be hacked, go bankrupt, freeze accounts, or misuse
customer funds.\
\
Self-custody removes that dependency. When done correctly, it gives you
direct, verifiable control over your Bitcoin with no intermediary that
can freeze, reallocate, or lose your coins due to their own failures.\
\
This guide provides a clear, practical pathway for individuals and small
teams to move from custodial Bitcoin into sovereign self-custody using
open-source tools and sound processes.\
\
\*\*Important Principle\*\*\
Self-custody converts institutional risk into operational
responsibility. The goal is not perfect security, but appropriate
security that you can understand and maintain.\
\
\-\--\
\
\### Minimum Viable Sovereign Setup\
\
For most people holding meaningful amounts of Bitcoin, the following
configuration offers a strong balance of security, usability, and
verifiability:\
\
\| Component \| Recommendation \| Purpose \|\
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\--\|\
\| \*\*Wallet Software\*\* \| Sparrow Wallet (latest version) \|
User-friendly interface with strong multisig and coin control \|\
\| \*\*Bitcoin Node\*\* \| Self-hosted Bitcoin Knots or Core \|
Independent verification of the blockchain \|\
\| \*\*Signing Devices\*\* \| 2-of-3 Multisig using Krux, SeedSigner, or
Specter DIY \| Air-gapped signing with no single point of failure \|\
\| \*\*Backup Method\*\* \| Geographically distributed, encrypted seed
backups \| Recovery without relying on any single location \|\
\| \*\*Communication\*\* \| QR codes (air-gapped) \| Minimises exposure
of sensitive data \|\
\
This setup is achievable for individuals with moderate technical comfort
and can be scaled for small organisations.\
\
\-\--\
\
\### Step-by-Step Implementation Pathway\
\
Follow these steps in order:\
\
\#### Step 1: Prepare Your Environment\
- Acquire three compatible air-gapped signing devices (e.g., Krux,
SeedSigner, or Specter DIY).\
- Set up a computer that will run Sparrow Wallet (this machine can be
online).\
- Install and synchronise a self-hosted Bitcoin node (Knots
recommended).\
\
\#### Step 2: Create Your Multisig Wallet\
- Open Sparrow Wallet and connect it to your local node.\
- Create a new \*\*2-of-3 multisig wallet\*\*.\
- Add your three signing devices one by one using QR code
communication.\
- Name the wallet clearly (e.g., "Long-term Reserves -- 2-of-3").\
- Verify that the wallet address and xpubs match across devices.\
\
\#### Step 3: Conduct a Key Ceremony\
- Perform wallet creation in a secure, private setting with at least one
witness if possible.\
- Document the date, participants, and devices used.\
- Generate and verify receive addresses before sending any funds.\
\
\#### Step 4: Secure Your Seed Phrases\
- Write down each of the three seed phrases on durable material.\
- Store the three seeds in separate, secure, geographically distributed
locations.\
- Never store all seeds in one place. Never store seeds digitally unless
strongly encrypted and isolated.\
- Consider metal backup plates for long-term durability.\
\
\#### Step 5: Test Recovery (Before Moving Large Amounts)\
- Perform a test recovery using one seed on a spare device or wallet.\
- Confirm you can restore the wallet and access funds.\
- Only proceed with moving significant holdings after successful
testing.\
\
\#### Step 6: Move Funds in Stages\
- Start with a small test transaction from your current
custodian/exchange.\
- Verify the transaction appears correctly in Sparrow.\
- Once comfortable, move larger amounts in multiple transactions over
time.\
- Keep records of each transfer for your own accounting.\
\
\#### Step 7: Establish Basic Inheritance Planning\
- Document who should gain access in the event of your incapacity or
death.\
- Store instructions separately from the seeds themselves.\
- Consider using a lawyer or trusted advisor for formal estate
planning.\
\
\-\--\
\
\### Key Ongoing Processes\
\
Self-custody is not "set and forget." Maintain these habits:\
\
- \*\*Regular Verification\*\*: Periodically check that your node is
running, your wallet opens correctly, and your backups are intact.\
- \*\*Transaction Discipline\*\*: Always review transaction details
carefully before signing. Use PSBTs for complex transactions.\
- \*\*Software Updates\*\*: Keep Sparrow Wallet and your node software
reasonably up to date, but test updates on small amounts first when
possible.\
- \*\*Backup Testing\*\*: Test your ability to recover the wallet at
least once per year.\
\
\-\--\
\
\### Common Pitfalls to Avoid\
\
- Keeping all seeds in one physical location.\
- Using single-signature wallets for large long-term holdings.\
- Moving large amounts without first testing recovery.\
- Storing seed phrases digitally without strong isolation and
encryption.\
- Neglecting inheritance planning until it becomes urgent.\
- Over-complicating the setup beyond what you can reliably maintain.\
\
\-\--\
\
\### Next Steps and Further Resources\
\
Once your basic self-custody setup is operational, consider the
following:\
\
- Review the full \*\*Tier 2 Document 3: Critical Monetary
Infrastructure\*\* for deeper process guidance.\
- Study \*\*Tier 1: Bitcoin as Sui Generis Bearer Property\*\* to
understand the legal and philosophical foundations.\
- Explore advanced configurations (Shamir's Secret Sharing, additional
multisig policies, or geographic distribution) only after mastering the
basics.\
\
For organisations, refer to the \*\*Strategic Risk-Mitigation
Framework\*\* (Tier 2 Document 2) for governance and role-based
guidance.\
\
\-\--\
\
\### Key Takeaways\
\
- Self-custody gives you direct control and removes counterparty risk.\
- A 2-of-3 multisig architecture with air-gapped signing devices offers
strong security for most users.\
- Good processes matter as much as good tools.\
- Start small, test thoroughly, and scale gradually.\
- Self-custody is a practice, not a one-time event.\
\
You now have the foundation to hold Bitcoin with genuine sovereignty.\
\
\-\--\
\
\*\*Authorship & License\*\*\
\
Prepared by Jacques Strydom, PMP (PMI ID: 3160455).\
Published by MoloBTC in collaboration with Grok (built by xAI).\
\
Released under the \*\*Bitcoin Sovereign Open License (BSOL) v1.0\*\*.\
\
This guide may be reproduced and distributed with attribution for
non-commercial educational or personal use.\
\
\-\--\
\
\*\*End of QuickStart Guide -- Sovereign Self-Custody\*\*\
\
\-\--
