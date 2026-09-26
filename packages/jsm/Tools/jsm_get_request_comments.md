---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_comments
title: "JSM - Get request comments"
kind: request
request: "[[JSM - Get request comments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/request/{issueIdOrKey}/comment · Get request comments. This method returns all comments on a customer request. No permissions error is provided if, for example, the user doesn't have access to the service desk or request, the method simply returns an empty response. Permissions required: Permission to view the customer request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the customer request whose comments will be retrieved."
  "public":
    type: string
    required: false
    description: "Specifies whether to return public comments or not. Default: true."
  "internal":
    type: string
    required: false
    description: "Specifies whether to return internal comments or not. Default: true."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the comment to expand: attachment returns the attachment details, if any, for each comment."
  "start":
    type: string
    required: false
    description: "The starting index of the returned comments. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of comments to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: true
---
# jsm_get_request_comments

`GET /rest/servicedeskapi/request/{issueIdOrKey}/comment` — Get request comments

- Request: [[JSM - Get request comments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
