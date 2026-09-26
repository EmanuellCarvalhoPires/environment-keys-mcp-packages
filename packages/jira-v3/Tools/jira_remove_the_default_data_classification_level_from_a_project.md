---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_the_default_data_classification_level_from_a_project
title: "Jira v3 - Remove the default data classification level from a project"
kind: request
request: "[[Jira v3 - Remove the default data classification level from a project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default · Remove the default data classification level from a project. Remove the default data classification level for a project. Permissions required: Administer projects project permission for the project. Administer jira global permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case-sensitive)."
writes: true
expose: false
---
# jira_remove_the_default_data_classification_level_from_a_project

`DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Remove the default data classification level from a project

- Request: [[Jira v3 - Remove the default data classification level from a project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
