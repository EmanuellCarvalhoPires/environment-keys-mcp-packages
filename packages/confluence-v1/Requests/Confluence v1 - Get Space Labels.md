---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/space/{spaceKey}/label"
category: "Experimental"
writes_data: false
tool_note: "[[confluence_v1_get_space_labels]]"
---
# Confluence v1 - Get Space Labels

**Get Space Labels** — `GET /wiki/rest/api/space/{spaceKey}/label`

- Run by the tool [[confluence_v1_get_space_labels]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/label?prefix={{param:prefix}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to get labels for.
- `prefix` (query, string, optional) — Filters the results to labels with the specified prefix. If this parameter is not specified, then labels with any prefix will be returned.
- `start` (query, string, optional) — The starting index of the returned labels.
- `limit` (query, string, optional) — The maximum number of labels to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns a list of labels associated with a space. Can provide a prefix as well as other filters to
select different types of labels.
