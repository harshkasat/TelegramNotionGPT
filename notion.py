import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()
import json
from datetime import datetime, timezone


token = os.getenv('NOTION_TOKEN')
dataset = os.getenv('DATABASE_ID')

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}
# title = "Test Title"
# description = "Test Description"
def createPage(message):
    message =  message.text
    message = message.split(",")
    title, youtube_url, blog_url = message[0], message[1], message[2]
    print(title, youtube_url, blog_url)
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": dataset },
        "properties": {
            "Descriptions": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": title,
                            }
                        }
                    ]
                },
            "Blog URL": {
                "url":blog_url
            
            },
            "Youtube URL": {
                    "url": youtube_url
                },
            }
        }
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)
    if res.status_code == 200:
        return True
    else:
        False
