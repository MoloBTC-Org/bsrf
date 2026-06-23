# Org Settings Configuration Checklist
## Lockdown / Hybrid / Open Modes for MoloBTC Repositories

**Purpose**: Quick-reference configuration guide to achieve the desired openness level while maintaining security and integrity. Use this when initializing any new MoloBTC repository.

**THE STANDARD Recommendation**: Most MoloBTC documentation and framework repositories should use **Hybrid** mode.

---

## 1. Organization-Level Settings (Apply Once per Org)

| Setting                                      | Lockdown Mode                  | Hybrid Mode (Recommended)          | Open Mode                     | Notes |
|----------------------------------------------|--------------------------------|------------------------------------|-------------------------------|-------|
| **Base Permissions** (for all members)      | Read or None                  | Read                              | Write or Admin               | Conservative base is strongly preferred |
| **Repository Creation**                     | Owners only                   | Owners + limited Members (private only) | Members (public + private)  | Restrict where possible |
| **Change Repository Visibility**            | Owners only                   | Owners only                       | Members                      | Critical control |
| **Invite Outside Collaborators**            | Owners only                   | Owners + Maintain role holders    | Members                      | High risk area |
| **Create Teams**                            | Owners only                   | Owners + Maintain role holders    | Members                      | — |
| **Allow Members to Change Repo Visibility** | Disabled                      | Disabled                          | Enabled (with caution)       | — |

**Recommended Default for New Orgs**: Start with **Hybrid** settings above.

---

## 2. Repository-Level Settings (Per Repo)

### Branch Protection (Main / Default Branch)

| Setting                                      | Lockdown Mode                          | Hybrid Mode (Recommended)                     | Open Mode                              |
|----------------------------------------------|----------------------------------------|-----------------------------------------------|----------------------------------------|
| Require Pull Request before merging         | Yes (2 approvals)                     | Yes (1–2 approvals)                          | Yes (1 approval)                      |
| Require review from Code Owners             | Yes                                   | Yes                                          | Optional                              |
| Require conversation resolution             | Yes                                   | Yes                                          | Recommended                           |
| Require signed commits                      | Yes                                   | Yes                                          | Recommended                           |
| Restrict who can push to matching branches  | Maintain + Admin only                 | Maintain + Admin only                        | Write + Maintain + Admin              |
| Allow force pushes                          | No                                    | No                                           | No (or limited to Maintain)           |
| Allow deletions                             | No                                    | No                                           | No                                    |
| Require status checks to pass               | Yes (if available)                    | Yes (if available)                           | Optional                              |

### Visibility & Access

| Setting                    | Lockdown Mode     | Hybrid Mode          | Open Mode       |
|---------------------------|-------------------|----------------------|-----------------|
| Repository Visibility     | Private           | Public               | Public          |
| Outside Collaborators     | Very limited      | Allowed (scoped)     | Freely allowed  |
| Wiki enabled              | No                | Optional             | Yes             |
| Issues enabled            | Yes (restricted)  | Yes                  | Yes             |
| Discussions enabled       | Yes (restricted)  | Yes (recommended)    | Yes             |
| Projects enabled          | Yes               | Yes                  | Yes             |

---

## 3. CODEOWNERS & Review Strategy

| Mode      | CODEOWNERS Strategy                              | Review Intensity |
|-----------|--------------------------------------------------|------------------|
| Lockdown  | Strict path-based ownership on all sensitive files | Very High       |
| **Hybrid**| Core files + high-sensitivity paths only        | High            |
| Open      | Core governance files only                       | Medium          |

**Recommended CODEOWNERS Pattern** (Hybrid):
```
/LICENSE.md
/CONTRIBUTING.md
/CODE_OF_CONDUCT.md
/SOVEREIGN-KNOWLEDGE-DECLARATION.md
/.github/          @JabulaniJakes @MoloBTC
```

---

## 4. Quick Decision Guide

**Use Lockdown Mode when**:
- Highly sensitive legal, financial, or body corporate documents.
- Very limited trusted contributors.
- Maximum confidentiality required.

**Use Hybrid Mode when** (Default for most MoloBTC repos):
- Public framework / documentation / knowledge work.
- Want broad community input via Discussions.
- Need strong protection on final published versions.

**Use Open Mode when**:
- Purely community-driven open source code projects.
- High contribution velocity is the priority.
- Lower sensitivity content.

---

**Usage**: Copy this checklist into `.github/governance/` of every new repository as a reference document. Update the owner handles as needed.

**Version**: 1.0 | Aligned with THE STANDARD governance model.