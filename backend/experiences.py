import requests
import json

AI_API_URL = "https://ai.hackclub.com/chat/completions"

def parse_experiences_with_ai(experience_text):
    prompt = (
        "You are a resume parser.\n"
        "Extract the following work experiences into a JSON array of objects, "
        "each with keys: company, title, date, location, description.\n"
        "Return valid JSON ONLY, no extra text.\n\n"
        "Experiences:\n"
        + experience_text
    )

    messages = [{"role": "user", "content": prompt}]
    payload = {"messages": messages}
    headers = {"Content-Type": "application/json"}

    response = requests.post(AI_API_URL, headers=headers, data=json.dumps(payload))

    # print("Status:", response.status_code)
    # print("Response:", response.text)

    if response.status_code != 200:
        raise Exception(f"AI API error: {response.status_code} {response.text}")

    data = response.json()
    ai_text = data["choices"][0]["message"]["content"]

    try:
        parsed = json.loads(ai_text)
    except json.JSONDecodeError:
        print("Warning: AI did not return valid JSON, returning empty list.")
        parsed = []

    return parsed
