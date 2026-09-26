---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}"
category: "Issue type properties"
writes_data: false
tool_note: "[[jira_get_issue_type_property]]"
---
# Jira v3 - Get issue type property

**Get issue type property** — `GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`

- Run by the tool [[jira_get_issue_type_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetype/{{param:issueTypeId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueTypeId` (path, string, required) — The ID of the issue type.
- `propertyKey` (path, string, required) — The key of the property. Use Get issue type property keys to get a list of all issue type property keys.

## Original description

Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type.
 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.
