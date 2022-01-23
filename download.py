import requests, sys, json, regex

filename_pattern = regex.compile("(\d+.pdf)")

json_input = sys.argv[1].replace("'", "\"")
print(json_input)
urls = json.loads(json_input)

for url in urls:
    print(url)
    match = filename_pattern.search(url)
    if match:
        filename = match.group(1)
        with open("pdf/" + filename, "wb") as writer:
            result = requests.get(url)
            if result.status_code == 200:
                writer.write(result.content)
            else:
                print("problem: " + result.status_code)
