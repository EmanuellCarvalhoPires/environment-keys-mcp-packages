---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/group-and-user-picker
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/groupuserpicker"
category: "Group and user picker"
writes_data: false
tool_note: "[[jira_find_users_and_groups]]"
---
# Jira v3 - Find users and groups

**Find users and groups** — `GET /rest/api/3/groupuserpicker`

- Run by the tool [[jira_find_users_and_groups]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/groupuserpicker?query={{param:query}}&maxResults={{param:maxResults}}&showAvatar={{param:showAvatar}}&fieldId={{param:fieldId}}&projectId={{param:projectId}}&issueTypeId={{param:issueTypeId}}&avatarSize={{param:avatarSize}}&caseInsensitive={{param:caseInsensitive}}&excludeConnectAddons={{param:excludeConnectAddons}}&includeAiAgents={{param:includeAiAgents}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — The search string.
- `maxResults` (query, string, optional) — The maximum number of items to return in each list.
- `showAvatar` (query, string, optional) — Whether the user avatar should be returned. If an invalid value is provided, the default value is used.
- `fieldId` (query, string, optional) — The custom field ID of the field this request is for.
- `projectId` (query, string, optional) — The ID of a project that returned users and groups must have permission to view. To include multiple projects, provide an ampersand-separated list. For example, projectId=10000&projectId=10001.
- `issueTypeId` (query, string, optional) — The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list.
- `avatarSize` (query, string, optional) — The size of the avatar to return. If an invalid value is provided, the default value is used.
- `caseInsensitive` (query, string, optional) — Whether the search for groups should be case insensitive.
- `excludeConnectAddons` (query, string, optional) — Whether Connect app users and groups should be excluded from the search results. If an invalid value is provided, the default value is used.
- `includeAiAgents` (query, string, optional) — Whether AI Agents should be included in the search results. If an invalid value is provided, the default value is used.

## Original description

Returns a list of users and groups matching a string. The string is used:

 *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.
 *  for groups, to find a case-sensitive match with group name.

For example, if the string *tin* is used, records with the display name *Tina*, email address *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

Optionally, the search can be refined to:

 *  the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific:
    
     *  projects.
     *  issue types.
    
    If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned.
 *  not return Connect app users and groups.
 *  return groups that have a case-insensitive match with the query.

The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an `html` field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically *Showing X of Y matching groups*.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/yodKLg).
