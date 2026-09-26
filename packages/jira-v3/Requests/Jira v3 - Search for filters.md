---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/filter/search"
category: "Filters"
writes_data: false
tool_note: "[[jira_search_for_filters]]"
---
# Jira v3 - Search for filters

**Search for filters** — `GET /rest/api/3/filter/search`

- Run by the tool [[jira_search_for_filters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/search?filterName={{param:filterName}}&accountId={{param:accountId}}&owner={{param:owner}}&groupname={{param:groupname}}&groupId={{param:groupId}}&projectId={{param:projectId}}&id={{param:id}}&orderBy={{param:orderBy}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&expand={{param:expand}}&overrideSharePermissions={{param:overrideSharePermissions}}&isSubstringMatch={{param:isSubstringMatch}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `filterName` (query, string, optional) — String used to perform a case-insensitive partial match with name.
- `accountId` (query, string, optional) — User account ID used to return filters with the matching owner.accountId. This parameter cannot be used with owner.
- `owner` (query, string, optional) — This parameter is deprecated because of privacy changes. Use accountId instead. See the migration guide for details. User name used to return filters with the matching owner.name.
- `groupname` (query, string, optional) — As a group's name can change, use of groupId is recommended to identify a group. Group name used to returns filters that are shared with a group that matches sharePermissions.group.groupname.
- `groupId` (query, string, optional) — Group ID used to returns filters that are shared with a group that matches sharePermissions.group.groupId. This parameter cannot be used with the groupname parameter.
- `projectId` (query, string, optional) — Project ID used to returns filters that are shared with a project that matches sharePermissions.project.id.
- `id` (query, string, optional) — The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Do not exceed 200 filter IDs.
- `orderBy` (query, string, optional) — Order the results by a field: description Sorts by filter description. Note that this sorting works independently of whether the expand to display the description field is in use.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include: description Returns the description of the filter.
- `overrideSharePermissions` (query, string, optional) — EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with Administer Jira global permission.
- `isSubstringMatch` (query, string, optional) — When true this will perform a case-insensitive substring match for the provided filterName. When false the filter name will be searched using full text search syntax.

## Original description

Returns a [paginated](#pagination) list of filters. Use this operation to get:

 *  specific filters, by defining `id` only.
 *  filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, only the following filters that match the query parameters are returned:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.
