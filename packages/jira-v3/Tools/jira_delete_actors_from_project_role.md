---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_actors_from_project_role
title: "Jira v3 - Delete actors from project role"
kind: request
request: "[[Jira v3 - Delete actors from project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project/{projectIdOrKey}/role/{id} · Delete actors from project role. Deletes actors from a project role for the project. To remove default actors from the project role, use Delete default actors from project role. This operation can be accessed anonymously. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
  "user":
    type: string
    required: false
    description: "The user account ID of the user to remove from the project role."
  "group":
    type: string
    required: false
    description: "The name of the group to remove from the project role. This parameter cannot be used with the groupId parameter. As a group's name can change, use of groupId is recommended."
  "groupId":
    type: string
    required: false
    description: "The ID of the group to remove from the project role. This parameter cannot be used with the group parameter."
writes: true
expose: false
---
# jira_delete_actors_from_project_role

`DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}` — Delete actors from project role

- Request: [[Jira v3 - Delete actors from project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
