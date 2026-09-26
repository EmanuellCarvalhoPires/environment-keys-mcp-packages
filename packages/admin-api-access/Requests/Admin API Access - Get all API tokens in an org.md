---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-token
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/api-tokens"
category: "API Token"
writes_data: false
---
# Admin API Access - Get all API tokens in an org

**Get all API tokens in an org** — `GET /orgs/{orgId}/api-tokens`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get all API tokens in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/api-tokens?q={{param:q}}&status={{param:status}}&createdAtSearchType={{param:createdAtSearchType}}&createdAtUom={{param:createdAtUom}}&createdAtValue={{param:createdAtValue}}&createdAtFrom={{param:createdAtFrom}}&createdAtTo={{param:createdAtTo}}&createdAtRangeFrom={{param:createdAtRangeFrom}}&createdAtRangeTo={{param:createdAtRangeTo}}&lastActiveAtSearchType={{param:lastActiveAtSearchType}}&lastActiveAtUom={{param:lastActiveAtUom}}&lastActiveAtValue={{param:lastActiveAtValue}}&lastActiveAtFrom={{param:lastActiveAtFrom}}&lastActiveAtTo={{param:lastActiveAtTo}}&lastActiveAtRangeFrom={{param:lastActiveAtRangeFrom}}&lastActiveAtRangeTo={{param:lastActiveAtRangeTo}}&sort={{param:sort}}&pageSize={{param:pageSize}}&cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `q` (query, string, optional) — Free text search filter to be applied to API token results. Query will be applied using a fuzzy, case-insensitive search. Will target token label, user.name, and user.email.
- `status` (query, string, optional) — Filter the API tokens by status to retrieve tokens of a specific type.
- `createdAtSearchType` (query, string, optional) — Filter the API tokens by creation date. This parameter is required if searching on creation date. Depending on search type provided, additional parameters shall be supplied.
- `createdAtUom` (query, string, optional) — Filter the API tokens by creation date. Unit of measure represents the scale of time for window search. This parameter is required if searching on creation date using gt or lt search.
- `createdAtValue` (query, string, optional) — Filter the API tokens by creation date. This represents the value of time scale for window search. This parameter is required if searching on creation date using gt or lt search.
- `createdAtFrom` (query, string, optional) — Filter the API tokens by creation date. This represents the starting timestamp for a window search. Either this parameter or createdAtTo is required if searching on creation date using range search.
- `createdAtTo` (query, string, optional) — Filter the API tokens by creation date. This represents the ending timestamp for a window search. Either this parameter or createdAtFrom is required if searching on creation date using range search.
- `createdAtRangeFrom` (query, string, optional) — Filter the API tokens by creation date range. This represents the starting relative time window for a range time search.
- `createdAtRangeTo` (query, string, optional) — Filter the API tokens by creation date range. This represents the ending relative time window for a range time search.
- `lastActiveAtSearchType` (query, string, optional) — Filter the API tokens by last active date. This parameter is required if searching on last active date. Depending on search type provided, additional parameters shall be supplied.
- `lastActiveAtUom` (query, string, optional) — Filter the API tokens by last active date. Unit of measure represents the scale of time for window search. This parameter is required if searching on last active date using gt or lt search.
- `lastActiveAtValue` (query, string, optional) — Filter the API tokens by last active date. This represents the value of time scale for window search. This parameter is required if searching on last active date using gt or lt search.
- `lastActiveAtFrom` (query, string, optional) — Filter the API tokens by last active date. This represents the starting timestamp for a window search.
- `lastActiveAtTo` (query, string, optional) — Filter the API tokens by last active date. This represents the ending timestamp for a window search.
- `lastActiveAtRangeFrom` (query, string, optional) — Filter the API tokens by last active date range. This represents the starting relative time window for a range time search.
- `lastActiveAtRangeTo` (query, string, optional) — Filter the API tokens by last active date range. This represents the ending relative time window for a range time search.
- `sort` (query, string, optional) — Sort the API tokens based on the following criteria: ascending is represented with + as the first character (optional); descending is represented with - as the first character.
- `pageSize` (query, string, optional) — Select the number of records to include in the results.
- `cursor` (query, string, optional) — Navigate to a specific page of paginated results. In a given response, it may include a self, next, and prev cursor to fetch the respective set of paginated results.

## Original description

Gets all [user API tokens](/cloud/admin/api-access/rest/intro/#API%20Tokens) in an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:tokens:admin`
