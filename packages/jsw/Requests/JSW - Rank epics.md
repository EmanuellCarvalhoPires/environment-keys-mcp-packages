---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/epic/{epicIdOrKey}/rank"
category: "Epic"
writes_data: true
tool_note: "[[jsw_rank_epics]]"
---
# JSW - Rank epics

**Rank epics** — `PUT /rest/agile/1.0/epic/{epicIdOrKey}/rank`

- Run by the tool [[jsw_rank_epics]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/epic/{{param:epicIdOrKey}}/rank
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `epicIdOrKey` (path, string, required) — The id or key of the epic to rank.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "rankBeforeEpic": "10000",
  "rankCustomFieldId": 10521
}
```

## Original description

Moves (ranks) an epic before or after a given epic.

If rankCustomFieldId is not defined, the default rank field will be used.

**Note:** This operation does not work for epics in next-gen projects.
