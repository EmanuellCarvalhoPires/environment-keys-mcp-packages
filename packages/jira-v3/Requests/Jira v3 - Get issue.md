---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_issue]]"
---
# Jira v3 - Get issue

**Get issue** — `GET /rest/api/3/issue/{issueIdOrKey}`

- Run by the tool [[jira_get_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}?fields={{param:fields}}&fieldsByKeys={{param:fieldsByKeys}}&expand={{param:expand}}&properties={{param:properties}}&updateHistory={{param:updateHistory}}&failFast={{param:failFast}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `fields` (query, string, optional) — A list of fields to return for the issue. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values: all Returns all fields.
- `fieldsByKeys` (query, string, optional) — Whether fields in fields are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID.
- `expand` (query, string, optional) — Use expand to include additional information about the issues in the response. This parameter accepts a comma-separated list.
- `properties` (query, string, optional) — A list of issue properties to return for the issue. This parameter accepts a comma-separated list. Allowed values: all Returns all issue properties.
- `updateHistory` (query, string, optional) — Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira. This also populates the JQL issues search lastViewed field.
- `failFast` (query, string, optional) — Whether to fail the request quickly in case of an error while loading fields for an issue. For failFast=true, if one field fails, the entire operation fails.

## Original description

Returns the details for an issue.

The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is the key of the issue found.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
