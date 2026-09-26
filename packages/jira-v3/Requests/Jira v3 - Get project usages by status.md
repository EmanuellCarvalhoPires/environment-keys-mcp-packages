---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuses/{statusId}/projectUsages"
category: "Status"
writes_data: false
tool_note: "[[jira_get_project_usages_by_status]]"
---
# Jira v3 - Get project usages by status

**Get project usages by status** — `GET /rest/api/3/statuses/{statusId}/projectUsages`

- Run by the tool [[jira_get_project_usages_by_status]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuses/{{param:statusId}}/projectUsages?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `statusId` (path, string, required) — The statusId to fetch project usages for
- `nextPageToken` (query, string, optional) — The cursor for pagination
- `maxResults` (query, string, optional) — The maximum number of results to return. Must be an integer between 1 and 200.

## Original description

Returns a page of projects using a given status.
