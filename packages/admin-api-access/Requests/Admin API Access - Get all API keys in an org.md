---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-key
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/api-keys"
category: "API Key"
writes_data: false
---
# Admin API Access - Get all API keys in an org

**Get all API keys in an org** — `GET /orgs/{orgId}/api-keys`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get all API keys in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/api-keys?q={{param:q}}&keyType={{param:keyType}}&expiresAtSearchType={{param:expiresAtSearchType}}&expiresAtUom={{param:expiresAtUom}}&expiresAtValue={{param:expiresAtValue}}&expiresAtFrom={{param:expiresAtFrom}}&expiresAtTo={{param:expiresAtTo}}&expiresAtRangeFrom={{param:expiresAtRangeFrom}}&expiresAtRangeTo={{param:expiresAtRangeTo}}&lastActiveAtSearchType={{param:lastActiveAtSearchType}}&lastActiveAtUom={{param:lastActiveAtUom}}&lastActiveAtValue={{param:lastActiveAtValue}}&lastActiveAtFrom={{param:lastActiveAtFrom}}&lastActiveAtTo={{param:lastActiveAtTo}}&lastActiveAtRangeFrom={{param:lastActiveAtRangeFrom}}&lastActiveAtRangeTo={{param:lastActiveAtRangeTo}}&sort={{param:sort}}&pageSize={{param:pageSize}}&cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `q` (query, string, optional) — Free text search filter to be applied to API token results. Query will be applied using a fuzzy, case-insensitive search. Will target token label, user.name, and user.email.
- `keyType` (query, string, optional) — Key type filter for API keys to return keys of a certain type.
- `expiresAtSearchType` (query, string, optional) — Filter the API keys by expiry date. Depending on search type provided, additional parameters shall be supplied.
- `expiresAtUom` (query, string, optional) — Filter the API keys by expiry date. Unit of measure represents the scale of time for window search. This parameter is required if searching on expiry date using gt or lt search.
- `expiresAtValue` (query, string, optional) — Filter the API tokens by last active date. This represents the value of time scale for window search. This parameter is required if searching on expiry date using gt or lt search.
- `expiresAtFrom` (query, string, optional) — Filter the API tokens by last active date. This represents the starting timestamp for a window search. Either this parameter or expiresAtTo is required if searching on expiry date using range search.
- `expiresAtTo` (query, string, optional) — Filter the API tokens by last active date. This represents the ending timestamp for a window search. Either this parameter or expiresAtFrom is required if searching on expiry date using range search.
- `expiresAtRangeFrom` (query, string, optional) — Filter the API keys by expiry date range. This represents the starting relative time window for a range time search.
- `expiresAtRangeTo` (query, string, optional) — Filter the API keys by expiry date range. This represents the ending relative time window for a range time search.
- `lastActiveAtSearchType` (query, string, optional) — Filter the API tokens by last active date. This parameter is required if searching on last active date. Depending on search type provided, additional parameters shall be supplied.
- `lastActiveAtUom` (query, string, optional) — Filter the API tokens by last active date. Unit of measure represents the scale of time for window search. This parameter is required if searching on last active date using gt or lt search.
- `lastActiveAtValue` (query, string, optional) — Filter the API tokens by last active date. This represents the value of time scale for window search. This parameter is required if searching on last active date using gt or lt search.
- `lastActiveAtFrom` (query, string, optional) — Filter the API tokens by last active date. This represents the starting timestamp for a window search.
- `lastActiveAtTo` (query, string, optional) — Filter the API tokens by last active date. This represents the ending timestamp for a window search.
- `lastActiveAtRangeFrom` (query, string, optional) — Filter the API tokens by last active date range. This represents the starting relative time window for a range time search.
- `lastActiveAtRangeTo` (query, string, optional) — Filter the API tokens by last active date range. This represents the ending relative time window for a range time search.
- `sort` (query, string, optional) — Sort the API keys based on the following criteria: ascending is represented with + as the first character (optional); descending is represented with - as the first character.
- `pageSize` (query, string, optional) — Select the number of records to include in the results.
- `cursor` (query, string, optional) — Navigate to a specific page of paginated results. In a given response, it may include a self, next, and prev cursor to fetch the respective set of paginated results.

## Original description

Gets all user API keys in an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:keys:admin`
