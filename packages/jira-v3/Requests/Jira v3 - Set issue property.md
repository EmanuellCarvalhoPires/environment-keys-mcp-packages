---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}"
category: "Issue properties"
writes_data: true
tool_note: "[[jira_set_issue_property]]"
---
# Jira v3 - Set issue property

**Set issue property** — `PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`

- Run by the tool [[jira_set_issue_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `propertyKey` (path, string, required) — The key of the issue property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of an issue's property. Use this resource to store custom data against an issue.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
