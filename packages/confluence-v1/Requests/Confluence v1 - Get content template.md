---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/template/{contentTemplateId}"
category: "Template"
writes_data: false
tool_note: "[[confluence_v1_get_content_template]]"
---
# Confluence v1 - Get content template

**Get content template** — `GET /wiki/rest/api/template/{contentTemplateId}`

- Run by the tool [[confluence_v1_get_content_template]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/template/{{param:contentTemplateId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `contentTemplateId` (path, string, required) — The ID of the content template to be returned.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the template to expand. - body or body.storage returns the content of the template in storage format.

## Original description

Returns a content template. This includes information about template,
like the name, the space or blueprint that the template is in, the body
of the template, and more.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space to view space templates and permission to
access the Confluence site ('Can use' global permission) to view global templates.
