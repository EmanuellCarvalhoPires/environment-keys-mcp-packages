---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_resolution
title: "Jira v3 - Delete resolution"
kind: request
request: "[[Jira v3 - Delete resolution]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/resolution/{id} · Delete resolution. Deletes an issue resolution. This operation is asynchronous. Follow the location link in the response to determine the status of the task and use Get task to obtain subsequent updates. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue resolution."
  "replaceWith":
    type: string
    required: true
    description: "The ID of the issue resolution that will replace the currently selected resolution."
writes: true
expose: false
---
# jira_delete_resolution

`DELETE /rest/api/3/resolution/{id}` — Delete resolution

- Request: [[Jira v3 - Delete resolution]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
