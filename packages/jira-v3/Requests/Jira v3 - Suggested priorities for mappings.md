---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/priorityscheme/mappings"
category: "Priority schemes"
writes_data: true
tool_note: "[[jira_suggested_priorities_for_mappings]]"
---
# Jira v3 - Suggested priorities for mappings

**Suggested priorities for mappings** — `POST /rest/api/3/priorityscheme/mappings`

- Run by the tool [[jira_suggested_priorities_for_mappings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/priorityscheme/mappings
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "maxResults": 50,
  "priorities": {
    "add": [
      10001,
      10002
    ],
    "remove": [
      10003
    ]
  },
  "projects": {
    "add": [
      10021
    ]
  },
  "schemeId": 10005,
  "startAt": 0
}
```

## Original description

Returns a [paginated](#pagination) list of priorities that would require mapping, given a change in priorities or projects associated with a priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
