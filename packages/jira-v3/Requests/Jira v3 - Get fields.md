---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_fields]]"
---
# Jira v3 - Get fields

**Get fields** — `GET /rest/api/3/field`

- Run by the tool [[jira_get_fields]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns system and custom issue fields according to the following rules:

 *  Fields that cannot be added to the issue navigator are always returned.
 *  Fields that cannot be placed on an issue screen are always returned.
 *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches.
 *  Fields that are not associated to any used field configurations or screens are not returned.
 *  For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
