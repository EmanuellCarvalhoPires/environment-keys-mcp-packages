---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}"
category: "Reports"
writes_data: true
tool_note: "[[bitbucket_create_or_update_a_report]]"
---
# Bitbucket - Create or update a report

**Create or update a report** — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`

- Run by the tool [[bitbucket_create_or_update_a_report]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit the report belongs to.
- `reportId` (path, string, required) — Either the uuid or external-id of the report.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates or updates a report for the specified commit.
To upload a report, make sure to generate an ID that is unique across all reports for that commit. If you want to use an existing id from your own system, we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-001.

### Sample cURL request:
```
curl --request PUT 'https://api.bitbucket.org/2.0/repositories///commit//reports/mysystem-001' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Security scan report",
    "details": "This pull request introduces 10 new dependency vulnerabilities.",
    "report_type": "SECURITY",
    "reporter": "mySystem",
    "link": "http://www.mysystem.com/reports/001",
    "result": "FAILED",
    "data": [
        {
            "title": "Duration (seconds)",
            "type": "DURATION",
            "value": 14
        },
        {
            "title": "Safe to merge?",
            "type": "BOOLEAN",
            "value": false
        }
    ]
}'
```

### Possible field values:
report_type: SECURITY, COVERAGE, TEST, BUG
result: PASSED, FAILED, PENDING
data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

#### Data field formats
| Type  Field   | Value Field Type  | Value Field Display |
|:--------------|:------------------|:--------------------|
| None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
| BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
| DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp (milliseconds) and will be displayed as a relative date if the date is less than one week ago, otherwise  it will be displayed as an absolute date. |
| DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed in a human readable duration format. |
| LINK | Object: `{"text": "Link text here", "href": "https://link.to.annotation/in/external/tool"}` | The value will be read as a JSON object containing the fields "text" and "href" and will be displayed as a clickable link on the report. |
| NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in a human readable format (e.g. 14.3k). |
| PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and 100 and will be displayed with a percentage sign. |
| TEXT | String | The value will be read as a JSON string and will be displayed as-is |

Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information.
