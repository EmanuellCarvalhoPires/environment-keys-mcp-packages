---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/assets
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_assets_workspaces
title: "JSM - Get assets workspaces"
kind: request
request: "[[JSM - Get assets workspaces]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/assets/workspace · Get assets workspaces. Returns a list of Assets workspace IDs. Include a workspace ID in the path to access the Assets REST APIs. Permissions required: Any Writes data: no."
params:
  "start":
    type: string
    required: false
    description: "The starting index of the returned workspace IDs. Base index: 0 See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of workspace IDs to return per page. Default: 50 See the Pagination section for more details."
writes: false
expose: true
---
# jsm_get_assets_workspaces

`GET /rest/servicedeskapi/assets/workspace` — Get assets workspaces

- Request: [[JSM - Get assets workspaces]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
