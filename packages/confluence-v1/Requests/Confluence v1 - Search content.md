---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/search
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/search"
category: "Search"
writes_data: false
tool_note: "[[confluence_v1_search_content]]"
---
# Confluence v1 - Search content

**Search content** — `GET /wiki/rest/api/search`

- Run by the tool [[confluence_v1_search_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/search?cql={{param:cql}}&cqlcontext={{param:cqlcontext}}&cursor={{param:cursor}}&next={{param:next}}&prev={{param:prev}}&limit={{param:limit}}&start={{param:start}}&includeArchivedSpaces={{param:includeArchivedSpaces}}&excludeCurrentSpaces={{param:excludeCurrentSpaces}}&excerpt={{param:excerpt}}&sitePermissionTypeFilter={{param:sitePermissionTypeFilter}}&_={{param:_}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cql` (query, string, required) — The CQL query to be used for the search. See Advanced Searching using CQL for instructions on how to build a CQL query.
- `cqlcontext` (query, string, optional) — The space, content, and content status to execute the search against. - spaceKey Key of the space to search against. Optional. - contentId ID of the content to search against. Optional.
- `cursor` (query, string, optional) — Pointer to a set of search results, returned as part of the next or prev URL from the previous search call.
- `next` (query, string, optional) — Query parameter next.
- `prev` (query, string, optional) — Query parameter prev.
- `limit` (query, string, optional) — The maximum number of content objects to return per page. Note, this may be restricted by fixed system limits.
- `start` (query, string, optional) — The start point of the collection to return
- `includeArchivedSpaces` (query, string, optional) — Whether to include content from archived spaces in the results.
- `excludeCurrentSpaces` (query, string, optional) — Whether to exclude current spaces and only show archived spaces.
- `excerpt` (query, string, optional) — The excerpt strategy to apply to the result
- `sitePermissionTypeFilter` (query, string, optional) — Filters users by permission type. Use none to default to licensed users, externalCollaborator for external/guest users, and all to include all permission types.
- `_` (query, string, optional) — Query parameter .
- `expand` (query, string, optional) — Query parameter expand.

## Original description

Searches for content using the
[Confluence Query Language (CQL)](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/).

**Note that CQL input queries submitted through the `/wiki/rest/api/search` endpoint no longer support user-specific fields like `user`, `user.fullname`, `user.accountid`, and `user.userkey`.** 
See this [deprecation notice](https://developer.atlassian.com/cloud/confluence/deprecation-notice-search-api/) for more details.

Example initial call:
```
/wiki/rest/api/search?cql=type=page&limit=25
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
    "next": "/rest/api/search?cql=type=page&limit=25&cursor=raNDoMsTRiNg",
    "self": ""
  }
}
```

When additional results are available, returns `next` and `prev` URLs to retrieve them in subsequent calls. The URLs each contain a cursor that points to the appropriate set of results. Use `limit` to specify the number of results returned in each call.

Example subsequent call (taken from example response):
```
/wiki/rest/api/search?cql=type=page&limit=25&cursor=raNDoMsTRiNg
```
The response to this will have a `prev` URL similar to the `next` in the example response.

If the expand query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query limit parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the entities. Note, only entities that the user has
permission to view will be returned.
