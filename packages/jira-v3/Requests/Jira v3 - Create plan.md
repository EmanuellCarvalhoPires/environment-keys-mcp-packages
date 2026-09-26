---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/plans/plan"
category: "Plans"
writes_data: true
tool_note: "[[jira_create_plan]]"
---
# Jira v3 - Create plan

**Create plan** — `POST /rest/api/3/plans/plan`

- Run by the tool [[jira_create_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/plans/plan?useGroupId={{param:useGroupId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `useGroupId` (query, string, optional) — Whether to accept group IDs instead of group names. Group names are deprecated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "crossProjectReleases": [
    {
      "name": "AB and BC merge",
      "releaseIds": [
        29,
        39
      ]
    }
  ],
  "customFields": [
    {
      "customFieldId": 2335,
      "filter": true
    }
  ],
  "exclusionRules": {
    "issueIds": [
      2,
      3
    ],
    "issueTypeIds": [
      32,
      33
    ],
    "numberOfDaysToShowCompletedIssues": 50,
    "releaseIds": [
      42,
      43
    ],
    "workStatusCategoryIds": [
      22,
      23
    ],
    "workStatusIds": [
      12,
      13
    ]
  },
  "issueSources": [
    {
      "type": "Project",
      "value": 12
    },
    {
      "type": "Board",
      "value": 462
    }
  ],
  "leadAccountId": "abc-12-rbji",
  "name": "ABC Quaterly plan",
  "permissions": [
    {
      "holder": {
        "type": "AccountId",
        "value": "234-tgj-343"
      },
      "type": "Edit"
    }
  ],
  "scheduling": {
    "dependencies": "Sequential",
    "endDate": {
      "type": "DueDate"
    },
    "estimation": "Days",
    "inferredDates": "ReleaseDates",
    "startDate": {
      "type": "TargetStartDate"
    }
  }
}
```

## Original description

Creates a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
