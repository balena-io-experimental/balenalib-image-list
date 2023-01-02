from datetime import datetime
import json
import pandas as pd
import requests

print("Starting builder...", flush=True)

# Set username and database path
uname = "balenalib"
database_path = "./src/database/repos.json"
markdown_path = "./repos.md"
markdown_html_path = "./repos_html.md"

# Create an empty file with a JSON array in it
with open(database_path, "w") as f:
    f.write("[]")

# Set the Docker Hub repository path. The API allows a maximum of 100 results per page.
next_page = f"https://hub.docker.com/v2/repositories/{uname}/?page_size=100"

print("Fetching repositories...", flush=True)
# Loop until the "next" key is null
while next_page:
    repo_list = []
    # Get the response from the API endpoint
    response = requests.get(url=next_page)

    # Convert it to JSON
    data = response.json()

    # Set the "next" page URL
    next_page = data["next"]

    # Loop through the results
    for result in data["results"]:
        # Extract the name and add it as JSON
        repo_list.append({"name": result["name"]})

    # Open JSON file and flush the current content. This needs to be done in blocks to
    # avoid hangs when the array gets too large.
    with open(database_path, "r") as f:
        # Load the JSON file
        data = json.load(f)

        # For each JSON item append it to the list
        for item in repo_list:
            data.append(item)

        # Write the JSON to a file
        with open(database_path, "w") as f:
            json.dump(data, f, indent=2, sort_keys=False)

    # Print URL about to be processed
    if next_page:
        print(f"Processing {next_page}", flush=True)

# Open the database file and sort the JSON array alphabetically
with open(database_path, "r") as f:
    data = json.load(f)
    data.sort(key=lambda x: x["name"])

    # Write the JSON back to the file
    with open(database_path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=False)

# Turn each JSON object in to a markdown item with a clickable URL
markdown_data = []
for item in data:
    # Add a new key to markdown_data
    markdown_data.append(
        {
            "Container Name": f"[{item['name']}](https://hub.docker.com/r/{uname}/{item['name']})"
        }
    )

# Create a Pandas DataFrame from the JSON
df = pd.DataFrame(markdown_data, index=None)

# Write the JSON as Markdown
with open(markdown_path, "w") as f:
    f.write(df.to_markdown(index=False))

# Turn each JSON object in to a clickable HTML link in markdown
markdown_data = []
for item in data:
    # Add a new key to markdown_data
    markdown_data.append(
        {
            "Container Name": f'<a href="https://hub.docker.com/r/{uname}/{item["name"]}" target="_blank">{item["name"]}<a>'
        }
    )

# Create a Pandas DataFrame from the JSON
df = pd.DataFrame(markdown_data, index=None)

# Write the JSON as Markdown
with open(markdown_html_path, "w") as f:
    f.write(df.to_markdown(index=False))

print("Builder finished.", flush=True)
