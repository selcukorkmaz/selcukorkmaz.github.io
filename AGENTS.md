# Persistent review and verification rule

Applies to every task and future session in this repository. User reaffirmed on 9 October 2026:

> I don't want to get into the loop where I ask you to review and you find new issues in every checking. Instead I want a detailed check at once where you check and confirm every claim iteratively with several rounds until you are confident there are no issues. If so, review and check the last updates based on that.

- Verification is part of the original task, before presenting any result, including drafts, factual chat statements, code, files and figures.
- Perform at least two substantive rounds. First verify every claim and changed behavior against primary sources, recalculation or execution. Then independently challenge the full result using counterexamples, boundary cases, failure paths and dependency checks; repeating a passing command is not another substantive round.
- Check all factual claims, numbers, calculations, quotations, internal consistency, applicable instructions, language and formatting. Recalculate counts from files; search quotations in their sources. Label anything that cannot be verified explicitly as unverified.
- After corrections, repeat the full verification round. Stop only after a complete round introduces no new findings or corrections. For an audit, record unresolved defects clearly rather than claiming they are fixed.
- Keep a concise verification record: reviewed scope, evidence, rounds, corrections, remaining findings and unverified items. Present one consolidated report rather than deferring checks to subsequent user requests.
- Distinguish “no new findings in the reviewed scope” from “all reported defects are fixed.” Never claim tests establish that an application has no bugs.
- Later reviews cover only the latest changes and their dependencies. Do not reopen resolved findings without new evidence. Label a genuine earlier oversight “missed in the earlier review.”
- Acceptance of a decision does not lock a step; obtain explicit approval if a step needs to be locked.

<claude-mem-context>
# Memory Context

# claude-mem status

This project has no memory yet. The current session will seed it; subsequent sessions will receive auto-injected context for relevant past work.

Memory injection starts on your second session in a project.

`/learn-codebase` is available if the user wants to front-load the entire repo into memory in a single pass (~5 minutes on a typical repo, optional). Otherwise memory builds passively as work happens.

Live activity: http://localhost:37777
How it works: `/how-it-works`

This message disappears once the first observation lands.
</claude-mem-context>
