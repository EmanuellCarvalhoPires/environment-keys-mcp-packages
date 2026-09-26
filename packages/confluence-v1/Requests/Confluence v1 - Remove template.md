---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/template/{contentTemplateId}"
category: "Template"
writes_data: true
tool_note: "[[confluence_v1_remove_template]]"
---
# Confluence v1 - Remove template

**Remove template** — `DELETE /wiki/rest/api/template/{contentTemplateId}`

- Run by the tool [[confluence_v1_remove_template]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/template/{{param:contentTemplateId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `contentTemplateId` (path, string, required) — The ID of the template to be deleted.

## Original description

Deletes a template. This results in different actions depending on the
type of template:

- If the template is a content template, it is deleted.
- If the template is a modified space-level blueprint template, it reverts
to the template inherited from the global-level blueprint template.
- If the template is a modified global-level blueprint template, it reverts
to the default global-level blueprint template.

 Note, unmodified blueprint templates cannot be deleted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Admin' permission for the space to delete a space template or 'Confluence Administrator'
        global permission to delete a global template.
