---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}"
category: "Issue type properties"
writes_data: true
tool_note: "[[jira_set_issue_type_property]]"
---
# Jira v3 - Set issue type property

**Set issue type property** — `PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`

- Run by the tool [[jira_set_issue_type_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetype/{{param:issueTypeId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueTypeId` (path, string, required) — The ID of the issue type.
- `propertyKey` (path, string, required) — The key of the issue type property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "number": 5,
  "string": "string-value"
}
```

## Original description

Creates or updates the value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against an issue type.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
