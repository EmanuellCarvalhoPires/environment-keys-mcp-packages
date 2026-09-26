---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_page
title: "Confluence v2 - Delete page"
kind: request
request: "[[Confluence v2 - Delete page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /pages/{id} · Delete page. Delete a page by id. By default this will delete pages that are non-drafts. To delete a page that is a draft, the endpoint must be called on a draft with the following param draft=true. Discarded drafts are not sent to the trash and are permanently deleted. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to be deleted."
  "purge":
    type: string
    required: false
    description: "If attempting to purge the page."
  "draft":
    type: string
    required: false
    description: "If attempting to delete a page that is a draft."
writes: true
expose: false
---
# confluence_delete_page

`DELETE /pages/{id}` — Delete page

- Request: [[Confluence v2 - Delete page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
