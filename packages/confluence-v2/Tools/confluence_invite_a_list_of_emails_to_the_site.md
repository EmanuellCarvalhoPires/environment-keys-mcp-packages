---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_invite_a_list_of_emails_to_the_site
title: "Confluence v2 - Invite a list of emails to the site"
kind: request
request: "[[Confluence v2 - Invite a list of emails to the site]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /user/access/invite-by-email · Invite a list of emails to the site. Invite a list of emails to the site. Ignores all invalid emails and no action is taken for the emails that already have access to the site. NOTE: This API is asynchronous and may take some time to complete. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_invite_a_list_of_emails_to_the_site

`POST /user/access/invite-by-email` — Invite a list of emails to the site

- Request: [[Confluence v2 - Invite a list of emails to the site]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
