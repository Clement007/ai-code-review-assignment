AI Code Review Assignment (Python)
Candidate
Name: Munyentwari Clement
Approximate time spent: ~75 mins

Task 1 — Average Order Value
1) Code Review Findings
Critical bugs
Divides by total orders instead of valid non-cancelled ones → incorrect average.
Division by zero on empty list.
Edge cases & risks
Assumes all entries are dicts with numeric "amount".
Missing or malformed "amount" crashes.
Cancelled orders silently distort denominator.
Code quality / design issues
Explanation mismatch (claims correctness).
No input validation / graceful fallback.

2) Proposed Fixes / Improvements
Summary of changes
Filter denominator to match numerator (non-cancelled + numeric).
Skip malformed entries, add safe float conversion.
Return 0.0 when no valid entries.
Corrected code
See correct_task1.py
Testing Considerations
Focus on:
empty inputs, all cancelled, mixed cancelled/valid, malformed entries, and non-numeric amounts.
These validate correctness + robustness.

3) Explanation Review & Rewrite
Issues in original explanation
Claims correct exclusion of cancelled orders (false).
Ignores denominator bug + edge cases.
Rewritten explanation
Computes the average of non-cancelled orders only.
Skips malformed or non-numeric amounts.
Returns 0.0 if no valid non-cancelled orders exist.

4) Final Judgment
Decision: Request Changes
Justification: Intent clear, but core logic flawed.
Confidence & unknowns: High confidence, low ambiguity.

Task 2 — Count Valid Emails
1) Code Review Findings
Critical bugs
"@" in email is not a meaningful validity check.
Crashes on non-string values (e.g., None, numbers).
Edge cases & risks
Accepts invalid formats ("@", "a@", "@b", "a@b").
Cannot detect spaces or domain issues.
Code quality / design issues
Explanation over-states correctness.
Logic too naive for claimed behavior.

2) Proposed Fixes / Improvements
Summary of changes
Add lightweight structural validation.
Enforce: string, no spaces, exactly one "@", non-empty parts, domain contains ".".
Corrected code
See correct_task2.py
Testing Considerations
Test mixed valid/invalid, non-string values, spacing issues, minimal cases, empty list.
Covers interpretation + failure modes.

3) Explanation Review & Rewrite
Issues in original explanation
“Valid email” claim misleading.
“Safely ignores invalid entries” untrue (can crash).
Rewritten explanation
Counts how many items look like valid emails using simple structural checks.
Ignores non-string values and invalid formats.

4) Final Judgment
Decision: Request Changes
Justification: Concept correct but validator insufficient and unsafe.
Confidence & unknowns: High; expected for beginner validators.

Task 3 — Aggregate Valid Measurements
1) Code Review Findings
Critical bugs
Divides by len(values) instead of valid entries → wrong result.
Division by zero on empty values.
float(v) can throw on invalid types.
Edge cases & risks
None, strings, and mixed inputs not handled.
Explanation contradicts behavior.
Code quality / design issues
Invalid assumption about type safety.
Logical mismatch between stated and real behavior.

2) Proposed Fixes / Improvements
Summary of changes
Count only values that convert to float.
Skip None and non-numeric values.
Return 0.0 when no valid measurements.
Corrected code
See correct_task3.py
Testing Considerations
Check: empty, all invalid, mixed numeric + strings, None-heavy inputs, single value.
Validates handling + averaging logic.

3) Explanation Review & Rewrite
Issues in original explanation
Claims to ignore missing values and handle mixed types (false).
Claims accuracy while denominator contradicts it.
Rewritten explanation
Averages only values that successfully convert to float.
Skips None and non-numeric inputs.
Returns 0.0 if no valid values exist.

4) Final Judgment
Decision: Reject
Justification: Core averaging logic incorrect and contradicts own explanation.
Confidence & unknowns: High confidence; failure is fundamental rather than cosmetic.


