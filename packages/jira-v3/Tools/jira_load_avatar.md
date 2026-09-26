---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_load_avatar
title: "Jira v3 - Load avatar"
kind: request
request: "[[Jira v3 - Load avatar]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/universal_avatar/type/{type}/owner/{entityId} · Load avatar. Loads a custom avatar for a project, issue type or priority. Specify the avatar's local file location in the body of the request. Writes data: yes."
params:
  "type":
    type: string
    required: true
    description: "The avatar type."
  "entityId":
    type: string
    required: true
    description: "The ID of the item the avatar is associated with."
  "x":
    type: string
    required: false
    description: "The X coordinate of the top-left corner of the crop region."
  "y":
    type: string
    required: false
    description: "The Y coordinate of the top-left corner of the crop region."
  "size":
    type: string
    required: true
    description: "The length of each side of the crop region."
  "body":
    type: string
    required: true
    description: "Request body (*/*)."
writes: true
expose: false
---
# jira_load_avatar

`POST /rest/api/3/universal_avatar/type/{type}/owner/{entityId}` — Load avatar

- Request: [[Jira v3 - Load avatar]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
