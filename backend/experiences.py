import requests
import json
import time

AI_API_URL = "https://ai.hackclub.com/chat/completions"

def parse_experiences_with_ai(experience_text, max_retries=2):
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

    for attempt in range(max_retries):
        print(f"Attempt {attempt+1}/{max_retries} to parse experiences...")
        response = requests.post(AI_API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            print(f"AI API error: {response.status_code}")
            continue

        try:
            ai_text = response.json()["choices"][0]["message"]["content"]
            parsed = json.loads(ai_text)

            if isinstance(parsed, list) and parsed:
                return parsed
            else:
                print("Empty or invalid parsed result, retrying...")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"JSON error: {e}, retrying...")

        time.sleep(1)

    print("All retries failed. Returning empty list.")
    return []

def parse_left_column_section_with_ai(section_name, section_text, max_retries=2):
    """
    Parse left column sections (Contact, Skills, Awards, etc) using AI.
    Returns a JSON array of strings, preserving multi-line content joined properly.
    Please be aware of when distinct items start and stop so that content that goes across multiple lines
    is preserved. Any links found should be continious and not broken up at all. only return valid JSON ONLY, no extra text.
    """
    prompt = (
        f"You are a resume parser.\n"
        f"Extract the {section_name} information into a JSON array of strings.\n"
        "Return valid JSON ONLY, no extra text.\n\n"
        f"Text:\n{section_text}"
    )

    messages = [{"role": "user", "content": prompt}]
    payload = {"messages": messages}
    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries):
        print(f"Attempt {attempt+1}/{max_retries} to parse {section_name}...")
        response = requests.post(AI_API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            print(f"AI API error: {response.status_code}")
            continue

        try:
            ai_text = response.json()["choices"][0]["message"]["content"]
            parsed = json.loads(ai_text)

            if isinstance(parsed, list) and parsed:
                return parsed
            else:
                print(f"Empty or invalid parsed {section_name} result, retrying...")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"JSON error: {e}, retrying...")

        time.sleep(1)

    print(f"All retries failed for {section_name}. Returning empty list.")
    return []
