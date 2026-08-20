# Scholar Total Citation Auto-Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update only the homepage's total Google Scholar citation count once per day through SerpAPI, while preserving the previous value on any invalid or decreasing result.

**Architecture:** A standard-library Python utility requests one Google Scholar Author API response from SerpAPI, validates the total, and synchronizes the existing homepage JSON files. GitHub Actions supplies the API key through a repository Secret, stages only runtime data files, and rebuilds GitHub Pages only after a real count change.

**Tech Stack:** GitHub Actions, Python 3 standard library, `unittest`, JSON, Jekyll/GitHub Pages.

---

### Task 1: Safe SerpAPI Total Updater

**Files:**
- Create: `google_scholar_crawler/update_total.py`
- Create: `tests/test_scholar_total_update.py`

- [x] **Step 1: Write failing SerpAPI parsing tests**

Use a successful fixture containing:

```python
{
    "search_metadata": {"status": "Success"},
    "cited_by": {"table": [{"citations": {"all": 231}}]},
}
```

Assert that `parse_serpapi_total()` returns `231`. Add failing fixtures for an API error, unsuccessful status, missing table, missing total, negative value, and string value.

- [x] **Step 2: Write failing synchronization safety tests**

Create all five runtime files in a temporary directory with a stored total of `229`. Assert that `231` updates every total while preserving h-index, i10-index, and publications; `229` performs no writes; and `228` raises before any file changes.

- [x] **Step 3: Implement the minimal updater**

Implement:

```python
def parse_serpapi_total(payload: object) -> int: ...
def fetch_serpapi_total(api_key: str, scholar_id: str) -> int: ...
def update_total(root: Path, total: int, now: Optional[str] = None) -> bool: ...
```

The CLI reads `SERPAPI_API_KEY`, defaults to Scholar ID `r9f4mLMAAAAJ`, performs one `google_scholar_author` request, and prints either `updated total citations to N` or `total citations unchanged at N`.

- [x] **Step 4: Verify Task 1**

Run:

```bash
python3 -m unittest tests/test_scholar_total_update.py
python3 -m py_compile google_scholar_crawler/update_total.py tests/test_scholar_total_update.py
```

Expected: all tests pass and Python compilation succeeds.

### Task 2: Daily SerpAPI Workflow

**Files:**
- Modify: `.github/workflows/update-google-scholar.yml`
- Create: `tests/test_scholar_workflow.py`

- [x] **Step 1: Write a failing workflow contract test**

Assert that the workflow:

```python
self.assertIn("cron: '17 2 * * *'", workflow)
self.assertIn("SERPAPI_API_KEY: ${{ secrets.SERPAPI_API_KEY }}", workflow)
self.assertIn("python3 google_scholar_crawler/update_total.py --root .", workflow)
self.assertNotIn("google-scholar-fetcher@", workflow)
self.assertNotIn("pip install", workflow)
```

Also assert that `git add --` stages exactly the three Scholar JSON files and two Shields.io JSON files.

- [x] **Step 2: Replace the scheduled path**

Use one daily cron entry, `actions/checkout@v4`, inject only `SERPAPI_API_KEY` into the updater step, and remove the dependency installation, direct Scholar scraper, manual floor input, and `git add -A`.

- [x] **Step 3: Verify Task 2**

Run:

```bash
python3 -m unittest tests/test_scholar_workflow.py tests/test_scholar_total_update.py
git diff --check
```

Expected: all tests pass and no whitespace errors are reported.

### Task 3: Release Gate

**Files:**
- Verify only before default-branch deployment.

- [x] **Step 1: Confirm the repository Secret exists**

Run `gh secret list` and confirm `SERPAPI_API_KEY` is present without reading or printing its value.

- [x] **Step 2: Run the complete local suite**

Run:

```bash
python3 -m unittest tests/test_scholar_workflow.py tests/test_scholar_total_update.py tests/test_cv_scholar_sync.py tests/test_cv_pagination.py
python3 -m py_compile google_scholar_crawler/update_total.py tests/test_scholar_total_update.py tests/test_scholar_workflow.py
git diff master...HEAD --check
```

Restore test-generated PDF byte changes and verify that the feature diff contains no `.pdf` path.

- [ ] **Step 3: Update the remote feature branch and dispatch the workflow**

Publish the revised feature snapshot without changing `master`, then run:

```bash
gh workflow run update-google-scholar.yml --ref codex/scholar-auto-update
```

- [ ] **Step 4: Verify the real SerpAPI run**

Confirm from the Actions log that the updater received a valid non-decreasing total, did not expose the Secret, and either made no commit for an unchanged value or changed only the five runtime data files.

- [ ] **Step 5: Request final deployment approval**

Report the run URL, fetched total, tests, changed files, and Pages behavior. Merge into `master` only after explicit user approval.
