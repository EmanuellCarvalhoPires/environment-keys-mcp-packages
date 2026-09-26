---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/bulk"
category: "Issues"
writes_data: true
tool_note: "[[jira_bulk_create_issue]]"
---
# Jira v3 - Bulk create issue

**Bulk create issue** — `POST /rest/api/3/issue/bulk`

- Run by the tool [[jira_bulk_create_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/bulk
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueUpdates": [
    {
      "fields": {
        "assignee": {
          "id": "5b109f2e9729b51b54dc274d"
        },
        "components": [
          {
            "id": "10000"
          }
        ],
        "customfield_10000": "09/Jun/19",
        "customfield_20000": "06/Jul/19 3:25 PM",
        "customfield_30000": [
          "10000",
          "10002"
        ],
        "customfield_40000": {
          "content": [
            {
              "content": [
                {
                  "text": "Occurs on all orders",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_50000": {
          "content": [
            {
              "content": [
                {
                  "text": "Could impact day-to-day work.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_60000": "jira-software-users",
        "customfield_70000": [
          "jira-administrators",
          "jira-software-users"
        ],
        "customfield_80000": {
          "value": "red"
        },
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order entry fails when selecting supplier.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "duedate": "2011-03-11",
        "environment": {
          "content": [
            {
              "content": [
                {
                  "text": "UAT",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "fixVersions": [
          {
            "id": "10001"
          }
        ],
        "issuetype": {
          "id": "10000"
        },
        "labels": [
          "bugfix",
          "blitz_test"
        ],
        "priority": {
          "id": "20000"
        },
        "project": {
          "id": "10000"
        },
        "reporter": {
          "id": "5b10a2844c20165700ede21g"
        },
        "security": {
          "id": "10000"
        },
        "summary": "Main order flow broken",
        "timetracking": {
          "originalEstimate": "10",
          "remainingEstimate": "5"
        },
        "versions": [
          {
            "id": "10000"
          }
        ]
      },
      "update": {
        "worklog": [
          {
            "add": {
              "started": "2019-07-05T11:05:00.000+0000",
              "timeSpent": "60m"
            }
          }
        ]
      }
    },
    {
      "fields": {
        "assignee": {
          "id": "5b109f2e9729b51b54dc274d"
        },
        "components": [
          {
            "id": "10000"
          }
        ],
        "customfield_10000": "09/Jun/19",
        "customfield_20000": "06/Jul/19 3:25 PM",
        "customfield_30000": [
          "10000",
          "10002"
        ],
        "customfield_40000": {
          "content": [
            {
              "content": [
                {
                  "text": "Occurs on all orders",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_50000": {
          "content": [
            {
              "content": [
                {
                  "text": "Could impact day-to-day work.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "customfield_60000": "jira-software-users",
        "customfield_70000": [
          "jira-administrators",
          "jira-software-users"
        ],
        "customfield_80000": {
          "value": "red"
        },
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order remains pending after approved.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "duedate": "2019-04-16",
        "environment": {
          "content": [
            {
              "content": [
                {
                  "text": "UAT",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "fixVersions": [
          {
            "id": "10001"
          }
        ],
        "issuetype": {
          "id": "10000"
        },
        "labels": [
          "new_release"
        ],
        "priority": {
          "id": "20000"
        },
        "project": {
          "id": "1000"
        },
        "reporter": {
          "id": "5b10a2844c20165700ede21g"
        },
        "security": {
          "id": "10000"
        },
        "summary": "Order stuck in pending",
        "timetracking": {
          "originalEstimate": "15",
          "remainingEstimate": "5"
        },
        "versions": [
          {
            "id": "10000"
          }
        ]
      },
      "update": {}
    }
  ]
}
```

## Original description

Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks. Transitions may be applied, to move the issues or subtasks to a workflow step other than the default start step, and issue properties set.

The content of each issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

Creating a subtask differs from creating an issue as follows:

 *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types).
 *  `parent` the must contain the ID or key of the parent issue.

**[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or subtask is created.
