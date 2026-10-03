import re

content_path = r"C:\Users\babul\.gemini\antigravity-ide\brain\5701c2bc-aea9-43bf-9388-77019af0a65d\.system_generated\steps\181\content.md"
with open(content_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("Length of content:", len(text))
name_match = re.search(r'itemprop="name"[^>]*>([^<]+)</span>', text)
print("itemprop name:", name_match.group(1).strip() if name_match else "None")

login_match = re.search(r'class="p-nickname[^"]*"[^>]*>([^<]+)</span>', text)
print("Login:", login_match.group(1).strip() if login_match else "None")

bio_match = re.search(r'<div class="[^"]*user-profile-bio[^"]*"[^>]*>(.*?)</div>', text, re.DOTALL)
if bio_match:
    print("Bio:", re.sub(r'<[^>]+>', '', bio_match.group(1)).strip())

loc_match = re.search(r'itemprop="homeLocation"[^>]*>(.*?)</li>', text, re.DOTALL)
if loc_match:
    print("Location:", re.sub(r'<[^>]+>', '', loc_match.group(1)).strip())

soc_matches = re.findall(r'itemprop="social"[^>]*href="([^"]+)"', text)
print("Social links:", soc_matches)
