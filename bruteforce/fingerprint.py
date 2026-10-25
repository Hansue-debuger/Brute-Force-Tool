import re

def is_success(resp_text, status, rules):
    # rules: dict with optional regex, body_len, cookie
    if "status" in rules and status != rules["status"]:
        return False
    if "regex" in rules and not re.search(rules["regex"], resp_text):
        return False
    if "body_len" in rules and len(resp_text) != rules["body_len"]:
        return False
    if "not_contains" in rules and rules["not_contains"] in resp_text:
        return False
    return True
