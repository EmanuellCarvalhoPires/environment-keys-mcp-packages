---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_default_actors_from_project_role
title: "Jira v3 - Delete default actors from project role"
kind: request
request: "[[Jira v3 - Delete default actors from project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/role/{id}/actors · Delete default actors from project role. Deletes the default actors from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request. Changing a project role's default actors does not affect project role members for projects already created. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
  "user":
    type: string
    required: false
    description: "The user account ID of the user to remove as a default actor."
  "groupId":
    type: string
    required: false
    description: "The group ID of the group to be removed as a default actor. This parameter cannot be used with the group parameter."
  "group":
    type: string
    required: false
    description: "The group name of the group to be removed as a default actor.This parameter cannot be used with the groupId parameter. As a group's name can change, use of groupId is recommended."
writes: true
expose: false
---
# jira_delete_default_actors_from_project_role

`DELETE /rest/api/3/role/{id}/actors` — Delete default actors from project role

- Request: [[Jira v3 - Delete default actors from project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
