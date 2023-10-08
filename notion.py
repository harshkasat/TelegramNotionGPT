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
# title='noice'
# youtube_url='notion'
# blog_url= 'xyz'
# description = "Test Description"
def createPage(title, youtube_url):
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
# createPage('thsi very noice i like it very much', ['i dont about but i like it', "I'm Batman" ], 'Let make peace around me')