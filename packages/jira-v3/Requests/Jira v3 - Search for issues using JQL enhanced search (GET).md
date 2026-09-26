---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/search/jql"
category: "Issue search"
writes_data: false
tool_note: "[[jira_search_for_issues_using_jql_enhanced_search_get]]"
---
# Jira v3 - Search for issues using JQL enhanced search (GET)

**Search for issues using JQL enhanced search (GET)** — `GET /rest/api/3/search/jql`

- Run by the tool [[jira_search_for_issues_using_jql_enhanced_search_get]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/search/jql?jql={{param:jql}}&nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}&fields={{param:fields}}&expand={{param:expand}}&properties={{param:properties}}&fieldsByKeys={{param:fieldsByKeys}}&failFast={{param:failFast}}&reconcileIssues={{param:reconcileIssues}}&includeArchivedProjects={{param:includeArchivedProjects}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `jql` (query, string, optional) — A JQL expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction. Example of an unbounded query: order by key desc.
- `nextPageToken` (query, string, optional) — The token for a page to fetch that is not the first page. The first page has a nextPageToken of null. Use the nextPageToken to fetch the next page of issues.
- `maxResults` (query, string, optional) — The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields or properties are requested.
- `fields` (query, string, optional) — A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include: all Returns all fields.
- `expand` (query, string, optional) — Use expand to include additional information about issues in the response. Note that, unlike the majority of instances where expand is specified, expand is defined as a comma-delimited string of value…
- `properties` (query, string, optional) — A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list.
- `fieldsByKeys` (query, string, optional) — Reference fields by their key (rather than ID). The default is false.
- `failFast` (query, string, optional) — Fail this request early if we can't retrieve all field data.
- `reconcileIssues` (query, string, optional) — Strong consistency issue ids to be reconciled with search results. Accepts max 50 ids. This list of ids should be consistent with each paginated request across different pages.
- `includeArchivedProjects` (query, string, optional) — Whether to also return issues that belong to archived projects. Issues in archived projects are excluded by default.

## Original description

Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned search results. If you need [read-after-write](https://developer.atlassian.com/cloud/jira/platform/search-and-reconcile/) consistency, you can utilize the `reconcileIssues` parameter to ensure stronger consistency assurances. This operation can be accessed anonymously.

If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-rest-api-3-search-post) version of this resource.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
