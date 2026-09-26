---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/knowledgebase
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/knowledgebase/article"
category: "Knowledgebase"
writes_data: false
tool_note: "[[jsm_get_articles]]"
---
# JSM - Get articles

**Get articles** — `GET /rest/servicedeskapi/knowledgebase/article`

- Run by the tool [[jsm_get_articles]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/knowledgebase/article?query={{param:query}}&highlight={{param:highlight}}&start={{param:start}}&limit={{param:limit}}&cursor={{param:cursor}}&prev={{param:prev}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — The string used to filter the articles (required).
- `highlight` (query, string, required) — If set to true matching query term in the title and excerpt will be highlighted using the @@@hl@@@term@@@endhl@@@ syntax. Default: false.
- `start` (query, string, optional) — (Deprecated) The starting index of the returned objects. Base index: 0.
- `limit` (query, string, optional) — The maximum number of items to return per page. Default: 50.
- `cursor` (query, string, optional) — Pointer to a set of search results, returned as part of the next or prev URL from the previous search call.
- `prev` (query, string, optional) — Should navigate to the previous page. Defaulted to false. Set to true as part of prev URL from the previous search call.

## Original description

Returns articles which match the given query string across all service desks.

**[Permissions](#permissions) required**: Permission to access the [customer portal](https://confluence.atlassian.com/servicedeskcloud/configuring-the-customer-portal-732528918.html).
