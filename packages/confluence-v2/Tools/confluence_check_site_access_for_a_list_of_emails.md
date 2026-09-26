---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/search
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_check_site_access_for_a_list_of_emails
title: "Confluence v2 - Check site access for a list of emails"
kind: request
request: "[[Confluence v2 - Check site access for a list of emails]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /user/access/check-access-by-email · Check site access for a list of emails. Returns the list of emails from the input list that do not have access to site. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# confluence_check_site_access_for_a_list_of_emails

`POST /user/access/check-access-by-email` — Check site access for a list of emails

- Request: [[Confluence v2 - Check site access for a list of emails]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
