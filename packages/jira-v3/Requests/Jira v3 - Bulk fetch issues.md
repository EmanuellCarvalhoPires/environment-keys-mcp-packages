---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/bulkfetch"
category: "Issues"
writes_data: false
tool_note: "[[jira_bulk_fetch_issues]]"
---
# Jira v3 - Bulk fetch issues

**Bulk fetch issues** — `POST /rest/api/3/issue/bulkfetch`

- Run by the tool [[jira_bulk_fetch_issues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/bulkfetch
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "expand": [
    "names"
  ],
  "fields": [
    "summary",
    "project",
    "assignee"
  ],
  "fieldsByKeys": false,
  "issueIdsOrKeys": [
    "EX-1",
    "EX-2",
    "10005"
  ],
  "properties": []
}
```

## Original description

Returns the details for a set of requested issues.

By default you can request up to 100 issues in a single call. You can request up to 1000 issues in a single call when the request is shaped so that it can be served efficiently, that is, when *all* of the following are true:

 *  the `fields` parameter explicitly names at least one field to include — a request that contains only exclusions is **not** eligible, and neither are the `*all` and `*navigable` wildcards or the default navigable field set, because the number of resolved fields depends on the site's configuration;
 *  no more than 100 fields are explicitly included;
 *  none of the included fields returns multiple values (for example `comment`, `worklog`, or `attachment`); and
 *  the `expand` parameter does not include `changelog`, `editmeta`, `operations`, `renderedFields`, `transitions`, or `versionedRepresentations`.

Requests that do not meet all of these conditions can include at most 100 issues; larger requests are rejected with a 400 error.

Each issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned.

Issues will be returned in ascending `id` order. If there are errors, Jira will return a list of issues which couldn't be fetched along with error messages.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
