# GitHub Projects Board Template
## Portfolio / Framework Evolution Tracking Board

**Board Name Recommendation**: `Framework Evolution & Publication Tracker`

### Purpose
Provide visibility into the full lifecycle of ideas → debate → proposal → official publication, while respecting the open debate + controlled edit model.

### Recommended Board Structure (Views)

Create one Project (Table + Board views recommended).

#### View 1: Lifecycle Board (Kanban-style)
Columns / Statuses:

1. **Ideas & Open Debate** (Discussions & early Issues)
2. **Structured Proposals** (Labeled Issues ready for work)
3. **In Draft / PR Open** (Active Pull Requests)
4. **Under Review** (Awaiting Maintainer / CODEOWNERS approval)
5. **Approved & Merging**
6. **Published** (Official version released)

#### View 2: By Category
Group by the Discussions category or primary label (`framework-debate`, `values-alignment`, `legal-review`, etc.)

#### View 3: Needs Attention
Filter for items with `needs-discussion`, `legal-review`, or stale items.

### Custom Fields (Highly Recommended)

Add these fields to every item:

| Field Name                    | Type          | Purpose / Options |
|-------------------------------|---------------|-------------------|
| `Values Alignment`            | Single Select | High / Medium / Low / Needs Discussion |
| `Legal / Governance Impact`   | Single Select | High / Medium / Low / None |
| `Clarity & Neatness Risk`     | Single Select | High / Medium / Low |
| `Priority`                    | Single Select | Critical / High / Medium / Low |
| `Bitcoin Values Tags`         | Multi Select  | Sovereignty, Sound Money, Voluntaryism, Verifiable Systems, Privacy, Open Debate |
| `Target Publication`          | Text / Date   | Which document/version this affects |
| `Reviewers`                   | People        | Assigned Maintainers / CODEOWNERS |
| `Discussion Link`             | URL           | Link to originating GitHub Discussion |
| `Status Note`                 | Text          | Free-text progress note |

### Automation Ideas (or Manual Process)

- When a PR is opened → Move item to "In Draft / PR Open" and set status to `under-review`
- When PR is merged → Move to "Published" and update `Values Alignment` if needed
- Use labels to auto-populate some fields where possible

### How to Set Up

1. Create a new **Project** in your organization or repository.
2. Add the above Views and Custom Fields.
3. Link relevant repositories (this public docs repo + any related code repos).
4. Start by importing or creating items from existing Discussions and Issues.
5. Share the board link in the README and pinned Discussions for transparency.

This board gives the entire community visibility into how ideas become official publications without compromising control over the final output.
