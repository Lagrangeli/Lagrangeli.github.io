# Scholar Total Citation Auto-Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update only the homepage's total Google Scholar citation count once per day without an API key, while refusing incomplete or decreasing scrape results.

**Architecture:** A commit-pinned Google Scholar Fetcher Action writes a temporary publication list. A standard-library Python utility validates and sums that list, then updates the five existing homepage data copies atomically enough for a Git commit; the workflow commits only when the accepted total changes.

**Tech Stack:** GitHub Actions, Python 3 standard library, `unittest`, JSON, Jekyll/GitHub Pages.

---

## File Map

- Create `google_scholar_crawler/update_total.py`: validate fetched publication records and synchronize only the total citation value.
- Create `tests/test_scholar_total_update.py`: fixture-based behavior tests for calculation, monotonicity, metadata preservation, and unchanged data.
- Create `tests/test_scholar_workflow.py`: contract test for the no-secret daily workflow.
- Modify `.github/workflows/update-google-scholar.yml`: replace the failing multi-source crawler with the pinned fetcher and updater.
- Modify at runtime only when the citation count increases: `results/gs_data.json`, `_data/scholar.json`, `google_scholar_crawler/results/gs_data.json`, and both Shields.io JSON copies.

### Task 1: Citation Total Updater

**Files:**
- Create: `tests/test_scholar_total_update.py`
- Create: `google_scholar_crawler/update_total.py`

- [ ] **Step 1: Write failing calculation and synchronization tests**

Create tests that build all five data files under `tempfile.TemporaryDirectory()`. Use publication records `[{"citations": 120}, {"citations": 111}, {}]` and assert:

```python
records = [{"citations": 120}, {"citations": 111}, {}]
self.assertEqual(231, calculate_total(records))
self.assertTrue(update_total(root, 231, now="2026-08-20 12:00:00"))
```

Check that the three Scholar files contain `citedby == 231`, retain their original `hindex`, `i10index`, and `publications`, and set `fetch_strategy` and `citation_value_source` to `google-scholar-fetcher`. Check that both badge files contain `message == "231"`.

- [ ] **Step 2: Write failing safety tests**

Add separate tests for these contracts:

```python
with self.assertRaisesRegex(ValueError, "publication list is empty"):
    calculate_total([])

for records in ([{"citations": -1}], [{"citations": "12"}], {"citations": 12}):
    with self.subTest(records=records):
        with self.assertRaises(ValueError):
            calculate_total(records)

before = snapshot_files(root)
with self.assertRaisesRegex(ValueError, "lower than stored total"):
    update_total(root, 228)
self.assertEqual(before, snapshot_files(root))

before = snapshot_files(root)
self.assertFalse(update_total(root, 229))
self.assertEqual(before, snapshot_files(root))
```

- [ ] **Step 3: Run the tests and verify RED**

Run:

```bash
python3 -m unittest tests/test_scholar_total_update.py
```

Expected: import failure because `google_scholar_crawler.update_total` does not exist.

- [ ] **Step 4: Implement the minimal updater**

Implement these interfaces in `google_scholar_crawler/update_total.py`:

```python
DATA_PATHS = (
    Path("results/gs_data.json"),
    Path("_data/scholar.json"),
    Path("google_scholar_crawler/results/gs_data.json"),
)
BADGE_PATHS = (
    Path("results/gs_data_shieldsio.json"),
    Path("google_scholar_crawler/results/gs_data_shieldsio.json"),
)

def calculate_total(records: object) -> int:
    if not isinstance(records, list) or not records:
        raise ValueError("publication list is empty or invalid")
    total = 0
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("publication record is invalid")
        value = record.get("citations", 0)
        if type(value) is not int or value < 0:
            raise ValueError("citation value must be a non-negative integer")
        total += value
    return total

def update_total(root: Path, total: int, now: Optional[str] = None) -> bool:
    payloads = {path: read_json(root / path) for path in DATA_PATHS}
    stored_total = max(int(payload.get("citedby", 0)) for payload in payloads.values())
    if total < stored_total:
        raise ValueError(f"fetched total {total} is lower than stored total {stored_total}")
    if total == stored_total:
        return False
    timestamp = now or datetime.utcnow().isoformat(sep=" ")
    for path, payload in payloads.items():
        payload["citedby"] = total
        payload["fetch_strategy"] = "google-scholar-fetcher"
        payload["citation_value_source"] = "google-scholar-fetcher"
        payload["updated"] = timestamp
        payload.pop("last_fetch_error", None)
        write_json(root / path, payload)
    for path in BADGE_PATHS:
        payload = read_json(root / path)
        payload["message"] = str(total)
        write_json(root / path, payload)
    return True
```

