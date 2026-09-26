---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_answer_approval
title: "JSM - Answer approval"
kind: request
request: "[[JSM - Answer approval]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId} · Answer approval. This method enables a user to Approve or Decline an approval on a customer request. The approval is assumed to be owned by the user making the call. Permissions required: User is assigned to the approval request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request to be updated."
  "approvalId":
    type: string
    required: true
    description: "The ID of the approval to be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_answer_approval

`POST /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}` — Answer approval

- Request: [[JSM - Answer approval]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
