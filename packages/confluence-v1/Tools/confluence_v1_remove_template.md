---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_template
title: "Confluence v1 - Remove template"
kind: request
request: "[[Confluence v1 - Remove template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/template/{contentTemplateId} · Remove template. Deletes a template. This results in different actions depending on the type of template: - If the template is a content template, it is deleted. Writes data: yes."
params:
  "contentTemplateId":
    type: string
    required: true
    description: "The ID of the template to be deleted."
writes: true
expose: false
---
# confluence_v1_remove_template

`DELETE /wiki/rest/api/template/{contentTemplateId}` — Remove template

- Request: [[Confluence v1 - Remove template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
