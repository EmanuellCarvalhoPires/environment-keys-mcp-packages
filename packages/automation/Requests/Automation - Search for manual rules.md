---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/manual-rules
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: GET
path: "/rest/v1/rule/manual/search"
category: "Manual rules"
writes_data: false
tool_note: "[[automation_search_for_manual_rules]]"
---
# Automation - Search for manual rules

**Search for manual rules** — `GET /rest/v1/rule/manual/search`

- Run by the tool [[automation_search_for_manual_rules]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
GET {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/manual/search?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `cursor` (query, string, required) — The pagination cursor to use to fetch a page of results. Cursors are obtained via requests to the search API and should not be constructed manually.
- `limit` (query, string, optional) — Optional page size limit

## Original description

Search for manually-triggered rules using the given query params.

**Note:** Currently only `cursor` is allowed as parameter for the GET operation. 
Use the POST operation to perform the initial search.

**Deprecated:** The `links` field in the response body has recently changed to return just the query parameters instead of absolute links. See [the changelog notice](/cloud/automation/api/changelog/#1-august-2025).
