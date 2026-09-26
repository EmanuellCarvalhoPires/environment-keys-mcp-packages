---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/webhook/failed"
category: "Webhooks"
writes_data: false
tool_note: "[[jira_get_failed_webhooks]]"
---
# Jira v3 - Get failed webhooks

**Get failed webhooks** — `GET /rest/api/3/webhook/failed`

- Run by the tool [[jira_get_failed_webhooks]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/webhook/failed?maxResults={{param:maxResults}}&after={{param:after}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `maxResults` (query, string, optional) — The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all rec…
- `after` (query, string, optional) — The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch.

## Original description

Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.

After 72 hours the failure may no longer be returned by this operation.

The oldest failure is returned first.

This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

**[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.
