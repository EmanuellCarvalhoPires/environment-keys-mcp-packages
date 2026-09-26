---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_restore_deleted_or_archived_project
title: "Jira v3 - Restore deleted or archived project"
kind: request
request: "[[Jira v3 - Restore deleted or archived project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project/{projectIdOrKey}/restore · Restore deleted or archived project. Restores a project that has been archived or placed in the Jira recycle bin. Permissions required: Administer Jira global permissionfor Company managed projects. Administer Jira global permission or Administer projects project permission for the project for Team managed projects. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: true
expose: false
---
# jira_restore_deleted_or_archived_project

`POST /rest/api/3/project/{projectIdOrKey}/restore` — Restore deleted or archived project

- Request: [[Jira v3 - Restore deleted or archived project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
