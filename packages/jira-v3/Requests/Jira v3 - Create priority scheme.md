---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/priorityscheme"
category: "Priority schemes"
writes_data: true
tool_note: "[[jira_create_priority_scheme]]"
---
# Jira v3 - Create priority scheme

**Create priority scheme** — `POST /rest/api/3/priorityscheme`

- Run by the tool [[jira_create_priority_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/priorityscheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultPriorityId": 10001,
  "description": "My priority scheme description",
  "mappings": {
    "in": {
      "10002": 10000,
      "10005": 10001,
      "10006": 10001,
      "10008": 10003
    },
    "out": {}
  },
  "name": "My new priority scheme",
  "priorityIds": [
    10000,
    10001,
    10003
  ],
  "projectIds": [
    10005,
    10006,
    10007
  ]
}
```

## Original description

Creates a new priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
