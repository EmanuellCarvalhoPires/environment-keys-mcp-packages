---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_the_default_data_classification_level_of_a_project
title: "Jira v3 - Get the default data classification level of a project"
kind: request
request: "[[Jira v3 - Get the default data classification level of a project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/classification-level/default · Get the default data classification level of a project. Returns the default data classification for a project. Permissions required: Browse Projects project permission for the project. Administer projects project permission for the project. Administer jira global permission. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case-sensitive)."
writes: false
expose: false
---
# jira_get_the_default_data_classification_level_of_a_project

`GET /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Get the default data classification level of a project

- Request: [[Jira v3 - Get the default data classification level of a project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
