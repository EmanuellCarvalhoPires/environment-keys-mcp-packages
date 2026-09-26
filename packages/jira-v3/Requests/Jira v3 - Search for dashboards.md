---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/search"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_search_for_dashboards]]"
---
# Jira v3 - Search for dashboards

**Search for dashboards** — `GET /rest/api/3/dashboard/search`

- Run by the tool [[jira_search_for_dashboards]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/search?dashboardName={{param:dashboardName}}&accountId={{param:accountId}}&owner={{param:owner}}&groupname={{param:groupname}}&groupId={{param:groupId}}&projectId={{param:projectId}}&orderBy={{param:orderBy}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&status={{param:status}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `dashboardName` (query, string, optional) — String used to perform a case-insensitive partial match with name.
- `accountId` (query, string, optional) — User account ID used to return dashboards with the matching owner.accountId. This parameter cannot be used with the owner parameter.
- `owner` (query, string, optional) — This parameter is deprecated because of privacy changes. Use accountId instead. See the migration guide for details. User name used to return dashboards with the matching owner.name.
- `groupname` (query, string, optional) — As a group's name can change, use of groupId is recommended. Group name used to return dashboards that are shared with a group that matches sharePermissions.group.name.
- `groupId` (query, string, optional) — Group ID used to return dashboards that are shared with a group that matches sharePermissions.group.groupId. This parameter cannot be used with the groupname parameter.
- `projectId` (query, string, optional) — Project ID used to returns dashboards that are shared with a project that matches sharePermissions.project.id.
- `orderBy` (query, string, optional) — Order the results by a field: description Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `status` (query, string, optional) — The status to filter by. It may be active, archived or deleted.
- `expand` (query, string, optional) — Use expand to include additional information about dashboard in the response. This parameter accepts a comma-separated list.

## Original description

Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned:

 *  Dashboards owned by the user. Not returned for anonymous users.
 *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
 *  Dashboards shared with a private project that the user can browse. Not returned for anonymous users.
 *  Dashboards shared with a public project.
 *  Dashboards shared with the public.
