---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_project
title: "Jira v3 - Delete project"
kind: request
request: "[[Jira v3 - Delete project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project/{projectIdOrKey} · Delete project. Deletes a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "enableUndo":
    type: string
    required: false
    description: "Whether this project is placed in the Jira recycle bin where it will be available for restoration."
writes: true
expose: false
---
# jira_delete_project

`DELETE /rest/api/3/project/{projectIdOrKey}` — Delete project

- Request: [[Jira v3 - Delete project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
