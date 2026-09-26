---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-settings
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_space_settings
title: "Confluence v1 - Update space settings"
kind: request
request: "[[Confluence v1 - Update space settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/space/{spaceKey}/settings · Update space settings. Updates the settings for a space. Permissions required: manage/space permission for the space. Note: To find the display name for each permission ID, call the Get available space permissions API. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space whose settings will be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_space_settings

`PUT /wiki/rest/api/space/{spaceKey}/settings` — Update space settings

- Request: [[Confluence v1 - Update space settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
