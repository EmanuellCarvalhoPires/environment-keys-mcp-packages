---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/analytics
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/analytics/content/{contentId}/views"
category: "Analytics"
writes_data: false
tool_note: "[[confluence_v1_get_views]]"
---
# Confluence v1 - Get views

**Get views** — `GET /wiki/rest/api/analytics/content/{contentId}/views`

- Run by the tool [[confluence_v1_get_views]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/analytics/content/{{param:contentId}}/views?fromDate={{param:fromDate}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `contentId` (path, string, required) — The ID of the content to get the views for.
- `fromDate` (query, string, optional) — The number of views for the content since the date.

## Original description

Get the total number of views a piece of content has.
