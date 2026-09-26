---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-versions
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_restore_content_version
title: "Confluence v1 - Restore content version"
kind: request
request: "[[Confluence v1 - Restore content version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/version · Restore content version. Restores a historical version to be the latest version. That is, a new version is created with the content of the historical version. Permissions required: Permission to update the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content for which the history will be restored."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. By default, the content object is expanded. - collaborators returns the users that collaborated on the version."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_restore_content_version

`POST /wiki/rest/api/content/{id}/version` — Restore content version

- Request: [[Confluence v1 - Restore content version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
