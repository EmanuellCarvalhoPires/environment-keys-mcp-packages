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
path: "/wiki/rest/api/template/blueprint"
category: "Template"
writes_data: false
tool_note: "[[confluence_v1_get_blueprint_templates]]"
---
# Confluence v1 - Get blueprint templates

**Get blueprint templates** — `GET /wiki/rest/api/template/blueprint`

- Run by the tool [[confluence_v1_get_blueprint_templates]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/template/blueprint?spaceKey={{param:spaceKey}}&start={{param:start}}&limit={{param:limit}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (query, string, optional) — The key of the space to be queried for templates. If the spaceKey is not specified, global blueprint templates will be returned.
- `start` (query, string, optional) — The starting index of the returned templates.
- `limit` (query, string, optional) — The maximum number of templates to return per page. Note, this may be restricted by fixed system limits.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the template to expand. - body or body.storage returns the content of the template in storage format.

## Original description

Returns all templates provided by blueprints. Use this method to retrieve
all global blueprint templates or all blueprint templates in a space.

Note, all global blueprints are inherited by each space. Space blueprints
can be customised without affecting the global blueprints.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space to view blueprints for the space and permission
to access the Confluence site ('Can use' global permission) to view global blueprints.
