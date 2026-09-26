---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_archive_project
title: "Jira v3 - Archive project"
kind: request
request: "[[Jira v3 - Archive project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project/{projectIdOrKey}/archive · Archive project. Archives a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: true
expose: false
---
# jira_archive_project

`POST /rest/api/3/project/{projectIdOrKey}/archive` — Archive project

- Request: [[Jira v3 - Archive project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
