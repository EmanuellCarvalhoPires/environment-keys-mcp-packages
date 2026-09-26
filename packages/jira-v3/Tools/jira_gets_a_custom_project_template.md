---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_gets_a_custom_project_template
title: "Jira v3 - Gets a custom project template"
kind: request
request: "[[Jira v3 - Gets a custom project template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project-template/live-template · Gets a custom project template. Get custom template This API endpoint allows you to get a live custom project template details by either templateKey or projectId Note: Custom Templates are only supported for Jira Enterprise edition. Writes data: no."
params:
  "projectId":
    type: string
    required: false
    description: "optional - The \\{@link String\\} containing the project key linked to the custom template to retrieve"
  "templateKey":
    type: string
    required: false
    description: "optional - The \\{@link String\\} containing the key of the custom template to retrieve"
writes: false
expose: false
---
# jira_gets_a_custom_project_template

`GET /rest/api/3/project-template/live-template` — Gets a custom project template

- Request: [[Jira v3 - Gets a custom project template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
