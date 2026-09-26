---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_invite_customer
title: "JSM - Invite customer"
kind: request
request: "[[JSM - Invite customer]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/invite · Invite customer. This method invites a customer to a specified service desk by sending them an email invitation, creating a new customer account if one does not already exist. The display name does not need to be unique. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk to which the newly created customer should be added."
  "strictConflictStatusCode":
    type: string
    required: false
    description: "Optional boolean flag to return 409 Conflict status code when a customer with the same email already exists."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_invite_customer

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/invite` — Invite customer

- Request: [[JSM - Invite customer]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
