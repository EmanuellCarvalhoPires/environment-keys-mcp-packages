---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/groups/picker"
category: "Groups"
writes_data: false
tool_note: "[[jira_find_groups]]"
---
# Jira v3 - Find groups

**Find groups** — `GET /rest/api/3/groups/picker`

- Run by the tool [[jira_find_groups]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/groups/picker?accountId={{param:accountId}}&query={{param:query}}&exclude={{param:exclude}}&excludeId={{param:excludeId}}&maxResults={{param:maxResults}}&caseInsensitive={{param:caseInsensitive}}&userName={{param:userName}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — This parameter is deprecated, setting it does not affect the results. To find groups containing a particular user, use Get user groups.
- `query` (query, string, optional) — The string to find in group names.
- `exclude` (query, string, optional) — As a group's name can change, use of excludeGroupIds is recommended to identify a group. A group to exclude from the result. To exclude multiple groups, provide an ampersand-separated list.
- `excludeId` (query, string, optional) — A group ID to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, excludeId=group1-id&excludeId=group2-id.
- `maxResults` (query, string, optional) — The maximum number of groups to return. The maximum number of groups that can be returned is limited by the system property jira.ajax.autocomplete.limit.
- `caseInsensitive` (query, string, optional) — Whether the search for groups should be case insensitive.
- `userName` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.

## Original description

Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results.

The primary use case for this resource is to populate a group picker suggestions list. To this end, the returned object includes the `html` field where the matched query term is highlighted in the group name with the HTML strong tag. Also, the groups list is wrapped in a response object that contains a header for use in the picker, specifically *Showing X of Y matching groups*.

The list returns with the groups sorted. If no groups match the list criteria, an empty list is returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without the required permission return an empty list.

*Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without this permission, calls where query is not an exact match to an existing group will return an empty list.
