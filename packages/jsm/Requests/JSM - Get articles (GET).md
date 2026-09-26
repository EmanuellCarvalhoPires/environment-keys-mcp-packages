---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/knowledgebase/article"
category: "Servicedesk"
writes_data: false
tool_note: "[[jsm_get_articles_get]]"
---
# JSM - Get articles (GET)

**Get articles** — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/knowledgebase/article`

- Run by the tool [[jsm_get_articles_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/knowledgebase/article?query={{param:query}}&highlight={{param:highlight}}&start={{param:start}}&limit={{param:limit}}&cursor={{param:cursor}}&prev={{param:prev}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceDeskId` (path, string, required) — Value of serviceDeskId in the path.
- `query` (query, string, required) — The string used to filter the articles (required).
- `highlight` (query, string, optional) — If set to true matching query term in the title and excerpt will be highlighted using the @@@hl@@@term@@@endhl@@@ syntax. Default: false.
- `start` (query, string, optional) — (Deprecated) The starting index of the returned objects. Base index: 0.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50. See the section for more details.
- `cursor` (query, string, optional) — Pointer to a set of search results, returned as part of the next or prev URL from the previous search call.
- `prev` (query, string, optional) — Should navigate to the previous page. Defaulted to false. Set to true as part of prev URL from the previous search call.

## Original description

Returns articles which match the given query and belong to the knowledge base linked to the service desk.

**[Permissions](#permissions) required**: Permission to access the service desk.
