---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/notificationscheme"
category: "Issue notification schemes"
writes_data: false
tool_note: "[[jira_get_notification_schemes_paginated]]"
---
# Jira v3 - Get notification schemes paginated

**Get notification schemes paginated** — `GET /rest/api/3/notificationscheme`

- Run by the tool [[jira_get_notification_schemes_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/notificationscheme?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&projectId={{param:projectId}}&onlyDefault={{param:onlyDefault}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of notification schemes IDs to be filtered by
- `projectId` (query, string, optional) — The list of projects IDs to be filtered by
- `onlyDefault` (query, string, optional) — When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.

## Original description

Returns a [paginated](#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

*Note that you should allow for events without recipients to appear in responses.*

**[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.
