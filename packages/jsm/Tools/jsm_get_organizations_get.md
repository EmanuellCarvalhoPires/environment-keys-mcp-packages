---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_organizations_get
title: "JSM - Get organizations (GET)"
kind: request
request: "[[JSM - Get organizations (GET)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization · Get organizations. This method returns a list of all organizations associated with a service desk. Permissions required: Service desk's agent. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk from which the organization list will be returned. This can alternatively be a project identifier."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50. See the Pagination section for more details."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
writes: false
expose: false
---
# jsm_get_organizations_get

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Get organizations

- Request: [[JSM - Get organizations (GET)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
