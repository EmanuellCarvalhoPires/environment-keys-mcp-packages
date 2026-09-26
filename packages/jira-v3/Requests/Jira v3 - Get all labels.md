---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/labels
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/label"
category: "Labels"
writes_data: false
tool_note: "[[jira_get_all_labels]]"
---
# Jira v3 - Get all labels

**Get all labels** — `GET /rest/api/3/label`

- Run by the tool [[jira_get_all_labels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/label?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of labels.
