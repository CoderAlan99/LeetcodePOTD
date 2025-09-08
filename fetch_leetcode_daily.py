import requests
from bs4 import BeautifulSoup

API_URL = "https://alfa-leetcode-api.onrender.com/dailyQuestion"


def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")

    # Inline formatting
    for code in soup.find_all("code"):
        code.replace_with(f"`{code.get_text()}`")
    for strong in soup.find_all("strong"):
        strong.replace_with(f"{strong.get_text()}")

    # Examples and code blocks
    for pre in soup.find_all("pre"):
        text = pre.get_text().strip()
        pre.replace_with(f"\n```\n{text}\n```\n")

    # Lists
    for li in soup.find_all("li"):
        li.insert_before("• ")
        li.append("\n")

    # Convert everything to text
    text = soup.get_text()
    # Collapse multiple newlines into max 2
    text = "\n".join([line.strip()
                     for line in text.splitlines() if line.strip()])
    return text


def fetch_daily_question():
    response = requests.get(API_URL)
    data = response.json()["data"]["activeDailyCodingChallengeQuestion"]

    description_text = html_to_markdown(data["question"]["content"])

    result = {
        "date": data["date"],
        "title": data["question"]["title"],
        "description": description_text,
        "topics": [tag["name"] for tag in data["question"]["topicTags"]],
        "link": f"https://leetcode.com{data['link']}"
    }
    return result


def pretty_print(daily):
    print(f"📅 Date: {daily['date']}")
    print(f"📝 Title: {daily['title']}\n")
    print("📖 Description:\n")
    print(daily['description'])
    print("\n🏷 Topics: " + ", ".join(daily['topics']))
    print(f"🔗 Link: {daily['link']}")


if __name__ == "__main__":
    daily = fetch_daily_question()
    pretty_print(daily)
