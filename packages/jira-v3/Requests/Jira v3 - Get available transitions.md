---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/bulk/issues/transition"
category: "Issue bulk operations"
writes_data: false
tool_note: "[[jira_get_available_transitions]]"
---
# Jira v3 - Get available transitions

**Get available transitions** — `GET /rest/api/3/bulk/issues/transition`

- Run by the tool [[jira_get_available_transitions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/bulk/issues/transition?issueIdsOrKeys={{param:issueIdsOrKeys}}&endingBefore={{param:endingBefore}}&startingAfter={{param:startingAfter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdsOrKeys` (query, string, required) — Comma (,) separated Ids or keys of the issues to get transitions available for them.
- `endingBefore` (query, string, optional) — (Optional)The end cursor for use in pagination.
- `startingAfter` (query, string, optional) — (Optional)The start cursor for use in pagination.

## Original description

Use this API to retrieve a list of transitions available for the specified issues that can be used or bulk transition operations. You can submit either single or multiple issues in the query to obtain the available transitions.

The response will provide the available transitions for issues, organized by their respective workflows. **Only the transitions that are common among the issues within that workflow and do not involve any additional field updates will be included.** For bulk transitions that require additional field updates, please utilise the Jira Cloud UI.

You can request available transitions for up to 1,000 issues in a single operation. This API uses pagination to return responses, delivering 50 workflows at a time.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
