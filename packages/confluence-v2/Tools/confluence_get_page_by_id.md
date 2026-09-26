---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_page_by_id
title: "Confluence v2 - Get page by id"
kind: request
request: "[[Confluence v2 - Get page by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id} · Get page by id. Returns a specific page. Permissions required: Permission to view the page and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to be returned. If you don't know the page ID, use Get pages and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "get_draft":
    type: string
    required: false
    description: "Retrieve the draft version of this page."
  "status":
    type: string
    required: false
    description: "Filter the page being retrieved by its status."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "include_labels":
    type: string
    required: false
    description: "Includes labels associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this page in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_likes":
    type: string
    required: false
    description: "Includes likes associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_versions":
    type: string
    required: false
    description: "Includes versions associated with this page in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_version":
    type: string
    required: false
    description: "Includes the current version associated with this page in the response. By default this is included and can be omitted by setting the value to false."
  "include_favorited_by_current_user_status":
    type: string
    required: false
    description: "Includes whether this page has been favorited by the current user."
  "include_webresources":
    type: string
    required: false
    description: "Includes web resources that can be used to render page content on a client."
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the page."
  "include_direct_children":
    type: string
    required: false
    description: "Includes direct children of the page, as defined in the ChildrenResponse object."
writes: false
expose: true
---
# confluence_get_page_by_id

`GET /pages/{id}` — Get page by id

- Request: [[Confluence v2 - Get page by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
