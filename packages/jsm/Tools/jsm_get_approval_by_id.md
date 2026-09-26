---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_approval_by_id
title: "JSM - Get approval by id"
kind: request
request: "[[JSM - Get approval by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId} · Get approval by id. This method returns an approval. Use this method to determine the status of an approval and the list of approvers. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request the approval is on."
  "approvalId":
    type: string
    required: true
    description: "The ID of the approval to be returned."
writes: false
expose: false
---
# jsm_get_approval_by_id

`GET /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}` — Get approval by id

- Request: [[JSM - Get approval by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