Add a CLI that accepts `record_file` and optional `--root`, loads the records, calls both functions, and prints either `updated total citations to N` or `total citations unchanged at N`. Return nonzero naturally for invalid input.

Add one subprocess test with a malformed record file and assert a nonzero exit code, proving that invalid fetched data fails the workflow step instead of being silently accepted.

- [ ] **Step 5: Run updater tests and verify GREEN**

Run:

```bash
python3 -m unittest tests/test_scholar_total_update.py
```

Expected: all updater tests pass.

- [ ] **Step 6: Commit Task 1**

```bash
git add -- google_scholar_crawler/update_total.py tests/test_scholar_total_update.py
git commit -m "Add safe Scholar citation total updater"
```

### Task 2: Daily No-Secret Workflow

**Files:**
- Create: `tests/test_scholar_workflow.py`
- Modify: `.github/workflows/update-google-scholar.yml`

- [ ] **Step 1: Write a failing workflow contract test**

Read the workflow as text and assert that it contains:

```python
self.assertIn("cron: '17 2 * * *'", workflow)
self.assertIn("sxlllslgh/google-scholar-fetcher@4a30641f7dab085f01f99c38d38069d8aec2496f", workflow)
self.assertIn("google-scholar-id: r9f4mLMAAAAJ", workflow)
self.assertIn("python3 google_scholar_crawler/update_total.py /tmp/scholar-record.json --root .", workflow)
self.assertNotIn("SERPAPI_API_KEY", workflow)
self.assertNotIn("pip install", workflow)
```

Also assert that `git add --` names only the three Scholar JSON files and two badge files.

- [ ] **Step 2: Run the workflow test and verify RED**

Run:

```bash
python3 -m unittest tests/test_scholar_workflow.py
```

Expected: failures because the current workflow still installs the old crawler and references SerpAPI.

- [ ] **Step 3: Replace the workflow**

Keep `workflow_dispatch`, `contents: write`, and `pages: write`. Use one daily schedule at `17 2 * * *`, `actions/checkout@v4`, and:

```yaml
- name: Fetch Google Scholar publications
  uses: sxlllslgh/google-scholar-fetcher@4a30641f7dab085f01f99c38d38069d8aec2496f
  with:
    google-scholar-id: r9f4mLMAAAAJ
    record-file: /tmp/scholar-record.json

- name: Update total citation count
  run: python3 google_scholar_crawler/update_total.py /tmp/scholar-record.json --root .
```

In the commit step, configure the Actions bot, run `git add --` with exactly the five runtime data files, set `changed=false` when the staged diff is empty, and otherwise commit `Auto update Google Scholar citation total`, push the current branch, and set `changed=true`. Retain the existing conditional GitHub Pages build request.

- [ ] **Step 4: Run workflow and full local tests**

Run:

```bash
python3 -m unittest tests/test_scholar_workflow.py tests/test_scholar_total_update.py tests/test_cv_scholar_sync.py tests/test_cv_pagination.py
python3 -m py_compile google_scholar_crawler/update_total.py tests/test_scholar_total_update.py tests/test_scholar_workflow.py
git diff --check
```

Expected: all tests pass, Python compilation succeeds, and the diff check is empty.

- [ ] **Step 5: Commit Task 2**

```bash
git add -- .github/workflows/update-google-scholar.yml tests/test_scholar_workflow.py
git commit -m "Automate homepage Scholar citation total"
```

### Task 3: End-to-End Validation and Release Gate

**Files:**
- Verify only; no default-branch changes before approval.

- [ ] **Step 1: Exercise the updater against a temporary repository fixture**

Run the updater test suite and inspect the resulting fixture assertions. Do not run it against the real data files with invented citation values.

- [ ] **Step 2: Verify the complete commit scope**

Run:

```bash
git diff master...HEAD --check
git diff master...HEAD --stat
git status --short
```

Expected: only the design, plan, updater, two tests, and workflow are tracked changes; `.superpowers/` and `Zhenyang_Li___Resume/` remain untracked.

Also assert that `git diff --name-only master...HEAD` contains no `.pdf` path, so neither CV is regenerated by this feature.

- [ ] **Step 3: Request authorization to push the feature branch**

Do not push until the user approves the reviewed implementation. After approval:

```bash
git push -u origin codex/scholar-auto-update
gh workflow run update-google-scholar.yml --ref codex/scholar-auto-update
```

- [ ] **Step 4: Verify the real Action run**

Use `gh run list` and `gh run view --log` to confirm the fetch step succeeded, the updater reported a valid non-decreasing total, and the commit step either made no commit for an unchanged value or changed only the five data files.

- [ ] **Step 5: Present the verified result for final approval**

Report the live run URL, fetched total, changed files, tests, and any scraper limitation. Merge or fast-forward to `master` and push only after the user explicitly confirms deployment.
