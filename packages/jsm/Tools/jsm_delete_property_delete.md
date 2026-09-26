---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_delete_property_delete
title: "JSM - Delete property (DELETE)"
kind: request
request: "[[JSM - Delete property (DELETE)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey} · Delete property. Removes a property from a request type. Properties for a Request Type in next-gen are stored as Issue Type properties and therefore can also be deleted by calling the Jira Cloud Platform Delete issue type property endpoint. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk which contains the request type. This can alternatively be a project identifier."
  "requestTypeId":
    type: string
    required: true
    description: "The ID of the request type for which the property will be removed."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property to remove."
writes: true
expose: false
---
# jsm_delete_property_delete

`DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Delete property

- Request: [[JSM - Delete property (DELETE)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
