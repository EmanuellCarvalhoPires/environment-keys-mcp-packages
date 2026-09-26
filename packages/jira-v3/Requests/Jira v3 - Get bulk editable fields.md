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
path: "/rest/api/3/bulk/issues/fields"
category: "Issue bulk operations"
writes_data: false
tool_note: "[[jira_get_bulk_editable_fields]]"
---
# Jira v3 - Get bulk editable fields

**Get bulk editable fields** — `GET /rest/api/3/bulk/issues/fields`

- Run by the tool [[jira_get_bulk_editable_fields]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/bulk/issues/fields?issueIdsOrKeys={{param:issueIdsOrKeys}}&searchText={{param:searchText}}&endingBefore={{param:endingBefore}}&startingAfter={{param:startingAfter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdsOrKeys` (query, string, required) — The IDs or keys of the issues to get editable fields from.
- `searchText` (query, string, optional) — (Optional)The text to search for in the editable fields.
- `endingBefore` (query, string, optional) — (Optional)The end cursor for use in pagination.
- `startingAfter` (query, string, optional) — (Optional)The start cursor for use in pagination.

## Original description

Use this API to get a list of fields visible to the user to perform bulk edit operations. You can pass single or multiple issues in the query to get eligible editable fields. This API uses pagination to return responses, delivering 50 fields at a time.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  Depending on the field, any field-specific permissions required to edit it.
