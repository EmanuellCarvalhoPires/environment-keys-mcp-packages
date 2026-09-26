---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/knowledgebase
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_articles
title: "JSM - Get articles"
kind: request
request: "[[JSM - Get articles]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/knowledgebase/article · Get articles. Returns articles which match the given query string across all service desks. Permissions required: Permission to access the customer portal. Writes data: no."
params:
  "query":
    type: string
    required: true
    description: "The string used to filter the articles (required)."
  "highlight":
    type: string
    required: true
    description: "If set to true matching query term in the title and excerpt will be highlighted using the @@@hl@@@term@@@endhl@@@ syntax. Default: false."
  "start":
    type: string
    required: false
    description: "(Deprecated) The starting index of the returned objects. Base index: 0."
  "limit":
    type: string
    required: false
    description: "The maximum number of items to return per page. Default: 50."
  "cursor":
    type: string
    required: false
    description: "Pointer to a set of search results, returned as part of the next or prev URL from the previous search call."
  "prev":
    type: string
    required: false
    description: "Should navigate to the previous page. Defaulted to false. Set to true as part of prev URL from the previous search call."
writes: false
expose: false
---
# jsm_get_articles

`GET /rest/servicedeskapi/knowledgebase/article` — Get articles

- Request: [[JSM - Get articles]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
