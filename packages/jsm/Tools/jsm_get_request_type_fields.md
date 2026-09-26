---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_request_type_fields
title: "JSM - Get request type fields"
kind: request
request: "[[JSM - Get request type fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/field · Get request type fields. This method returns the fields for a service desk's customer request type. Also, the following information about the user's permissions for the request type is returned: canRaiseOnBehalfOf returns true if the user has permission to raise customer requests on behalf of other custo… Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk containing the request types whose fields are to be returned. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request types whose fields are to be returned."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts hiddenFields that returns hidden fields associated with the request type."
writes: false
expose: false
---
# jsm_get_request_type_fields

`GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/field` — Get request type fields

- Request: [[JSM - Get request type fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
