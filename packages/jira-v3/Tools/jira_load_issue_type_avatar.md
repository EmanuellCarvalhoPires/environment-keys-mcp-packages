---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_load_issue_type_avatar
title: "Jira v3 - Load issue type avatar"
kind: request
request: "[[Jira v3 - Load issue type avatar]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issuetype/{id}/avatar2 · Load issue type avatar. Loads an avatar for the issue type. Specify the avatar's local file location in the body of the request. Also, include the following headers: X-Atlassian-Token: no-check To prevent XSRF protection blocking the request, for more information see Special Headers. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue type."
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
# jira_load_issue_type_avatar

`POST /rest/api/3/issuetype/{id}/avatar2` — Load issue type avatar

- Request: [[Jira v3 - Load issue type avatar]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
