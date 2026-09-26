---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/space/{spaceKey}/label"
category: "Experimental"
writes_data: true
tool_note: "[[confluence_v1_remove_label_from_a_space]]"
---
# Confluence v1 - Remove label from a space

**Remove label from a space** — `DELETE /wiki/rest/api/space/{spaceKey}/label`

- Run by the tool [[confluence_v1_remove_label_from_a_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/label?name={{param:name}}&prefix={{param:prefix}}
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to remove a labels from.
- `name` (query, string, required) — The name of the label to remove
- `prefix` (query, string, optional) — The prefix of the label to remove. If not provided defaults to global.

