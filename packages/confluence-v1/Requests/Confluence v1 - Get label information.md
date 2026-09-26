---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/label-info
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/label"
category: "Label info"
writes_data: false
tool_note: "[[confluence_v1_get_label_information]]"
---
# Confluence v1 - Get label information

**Get label information** — `GET /wiki/rest/api/label`

- Run by the tool [[confluence_v1_get_label_information]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/label?name={{param:name}}&type={{param:type}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (query, string, required) — Name of the label to query.
- `type` (query, string, optional) — The type of contents that are to be returned.
- `start` (query, string, optional) — The starting offset for the results.
- `limit` (query, string, optional) — The number of results to be returned.

## Original description

Returns label information and a list of contents associated with the label.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission). Only contents
that the user is permitted to view is returned.
