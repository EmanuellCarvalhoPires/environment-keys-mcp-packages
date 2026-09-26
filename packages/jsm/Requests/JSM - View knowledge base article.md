---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/other-operations
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/knowledgebase/article/view/{pageId}"
category: "Other operations"
writes_data: false
tool_note: "[[jsm_view_knowledge_base_article]]"
---
# JSM - View knowledge base article

**View knowledge base article** — `GET /rest/servicedeskapi/knowledgebase/article/view/{pageId}`

- Run by the tool [[jsm_view_knowledge_base_article]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/knowledgebase/article/view/{{param:pageId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Value of pageId in the path.

