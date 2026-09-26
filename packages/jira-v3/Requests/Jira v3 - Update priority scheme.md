---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/priorityscheme/{schemeId}"
category: "Priority schemes"
writes_data: true
tool_note: "[[jira_update_priority_scheme]]"
---
# Jira v3 - Update priority scheme

**Update priority scheme** — `PUT /rest/api/3/priorityscheme/{schemeId}`

- Run by the tool [[jira_update_priority_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/priorityscheme/{{param:schemeId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the priority scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultPriorityId": 10001,
  "description": "My priority scheme description",
  "mappings": {
    "in": {
      "10003": 10002,
      "10004": 10001
    },
    "out": {
      "10001": 10005,
      "10002": 10006
    }
  },
  "name": "My new priority scheme",
  "priorities": {
    "add": {
      "ids": [
        10001,
        10002
      ]
    },
    "remove": {
      "ids": [
        10003,
        10004
      ]
    }
  },
  "projects": {
    "add": {
      "ids": [
        10101,
        10102
      ]
    },
    "remove": {
      "ids": [
        10103,
        10104
      ]
    }
  }
}
```

## Original description

Updates a priority scheme. This includes its details, the lists of priorities and projects in it

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
