# Google Scholar Total Citation Auto-Update Design

## Goal

Automatically keep only the homepage's total Google Scholar citation count current. The feature does not regenerate either CV PDF, change the homepage layout, or automatically replace the stored h-index and i10-index.

## Data Source Decision

The initial no-secret design used `sxlllslgh/google-scholar-fetcher`. Both a local probe and GitHub Actions run `32385686195` received Google's HTML anti-bot page instead of JSON, so that route was rejected before deployment.

The implemented route uses the Google Scholar Author API provided by SerpAPI. Its key is stored only as the repository Actions secret `SERPAPI_API_KEY` and is never written to files or logs.

## Data Flow

1. A GitHub Actions workflow runs once per day at 02:17 UTC and can also be started manually.
2. `google_scholar_crawler/update_total.py` requests the SerpAPI author record for Scholar profile `r9f4mLMAAAAJ` using only Python's standard library.
3. The updater accepts a total only when SerpAPI reports a successful search and returns a non-negative integer in `cited_by.table[].citations.all`.
4. A total lower than the largest stored total is rejected. An unchanged total produces no file writes.
5. A higher total is synchronized to the three existing Scholar JSON files and two Shields.io JSON files. Existing publications, h-index, i10-index, and other Scholar data are preserved.
6. The workflow stages exactly those five runtime files, commits only when they changed, pushes the current branch, and requests a GitHub Pages rebuild.

## Failure Handling

- A missing Secret, HTTP failure, invalid API response, missing total, malformed value, or decreasing total fails the workflow before any commit.
- Fetch and validation happen before runtime files are written.
- The previous public value remains available when a scheduled update fails.

## Verification

Unit tests cover SerpAPI response parsing, malformed and failed responses, higher totals, unchanged totals, decreasing totals, metadata preservation, missing Secret behavior, and exact workflow staging scope. A manual feature-branch Action run must succeed before the implementation is merged into `master`.
