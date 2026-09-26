---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_edit_a_custom_project_template
title: "Jira v3 - Edit a custom project template"
kind: request
request: "[[Jira v3 - Edit a custom project template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project-template/edit-template · Edit a custom project template. Edit custom template This API endpoint allows you to edit an existing customised template. Note: Custom Templates are only supported for Jira Enterprise edition. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_edit_a_custom_project_template

`PUT /rest/api/3/project-template/edit-template` — Edit a custom project template

- Request: [[Jira v3 - Edit a custom project template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
