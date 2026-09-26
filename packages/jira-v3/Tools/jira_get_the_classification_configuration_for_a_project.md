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
tool: jira_get_the_classification_configuration_for_a_project
title: "Jira v3 - Get the classification configuration for a project"
kind: request
request: "[[Jira v3 - Get the classification configuration for a project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/classification-config · Get the classification configuration for a project. Returns the consolidated classification configuration for a project's admin settings page. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case-sensitive)."
writes: false
expose: false
---
# jira_get_the_classification_configuration_for_a_project

`GET /rest/api/3/project/{projectIdOrKey}/classification-config` — Get the classification configuration for a project

- Request: [[Jira v3 - Get the classification configuration for a project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
