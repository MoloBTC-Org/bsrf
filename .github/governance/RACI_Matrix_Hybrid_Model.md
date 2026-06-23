# RACI Matrix – Hybrid Public Documentation Model
## For MoloBTC Repositories (THE STANDARD)

**Purpose**: Clarify accountability and responsibility in the hybrid governance model (open debate + strict publication control). This matrix can be copied into every new repository.

**Model Overview**:
- **Open Debate Layer**: Discussions + Issues (anyone can participate).
- **Controlled Publication Layer**: Pull Requests to protected `main` branch (only approved changes merge).

---

## RACI Matrix

| Activity / Decision                                      | Maintainers (Stewards) | CODEOWNERS          | Core Contributors (Write role) | Community / Public (Read + Discussions) | Project Board / Labels |
|----------------------------------------------------------|------------------------|---------------------|--------------------------------|-----------------------------------------|------------------------|
| **Open Debate in Discussions**                           | A / C                  | C                   | R                              | R                                       | I                      |
| **Create / Label Issues & Proposals**                    | A                      | C                   | R                              | R                                       | R                      |
| **Submit Pull Request**                                  | A                      | C                   | R                              | C (via fork)                            | I                      |
| **Review Pull Requests**                                 | A / R                  | R                   | C                              | I                                       | I                      |
| **Approve / Merge Changes to `main`**                    | A / R                  | R (path owners)     | C                              | I                                       | I                      |
| **Define / Update CODEOWNERS**                           | A / R                  | C                   | I                              | I                                       | I                      |
| **Set / Update Branch Protection Rules**                 | A / R                  | C                   | I                              | I                                       | I                      |
| **Manage Project Board & Custom Fields**                 | A / R                  | C                   | C                              | I                                       | R                      |
| **Enforce Code of Conduct**                              | A / R                  | C                   | C                              | I                                       | I                      |
| **Decide on Major Framework Changes**                    | A                      | R                   | C                              | C                                       | I                      |
| **Publish Official Releases / Versions**                 | A / R                  | C                   | I                              | I                                       | I                      |
| **Respond to Platform / Security Incidents**             | A / R                  | C                   | I                              | I                                       | I                      |
| **Update Governance Documents** (CONTRIBUTING, CoC, etc.)| A / R                  | C                   | C                              | I                                       | I                      |

---

## RACI Definitions Used

- **R** = Responsible (Does the work)
- **A** = Accountable (Final decision maker, "the buck stops here")
- **C** = Consulted (Must be consulted before decision/action)
- **I** = Informed (Kept up to date)

**Note**: In most cases, Maintainers hold both **A** and **R** for high-impact decisions. CODEOWNERS hold **R** for changes touching their owned paths.

---

## Key Governance Principles Embedded

- **Openness with Guardrails**: Anyone can debate and propose. Only approved, reviewed changes reach official publications.
- **Clear Accountability**: Maintainers are ultimately accountable for integrity of published content.
- **Path-based Ownership**: CODEOWNERS provide focused expertise and review on sensitive sections (e.g., legal, core frameworks).
- **Values Alignment**: All significant changes should be reviewed against Bitcoin sovereignty principles.

---

## How to Use This Matrix

1. Copy into `.github/governance/` of every new repository.
2. Customize owner names/teams as needed.
3. Reference it during onboarding of new contributors or when clarifying roles.
4. Update when the governance model evolves.

**Version**: 1.0 | Part of THE STANDARD governance suite.