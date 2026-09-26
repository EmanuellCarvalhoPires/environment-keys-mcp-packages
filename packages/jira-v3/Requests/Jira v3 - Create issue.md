---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue"
category: "Issues"
writes_data: true
tool_note: "[[jira_create_issue]]"
---
# Jira v3 - Create issue

**Create issue** — `POST /rest/api/3/issue`

- Run by the tool [[jira_create_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue?updateHistory={{param:updateHistory}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `updateHistory` (query, string, optional) — Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
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
    "duedate": "2019-05-11",
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
    "parent": {
      "key": "PROJ-123"
    },
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
  "update": {}
}
```

## Original description

Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition may be applied, to move the issue or subtask to a workflow step other than the default start step, and issue properties set.

The content of the issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

Creating a subtask differs from creating an issue as follows:

 *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types).
 *  `parent` must contain the ID or key of the parent issue.

In a next-gen project any issue may be made a child providing that the parent and child are members of the same project.

**[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or subtask is created.
