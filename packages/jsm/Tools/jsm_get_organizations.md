---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_organizations
title: "JSM - Get organizations"
kind: request
request: "[[JSM - Get organizations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/organization · Get organizations. This method returns a list of organizations in the Jira Service Management instance. Use this method when you want to present a list of organizations or want to locate an organization by name. Permissions required: Any. Writes data: no."
params:
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of organizations to return per page. Default: 50. See the Pagination section for more details."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
writes: false
expose: false
---
# jsm_get_organizations

`GET /rest/servicedeskapi/organization` — Get organizations

- Request: [[JSM - Get organizations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
