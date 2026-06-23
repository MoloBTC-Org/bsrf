# Branch Protection Ruleset + CODEOWNERS Configuration
## For Public Legal-Level & Framework Documentation Repositories

**Purpose**: Enforce strict control over the official `main` branch while allowing open contributions via Pull Requests. This keeps official publications neat, tidy, and high-quality.

### 1. Recommended Branch Protection Rules (for `main` branch)

Go to **Repository Settings → Branches → Branch protection rules → Add rule** for the `main` branch.

**Recommended Settings**:

- **Require a pull request before merging**
  - Required approvals: **1** or **2**
  - Dismiss stale pull request approvals when new commits are pushed: **Enabled**
  - Require review from Code Owners: **Enabled** (critical)

- **Require status checks to pass before merging** (Optional but recommended if you have CI)

- **Require conversation resolution before merging**: **Enabled**

- **Require signed commits**: **Enabled** (strong recommendation for auditability and sovereignty alignment)

- **Do not allow bypassing the above settings**: **Enabled**

- **Restrict who can push to matching branches**
  - Only allow users with **Maintain** or **Admin** role to push directly

- **Allow force pushes**: **Disabled**
- **Allow deletions**: **Disabled**

### 2. CODEOWNERS File

The `.github/CODEOWNERS` file has already been created with the correct maintainers.

### 3. Implementation Steps

1. The `.github/CODEOWNERS` file is already in place.
2. Go to Settings → Branches and add the protection rule as described above.
3. Communicate the new process clearly in Discussions and the README.

This configuration delivers **strict edit control** on official content while keeping the contribution process open and welcoming.
