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
tool: jira_delete_project_asynchronously
title: "Jira v3 - Delete project asynchronously"
kind: request
request: "[[Jira v3 - Delete project asynchronously]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project/{projectIdOrKey}/delete · Delete project asynchronously. Deletes a project asynchronously. This operation is: transactional, that is, if part of the delete fails the project is not deleted. asynchronous. Follow the location link in the response to determine the status of the task and use Get task to obtain subsequent updates. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: true
expose: false
---
# jira_delete_project_asynchronously

`POST /rest/api/3/project/{projectIdOrKey}/delete` — Delete project asynchronously

- Request: [[Jira v3 - Delete project asynchronously]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
