---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_contents_metadata_for_an_expanded_attachment
title: "Jira v3 - Get contents metadata for an expanded attachment"
kind: request
request: "[[Jira v3 - Get contents metadata for an expanded attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/attachment/{id}/expand/raw · Get contents metadata for an expanded attachment. Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment."
writes: false
expose: false
---
# jira_get_contents_metadata_for_an_expanded_attachment

`GET /rest/api/3/attachment/{id}/expand/raw` — Get contents metadata for an expanded attachment

- Request: [[Jira v3 - Get contents metadata for an expanded attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
