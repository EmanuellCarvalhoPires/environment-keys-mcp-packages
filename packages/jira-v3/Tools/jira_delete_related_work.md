---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_related_work
title: "Jira v3 - Delete related work"
kind: request
request: "[[Jira v3 - Delete related work]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId} · Delete related work. Deletes the given related work for the given version. This operation can be accessed anonymously. Permissions required: Resolve issues: and Edit issues Managing project permissions for the project that contains the version. Writes data: yes."
params:
  "versionId":
    type: string
    required: true
    description: "The ID of the version that the target related work belongs to."
  "relatedWorkId":
    type: string
    required: true
    description: "The ID of the related work to delete."
writes: true
expose: false
---
# jira_delete_related_work

`DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}` — Delete related work

- Request: [[Jira v3 - Delete related work]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
