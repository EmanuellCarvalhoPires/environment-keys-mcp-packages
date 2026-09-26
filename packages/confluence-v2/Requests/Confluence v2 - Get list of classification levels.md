---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/classification-levels"
category: "Classification Level"
writes_data: false
tool_note: "[[confluence_get_list_of_classification_levels]]"
---
# Confluence v2 - Get list of classification levels

**Get list of classification levels** — `GET /classification-levels`

- Run by the tool [[confluence_get_list_of_classification_levels]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/classification-levels
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a list of [classification levels](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level) 
available.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Permission to access the Confluence site ('Can use' global permission).
