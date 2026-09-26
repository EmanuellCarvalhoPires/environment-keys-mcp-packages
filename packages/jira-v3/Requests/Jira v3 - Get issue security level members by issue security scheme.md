---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-level
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members"
category: "Issue security level"
writes_data: false
tool_note: "[[jira_get_issue_security_level_members_by_issue_security_scheme]]"
---
# Jira v3 - Get issue security level members by issue security scheme

**Get issue security level members by issue security scheme** — `GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members`

- Run by the tool [[jira_get_issue_security_level_members_by_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/{{param:issueSecuritySchemeId}}/members?startAt={{param:startAt}}&maxResults={{param:maxResults}}&issueSecurityLevelId={{param:issueSecurityLevelId}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueSecuritySchemeId` (path, string, required) — The ID of the issue security scheme. Use the Get issue security schemes operation to get a list of issue security scheme IDs.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `issueSecurityLevelId` (query, string, optional) — The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: issueSecurityLevelId=10000&issueSecurityLevelId=10001.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include: all Returns all expandable information.

## Original description

Returns issue security level members.

Only issue security level members in context of classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
