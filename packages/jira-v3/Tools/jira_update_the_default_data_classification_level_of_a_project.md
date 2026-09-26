---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_the_default_data_classification_level_of_a_project
title: "Jira v3 - Update the default data classification level of a project"
kind: request
request: "[[Jira v3 - Update the default data classification level of a project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default · Update the default data classification level of a project. Updates the default data classification level for a project. Permissions required: Administer projects project permission for the project. Administer jira global permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case-sensitive)."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_the_default_data_classification_level_of_a_project

`PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Update the default data classification level of a project

- Request: [[Jira v3 - Update the default data classification level of a project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
