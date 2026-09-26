---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/template/page"
category: "Template"
writes_data: false
tool_note: "[[confluence_v1_get_content_templates]]"
---
# Confluence v1 - Get content templates

**Get content templates** — `GET /wiki/rest/api/template/page`

- Run by the tool [[confluence_v1_get_content_templates]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/template/page?spaceKey={{param:spaceKey}}&start={{param:start}}&limit={{param:limit}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (query, string, optional) — The key of the space to be queried for templates. If the spaceKey is not specified, global templates will be returned.
- `start` (query, string, optional) — The starting index of the returned templates.
- `limit` (query, string, optional) — The maximum number of templates to return per page. Note, this may be restricted by fixed system limits.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the template to expand. - body or body.storage returns the content of the template in storage format.

## Original description

Returns all content templates. Use this method to retrieve all global
content templates or all content templates in a space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space to view space templates and permission to
access the Confluence site ('Can use' global permission) to view global templates.
