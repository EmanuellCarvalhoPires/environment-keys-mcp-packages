---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/limit/adf/report"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_issue_adf_limit_report]]"
---
# Jira v3 - Get issue adf limit report

**Get issue adf limit report** — `GET /rest/api/3/issue/limit/adf/report`

- Run by the tool [[jira_get_issue_adf_limit_report]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/limit/adf/report?isReturningKeys={{param:isReturningKeys}}&fieldType={{param:fieldType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `isReturningKeys` (query, string, optional) — Return issue keys instead of issue ids in the response. Usage: Add ?isReturningKeys=true to the end of the path to request issue keys.
- `fieldType` (query, string, optional) — Restrict the report to the given ADF field types. Defaults to every ADF field type. For sites with a high issue volume, consider requesting field types individually to avoid timeouts.

## Original description

Returns all issues whose ADF (rich text) field data breaches the universal ADF size limit.

Unlike the issue limit report, which reports issues breaching per-issue entity *count* limits, this endpoint reports issues whose ADF field *byte size* exceeds that limit. The reported ADF field types are `comment_adf`, `worklog_adf`, `customfield_adf`, `description_adf` and `environment_adf`. The reported value for each issue is the number of breaching entities for that field (always 1 for the single-value description and environment fields).

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
