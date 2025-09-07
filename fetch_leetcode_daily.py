import requests
import datetime
import re
import os


def get_daily_question():
    # LeetCode GraphQL endpoint
    url = "https://leetcode.com/graphql"
    query = {
        "operationName": "questionOfToday",
        "query": """
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            date
            question {
              questionId
              frontendQuestionId
              titleSlug
              title
              content
            }
          }
        }
        """,
        "variables": {}
    }
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/problemset/all/"
    }
    response = requests.post(url, json=query, headers=headers)
    response.raise_for_status()
    data = response.json()[
        "data"]["activeDailyCodingChallengeQuestion"]["question"]

    # Clean up title for filename
    title_clean = re.sub(r'[^a-zA-Z0-9]+', '-', data['title']).strip('-')
    date_str = datetime.datetime.utcnow().strftime('%Y%m%d')
    file_name = f"{date_str}-LC-{data['frontendQuestionId']}-{title_clean}.py"
    return file_name, data


def make_file(file_name, data):
    description = re.sub(r'<[^>]+>', '', data['content'])  # Remove HTML tags
    py_template = f'''"""
LeetCode Problem #{data['frontendQuestionId']}: {data['title']}
Date: {datetime.datetime.utcnow().strftime('%Y-%m-%d')}

{description}
"""

# Write your solution below

def solution():
    pass
'''
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(py_template)
    print(f"Created file: {file_name}")


if __name__ == "__main__":
    file_name, question_data = get_daily_question()
    # Avoid overwrite if file already exists
    if not os.path.exists(file_name):
        make_file(file_name, question_data)
    else:
        print(f"{file_name} already exists.")
