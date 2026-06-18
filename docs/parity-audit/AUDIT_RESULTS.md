# Parity Audit Results

Historical source: initial parity audit generated 2026-03-27 by a 3-agent
audit council.

This file is kept as the initial env0 parity baseline. Notebook files have
been ported into this directory with `mock-*` path/name updates, but should be
rerun before treating their results as current gates.

## Summary

| Environment | Correctness | Completeness | Readability | Status |
|-------------|-------------|--------------|-------------|--------|
| mock-gmail | NEEDS FIX | MOSTLY COMPLETE | CLEAR | Needs refresh |
| mock-gcal | PASS | MOSTLY COMPLETE | CLEAR | OK |
| mock-gdoc | NEEDS FIX | COMPLETE | CLEAR | Needs refresh |
| mock-gdrive | NEEDS FIX | INCOMPLETE | NEEDS POLISH | Needs refresh |
| mock-slack | FAIL | MOSTLY COMPLETE | NEEDS POLISH | Needs refresh |

## Initial Must-Fix Items

- [x] Slack notebook: wrong metadata keys and total endpoint count.
- [x] Slack notebook: standardize blocking threshold to 80%/90%.
- [x] GDoc: invalid JSON in API spec.
- [x] GDrive: add missing fixture comparisons.
- [x] Gmail: add missing fixtures to aggregate calls.
- [x] GDrive: fix lambda closure bug.
- [ ] Add error response testing to GCal, Gmail, GDrive, Slack parity audits.
- [ ] Add pagination testing to all parity audits.
- [x] Standardize severity definitions.
- [x] Add definitions for golden fixtures and shape comparison.

## Fixture Capture Status

Historical initial-audit fixtures were captured 2026-03-27:

- Gmail: 34 fixtures
- GCal: 29 fixtures
- GDocs: 9 fixtures
- GDrive: 41 fixtures
- Slack: 52 fixtures
- Total: 165 golden fixtures

Current env0 real golden fixture count:

- Gmail: 35 fixtures
- GCal: 31 fixtures
- GDocs: 6 fixtures
- GDrive: 42 fixtures
- Slack: 57 fixtures
- Total: 171 golden fixtures

## env0 Refresh Needed

- Verify all paths/names use current `mock-*` contracts.
- Verify fixture coverage maps under each `packages/environments/mock-*`.
- Add missing error response tests.
- Add pagination tests where APIs support pagination.
- Re-run conformance suites after any fixture refresh.
