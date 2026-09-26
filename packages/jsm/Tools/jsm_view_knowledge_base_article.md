---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/other-operations
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_view_knowledge_base_article
title: "JSM - View knowledge base article"
kind: request
request: "[[JSM - View knowledge base article]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/knowledgebase/article/view/{pageId} · View knowledge base article. Writes data: no."
params:
  "pageId":
    type: string
    required: true
    description: "Value of pageId in the path."
writes: false
expose: false
---
# jsm_view_knowledge_base_article

`GET /rest/servicedeskapi/knowledgebase/article/view/{pageId}` — View knowledge base article

- Request: [[JSM - View knowledge base article]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
