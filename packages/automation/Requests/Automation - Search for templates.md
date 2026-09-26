---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: GET
path: "/rest/v1/template/search"
category: "Templates"
writes_data: false
tool_note: "[[automation_search_for_templates]]"
---
# Automation - Search for templates

**Search for templates** — `GET /rest/v1/template/search`

- Run by the tool [[automation_search_for_templates]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
GET {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/template/search?cursor={{param:cursor}}&limit={{param:limit}}&categories={{param:categories}}&ruleHome={{param:ruleHome}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `cursor` (query, string, optional) — The pagination cursor to use to fetch a page of results. Cursors are obtained via requests to the search API and should not be constructed manually.
- `limit` (query, string, optional) — Optional page size limit
- `categories` (query, string, optional) — Optional categories filter parameter
- `ruleHome` (query, string, optional) — If provided, only templates that apply to the ruleHome represented by the ARI will be returned. Used to limit results to templates applicable for a given project or product etc.

## Original description

Search for templates rules using the given query params.

Accepts either a combination of filter parameters, or a cursor, but not both.

**Deprecated:** The `links` field in the response body has recently changed to return just the query parameters instead of absolute links. See [the changelog notice](/cloud/automation/api/changelog/#1-august-2025).
