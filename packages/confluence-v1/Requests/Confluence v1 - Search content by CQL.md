---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/search"
category: "Content"
writes_data: false
tool_note: "[[confluence_v1_search_content_by_cql]]"
---
# Confluence v1 - Search content by CQL

**Search content by CQL** — `GET /wiki/rest/api/content/search`

- Run by the tool [[confluence_v1_search_content_by_cql]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/search?cql={{param:cql}}&cqlcontext={{param:cqlcontext}}&expand={{param:expand}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cql` (query, string, required) — The CQL string that is used to find the requested content.
- `cqlcontext` (query, string, optional) — The space, content, and content status to execute the search against. Specify this as an object with the following properties: - spaceKey Key of the space to search against. Optional.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards.
- `cursor` (query, string, optional) — Pointer to a set of search results, returned as part of the next or prev URL from the previous search call.
- `limit` (query, string, optional) — The maximum number of content objects to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the list of content that matches a Confluence Query Language
(CQL) query. For information on CQL, see:
[Advanced searching using CQL](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/).

Example initial call:
```
/wiki/rest/api/content/search?cql=type=page&limit=25
```

Example response:
```
{
  "results": [
    { ... },
    { ... },
    ...
    { ... }
  ],
  "limit": 25,
  "size": 25,
  ...
  "_links": {
    "base": "",
    "context": "",
    "next": "/rest/api/content/search?cql=type=page&limit=25&cursor=raNDoMsTRiNg",
    "self": ""
  }
}
```

When additional results are available, returns `next` and `prev` URLs to retrieve them in subsequent calls. The URLs each contain a cursor that points to the appropriate set of results. Use `limit` to specify the number of results returned in each call.
Example subsequent call (taken from example response):
```
/wiki/rest/api/content/search?cql=type=page&limit=25&cursor=raNDoMsTRiNg
```
The response to this will have a `prev` URL similar to the `next` in the example response.

If the expand query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query limit parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
Only content that the user has permission to view will be returned.
