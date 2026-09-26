---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_deletes_a_custom_project_template
title: "Jira v3 - Deletes a custom project template"
kind: request
request: "[[Jira v3 - Deletes a custom project template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project-template/remove-template · Deletes a custom project template. Remove custom template This API endpoint allows you to remove a specified customised template Note: Custom Templates are only supported for Jira Enterprise edition. Writes data: yes."
params:
  "templateKey":
    type: string
    required: true
    description: "The \\{@link String\\} containing the key of the custom template to remove"
writes: true
expose: false
---
# jira_deletes_a_custom_project_template

`DELETE /rest/api/3/project-template/remove-template` — Deletes a custom project template

- Request: [[Jira v3 - Deletes a custom project template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
