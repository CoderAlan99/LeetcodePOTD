# LeetcodePOTD

This repository automatically fetches LeetCode's Daily Problem of the Day and creates a Python starter file for users to quickly begin working on the solution.

## Features

- **Daily Scheduler:** Uses GitHub Actions to fetch and generate a Python file for LeetCode's daily question every day.
- **File Naming Convention:** Each file is named as `YYYYMMDD-LC-QuestionNumber-QuestionTitle.py` for easy organization.
- **Problem Description:** The problem description is automatically included as a docstring at the top of each Python file.

## Usage

1. Clone the repository.
2. Open the latest daily Python file.
3. Read the problem description and start coding your solution in the provided template.

## Contributing

Feel free to submit your solutions as pull requests or open issues for improvements!

## Automation Details

- The scheduler is implemented via GitHub Actions in `.github/workflows/daily-leetcode.yml`.
- The fetching logic is in `fetch_leetcode_daily.py`, which scrapes the LeetCode daily question using their public GraphQL endpoint.

## Example

See [`20250907-LC-1-Two-Sum.py`](20250907-LC-1-Two-Sum.py) for a sample daily file.
