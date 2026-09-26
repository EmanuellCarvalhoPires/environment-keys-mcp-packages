---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetype/{issueTypeId}/properties"
category: "Issue type properties"
writes_data: false
tool_note: "[[jira_get_issue_type_property_keys]]"
---
# Jira v3 - Get issue type property keys

**Get issue type property keys** — `GET /rest/api/3/issuetype/{issueTypeId}/properties`

- Run by the tool [[jira_get_issue_type_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetype/{{param:issueTypeId}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueTypeId` (path, string, required) — The ID of the issue type.

## Original description

Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.
 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.
