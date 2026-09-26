---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/data-policies
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_data_policy_metadata_for_the_workspace
title: "Confluence v2 - Get data policy metadata for the workspace"
kind: request
request: "[[Confluence v2 - Get data policy metadata for the workspace]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /data-policies/metadata · Get data policy metadata for the workspace. Returns data policy metadata for the workspace. Permissions required: Only apps can make this request. Permission to access the Confluence site ('Can use' global permission). Writes data: no."
writes: false
expose: false
---
# confluence_get_data_policy_metadata_for_the_workspace

`GET /data-policies/metadata` — Get data policy metadata for the workspace

- Request: [[Confluence v2 - Get data policy metadata for the workspace]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
