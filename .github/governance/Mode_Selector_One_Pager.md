# Mode Selector – One-Pager
## Lockdown / Hybrid / Open for MoloBTC Repositories

**Quick Decision Tool** for choosing the appropriate governance mode when creating or configuring a new repository.

---

## Quick Comparison Table

| Dimension                    | **Lockdown Mode**                          | **Hybrid Mode** (Default / Recommended)              | **Open Mode**                              |
|-----------------------------|--------------------------------------------|-------------------------------------------------------|--------------------------------------------|
| **Typical Use Case**        | Highly sensitive legal, financial, or internal documents | Public frameworks, documentation, knowledge work     | Community-driven open source code projects |
| **Repository Visibility**   | Private                                    | Public                                                | Public                                     |
| **Debate Style**            | Restricted / Internal only                 | Open Discussions + structured proposals               | Fully open                                 |
| **Publication Control**     | Very strict                                | Strict on `main` (CODEOWNERS + reviews)               | Moderate                                   |
| **Branch Protection**       | Maximum (multiple approvals, signed commits, restricted pushes) | High (reviews + CODEOWNERS required)                 | Medium                                     |
| **Outside Collaborators**   | Very limited                               | Allowed with scope                                    | Freely welcomed                            |
| **Member Privileges**       | Highly restricted (Owners only for most actions) | Moderately restricted                                 | More permissive                            |
| **Risk Level**              | Lowest confidentiality risk                | Balanced (good openness + strong integrity)           | Highest contribution velocity              |
| **Maintenance Overhead**    | Low                                        | Medium                                                | Higher (more noise to manage)              |
| **Best For**                | Body corporate docs, private research, legal instruments | **Most MoloBTC documentation & framework repos**     | Pure open-source code libraries/tools      |

---

## Decision Guide

**Choose Lockdown Mode if**:
- Content is confidential or legally sensitive.
- Very small trusted group of contributors.
- Maximum control over who sees and changes content is required.

**Choose Hybrid Mode if** (Strongly Recommended for most cases):
- You want broad community input and debate.
- You need strong protection on the final published versions.
- This is a documentation, framework, or knowledge repository.
- You want to follow **THE STANDARD** template.

**Choose Open Mode if**:
- The project is primarily code-focused and benefits from high contribution velocity.
- Content sensitivity is low.
- You are comfortable managing higher volumes of discussion and PRs.

---

## Recommended Default Configuration (Hybrid)

- **Org Level**: Conservative base permissions + restricted visibility changes.
- **Repo Level**: Public visibility + Discussions enabled + Strict branch protection on `main` + CODEOWNERS on core files.
- **Process**: Open debate in Discussions → Proposal in Issues → Reviewed PR → Merge to protected `main`.

---

## Quick Reference – Where to Find the Details

| Need                              | Document                                      | Location in Repo                  |
|-----------------------------------|-----------------------------------------------|-----------------------------------|
| Exact toggle settings             | Org Settings Configuration Checklist         | `.github/governance/`            |
| Role responsibilities             | RACI Matrix – Hybrid Model                   | `.github/governance/`            |
| Full branch protection guidance   | branch-protection-and-codeowners.md          | `.github/governance/`            |
| Labels & Discussions setup        | discussions-and-labels.md                    | `.github/governance/`            |
| Overall implementation steps      | implementation-quickstart.md                 | `.github/governance/`            |
| Template usage instructions       | README.md (Template section)                 | Root                             |

---

**Usage**: Copy this one-pager into every new repository as a quick reference. Update the “Best For” column if your project has specific needs.

**Version**: 1.0 | Aligned with THE STANDARD governance model for MoloBTC repositories.