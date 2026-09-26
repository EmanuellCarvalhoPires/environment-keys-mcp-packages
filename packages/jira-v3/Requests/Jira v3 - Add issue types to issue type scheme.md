---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_add_issue_types_to_issue_type_scheme]]"
---
# Jira v3 - Add issue types to issue type scheme

**Add issue types to issue type scheme** — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype`

- Run by the tool [[jira_add_issue_types_to_issue_type_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescheme/{{param:issueTypeSchemeId}}/issuetype
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueTypeSchemeId` (path, string, required) — The ID of the issue type scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeIds": [
    "10000",
    "10002",
    "10003"
  ]
}
```

## Original description

Adds issue types to an issue type scheme.

The added issue types are appended to the issue types list.

If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
