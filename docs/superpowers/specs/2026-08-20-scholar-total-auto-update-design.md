# Google Scholar Total Citation Auto-Update Design

## Goal

Automatically keep the homepage's total Google Scholar citation count current without requiring an API key. The change is limited to the homepage data files; it does not regenerate either CV PDF or alter the homepage layout.

## Data Flow

1. A scheduled GitHub Actions workflow runs once per day and can also be started manually.
2. A commit-pinned version of `sxlllslgh/google-scholar-fetcher` retrieves the public publication list for Scholar profile `r9f4mLMAAAAJ` into a temporary JSON file.
3. A small standard-library Python updater sums the per-publication citation counts.
4. The updater writes the accepted total to the existing homepage data files:
   - `results/gs_data.json`
   - `_data/scholar.json`
   - `google_scholar_crawler/results/gs_data.json`
   - the corresponding Shields.io JSON files
5. The workflow commits only when the accepted total changes. A successful push triggers the existing GitHub Pages rebuild.

## Safety Rules

- Reject empty, malformed, non-integer, or negative citation values.
- Reject an empty publication list.
- Never replace the stored citation total with a lower value. This protects the homepage from partial Scholar responses and temporary scraper failures.
- Preserve the existing JSON structure and all metrics other than the total citation count.
- When fetching or validation fails, fail the workflow and leave the published value unchanged.

## Workflow Simplification

The current multi-source crawler, dependency installation, SerpAPI fallback, manual floor, and timestamp-only commits are removed from the scheduled path. The workflow needs no repository secret and performs no commit when the citation total is unchanged.

## Verification

Unit tests use local fixtures to verify:

- citation values are summed correctly;
- a higher total updates every homepage data copy;
- an unchanged total produces no file changes;
- a lower, empty, or malformed result is rejected;
- unrelated Scholar metadata remains unchanged.

After implementation, the workflow is manually dispatched once on the feature branch. Its output, generated JSON, commit scope, and homepage rendering are checked before merging or pushing to the default branch.
