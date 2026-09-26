---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-versions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_content_version
title: "Confluence v1 - Delete content version"
kind: request
request: "[[Confluence v1 - Delete content version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/version/{versionNumber} · Delete content version. Delete a historical version. This does not delete the changes made to the content in that version, rather the changes for the deleted version are rolled up into the next version. Note, you cannot delete the current version. Permissions required: Permission to update the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the version will be deleted from."
  "versionNumber":
    type: string
    required: true
    description: "The number of the version to be deleted. The version number starts from 1 up to current version."
writes: true
expose: false
---
# confluence_v1_delete_content_version

`DELETE /wiki/rest/api/content/{id}/version/{versionNumber}` — Delete content version

- Request: [[Confluence v1 - Delete content version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
